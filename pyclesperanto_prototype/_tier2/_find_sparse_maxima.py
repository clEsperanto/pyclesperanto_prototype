from .._tier0 import Image
from .._tier0 import plugin_function

@plugin_function(categories=['binarize', 'in assistant'])
def find_sparse_maxima(image: Image, destination: Image = None, max_distance: int = 1, prominence: float = 0,
                       max_iterations=2):
    """
    Finds local maxima, extends them so that all below a given distance touch and then removes touching neighbors
    which have a lower maximum intensity than the local maximum intensity minus a given prominence value.

    The returned binary image may contain regions marked and not just single spots.

    It is recommended to process images with isotropic pixel size only.

    Parameters
    ----------
    image : Image
        intensity image or distace map
    destination : Image, optional
        binary output image
    max_distance : int
        the local maximum intensity threshold is determined from labels that are closer than this value.
    prominence
        intensity threshold. All local maxima are excluded with maximum intensity below this value. Furthermore, all
        local maxima are excluded that have local maximum close by that has a value higher than hte own maximum value
        plus prominence
    max_iterations
        The algorithm runs iteratively, excluding neighbors, determining neighbors again and excluding again.

    Returns
    -------

    """
    import numpy as np
    from .._tier1 import find_maxima_plateaus
    from .._tier1 import greater_constant
    from .._tier1 import binary_and
    from .._tier4 import connected_components_labeling_box
    from .._tier9 import statistics_of_background_and_labelled_pixels
    from .._tier0 import push_zyx
    from .._tier4 import extend_labels_with_maximum_radius
    from .._tier1 import generate_touch_matrix
    from .._tier1 import set_row
    from .._tier1 import set_column
    from .._tier2 import maximum_of_touching_neighbors
    from .._tier1 import add_image_and_scalar
    from .._tier1 import greater_or_equal
    from .._tier0 import create_like
    from .._tier1 import set_ramp_x
    from .._tier1 import multiply_images
    from .._tier2 import sum_of_all_pixels
    from .._tier1 import replace_intensities

    extended_labels = destination  # re-use memory

    maxima_plateaus = find_maxima_plateaus(image)
    binary = greater_constant(image, constant=prominence)

    temp = destination  # re-use memory

    binary_and(maxima_plateaus, binary, temp)

    labels = connected_components_labeling_box(temp)

    props = statistics_of_background_and_labelled_pixels(image, labels)
    maximum_intensities = push_zyx(np.asarray([[p.max_intensity for p in props]]))
    local_maximum_intensities = None
    thresholds = None

    #print("initial labels")
    #cle.imshow(labels, labels=True)

    former_sum_labels = 0

    for i in range(0, max_iterations):
        print("i", i)
        extend_labels_with_maximum_radius(labels, extended_labels, int(max_distance / 2 + 0.5))

        touch_matrix = generate_touch_matrix(extended_labels)
        set_column(touch_matrix, 0, 0)
        set_row(touch_matrix, 0, 0)

        local_maximum_intensities = maximum_of_touching_neighbors(maximum_intensities, touch_matrix,
                                                                      local_maximum_intensities)
        thresholds = add_image_and_scalar(local_maximum_intensities, thresholds, -prominence)

        #print("extended_labels")
        #cle.imshow(labels, labels=True)

        # print(local_maximum_intensities)
        # print(maximum_intensities)
        # print(thresholds)

        binary_vector = greater_or_equal(maximum_intensities, thresholds)
        labels_to_keep = create_like(binary_vector)
        set_ramp_x(labels_to_keep)

        labels_to_keep = multiply_images(binary_vector, labels_to_keep)

        sum_labels = sum_of_all_pixels(labels_to_keep)
        print(sum_labels)
        if former_sum_labels == sum_labels:
            print("find_sparse_maxima converged. Jeey!")
            break
        former_sum_labels = sum_labels

        labels = replace_intensities(labels, labels_to_keep)

        #cle.imshow(labels, labels=True)
        if (i == max_iterations - 1):
            from warnings import warn
            warn("Maximum number of iterations reached in find_sparse_maxima. The algorithm did not converge.")

    greater_constant(labels, destination, constant=0)

    return destination