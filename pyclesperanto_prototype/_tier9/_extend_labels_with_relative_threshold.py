from .._tier0 import Image, plugin_function


@plugin_function(categories=['combine', 'label processing', 'in assistant'])
def extend_labels_with_relative_threshold(intensity_image: Image, labels_input: Image, labels_destination: Image = None,
                                          relative_threshold: float = 0.5, extension_step: int = 2,
                                          max_iterations: int = 10):
    """
    Iteratively extends labels as long as underlying pixel values are above a given threshold. The threshold is
    specified relative to the maximum intensity in the label.

    The maximum radius this operation can reach pixels is extension_step times max_iterations.

    This function expects pixel intensities above 0.

    It is recommended to process images with isotropic pixel size only.

    Parameters
    ----------
    intensity_image : Image
    labels_input : Image
    labels_destination : Image, optional
    relative_threshold : float, optional
        between 0 and 1.
    extension_step
        with every step, more surrounding pixels are checked if their intensity is above the threshold. If the image has
        many local maxima and/or sharp edges, the extension step should be rater short.
    max_iterations
        Exection stops after that many extensions.

    Returns
    -------

    """
    from .._tier9 import statistics_of_background_and_labelled_pixels
    from .._tier9 import statistics_of_labelled_pixels
    from .._tier1 import multiply_image_and_scalar
    from .._tier4 import extend_labels_with_maximum_radius
    from .._tier1 import replace_intensities
    from .._tier1 import greater_or_equal
    from .._tier1 import multiply_images
    from .._tier2 import sum_of_all_pixels
    from .._tier2 import maximum_of_all_pixels
    from .._tier0 import push_zyx
    from .._tier1 import copy
    from .._tier1 import set_column
    import numpy as np

    import time
    start_time = time.time()

    props = statistics_of_labelled_pixels(intensity_image, labels_input, measure_shape=False)
    copy(labels_input, labels_destination)

    maximum_intensities = push_zyx(np.asarray([[p.max_intensity for p in props]]))
    thresholds = multiply_image_and_scalar(maximum_intensities, scalar=relative_threshold)
    #print(thresholds)

    # set the threshold of the background to an unreachable value
    max_intensity = maximum_of_all_pixels(thresholds)
    set_column(thresholds, 0, max_intensity + 1)

    # print(maximum_intensities)
    # print(thresholds)

    extended_labels = None
    local_threshold = None
    binary_image = None

    former_number_of_labelled_pixels = 0

    for i in range(0, max_iterations):
        #from .._tier9 import imshow
        #print(i)
        #imshow(labels_destination)

        extended_labels = extend_labels_with_maximum_radius(labels_destination, extended_labels, extension_step)
        local_threshold = replace_intensities(extended_labels, thresholds, local_threshold)
        binary_image = greater_or_equal(intensity_image, local_threshold, binary_image)

        from .._tier0 import create_like
        temp = create_like(labels_destination)
        copy(labels_destination, temp)

        labels_destination = multiply_images(extended_labels, binary_image, labels_destination)

        #from .._tier3 import absolute_difference
        #imshow(absolute_difference(temp, labels_destination))
        #imshow(labels_destination)


        number_of_labelled_pixels = sum_of_all_pixels(binary_image)
        #print(number_of_labelled_pixels)

        if number_of_labelled_pixels == former_number_of_labelled_pixels:
            print("extend_labels_with_relative_threshold converged after " + str(i) + ". Jeey!")
            break
        former_number_of_labelled_pixels = number_of_labelled_pixels

        if (i == max_iterations - 1):
            from warnings import warn
            warn(
                "Maximum number of iterations reached in extend_labels_with_relative_threshold. The algorithm did not converge.")

    print("extend_labels_with_relative_threshold took " + str(time.time() - start_time) + "s")

    return labels_destination
