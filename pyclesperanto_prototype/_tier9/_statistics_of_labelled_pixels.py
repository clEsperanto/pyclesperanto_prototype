from warnings import warn

from skimage.measure import regionprops

from .._tier0 import Image
from .._tier0 import create_none
from .._tier0 import plugin_function

@plugin_function(output_creator=create_none)
def statistics_of_labelled_pixels(intensity_image : Image = None, label_image : Image = None):
    """Determines bounding box, area (in pixels/voxels), min, max, mean, standard deviation of the intensity and some
    shape descriptors of labelled objects in a label map and corresponding pixels in the original image.
    
    Instead of a label map, you can also use a binary image as a binary image is a label map with just one label.

        Note: the parameter order is different compared to regionprops.


    Parameters
    ----------
    input : Image
    labelmap : Image

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_statisticsOfLabelledPixels
    """

    from .._tier0 import create
    from .._tier0 import create_like
    from .._tier1 import set
    from .._tier1 import sum_y_projection
    from .._tier1 import minimum_y_projection
    from .._tier1 import maximum_y_projection
    from .._tier1 import crop
    from .._tier1 import paste
    from .._tier1 import divide_images
    from .._tier1 import set_plane
    from .._tier0 import pull
    from .._tier1 import power
    from .._tier2 import maximum_of_all_pixels
    import numpy as np

    # check if label image and intensity image a properly set
    if intensity_image is None and label_image is None:
        raise ValueError("Either intensity image or labels must be set")
    if label_image is None:
        warn("No label image provided. All pixels will be analysed in one group.")
        label_image = create_like(intensity_image)
        set(label_image, 1) # all pixels belong to label 1
    if intensity_image is None:
        intensity_image = label_image

    # when copying measurements, we skip the first column, as we don't analyse background
    measurements_start_x = 1

    # determine size of temporary images
    num_labels = int(maximum_of_all_pixels(label_image)) + measurements_start_x
    height = label_image.shape[-2]
    if len(label_image.shape) == 3:
        depth = label_image.shape[0]
    else:
        depth = 1
    num_dimensions = len(label_image.shape)

    # results go here
    region_props = {}

    # intermediate results are stored in this image which is a high as the original image,
    # as wide as number of labels and has 16 planes representing:
    # 0. sum_x: all x-coordinates summed per label (and column)
    # 1. sum_y:
    # 2. sum_z:
    # 3. sum: number of pixels per label (sum of a binary image representing the label)
    # 4. sum_intensity_x: intensity (of the intensity image) times x-coordinate summed per label
    # 5. sum_intensity_y
    # 6. sum_intensity_z
    # 7. sum_intensity: sum intensity (a.k.a. total intensity) of the label
    # 8. min_intensity
    # 9. max_intensity
    # 10. min_x: minimum x coordinate of the label (in the given column)
    # 11. max_x
    # 12. min_y
    # 13. max_y
    # 14. min_z
    # 15. max_z
    cumulative_stats_per_label_image = create([16, height, num_labels])
    # init sum-fields with zero
    set(cumulative_stats_per_label_image, 0)
    # before determining min/max, set initial values to very high and very low values
    min_value = np.finfo(np.float32).min
    max_value = np.finfo(np.float32).max
    set_plane(cumulative_stats_per_label_image, 8, max_value)
    set_plane(cumulative_stats_per_label_image, 9, min_value)
    set_plane(cumulative_stats_per_label_image, 10, max_value)
    set_plane(cumulative_stats_per_label_image, 11, min_value)
    set_plane(cumulative_stats_per_label_image, 12, max_value)
    set_plane(cumulative_stats_per_label_image, 13, min_value)
    set_plane(cumulative_stats_per_label_image, 14, max_value)
    set_plane(cumulative_stats_per_label_image, 15, min_value)

    # accumulate statistics slice-by-slice
    dimensions = [1, height, 1]
    parameters = {
        'dst': cumulative_stats_per_label_image,
        'src_label': label_image,
        'src_image': intensity_image,
        'sum_background': 0  # don't analyse background
    }
    for z in range(0, depth):
        #print('z', z)
        parameters['z'] = z

        from .._tier0 import execute
        execute(__file__, 'statistics_per_label_x.cl', 'statistics_per_label', dimensions, parameters)

    # collect slice-by-slice measurements in single planes
    sum_per_label = sum_y_projection(cumulative_stats_per_label_image)
    min_per_label = minimum_y_projection(cumulative_stats_per_label_image)
    max_per_label = maximum_y_projection(cumulative_stats_per_label_image)

    # create some temporary images
    label_statistics_image = create([1, 8, num_labels])
    result_vector = create([1, num_labels - measurements_start_x])
    sum_dim = create([1, num_labels - measurements_start_x])
    avg_dim = create([1, num_labels - measurements_start_x])

    # <param_name> = <column index>
    # --------------------
    # IDENTIFIER = 0
    region_props['label'] = np.arange(measurements_start_x, num_labels)
    region_props['original_label'] = np.arange(measurements_start_x, num_labels)

    #     BOUNDING_BOX_X = 1
    #     BOUNDING_BOX_Y = 2
    #     BOUNDING_BOX_Z = 3
    #     BOUNDING_BOX_WIDTH = 7
    #     BOUNDING_BOX_HEIGHT = 8
    #     BOUNDING_BOX_DEPTH = 9
    crop(min_per_label, result_vector, measurements_start_x, 10, 0)
    bbox_min_x = pull(result_vector)[0]
    region_props['bbox_min_x'] = bbox_min_x

    crop(min_per_label, result_vector, measurements_start_x, 12, 0)
    bbox_min_y = pull(result_vector)[0]
    region_props['bbox_min_y'] = bbox_min_y

    crop(min_per_label, result_vector, measurements_start_x, 14, 0)
    bbox_min_z = pull(result_vector)[0]
    region_props['bbox_min_z'] = bbox_min_z

    crop(max_per_label, result_vector, measurements_start_x, 11, 0)
    bbox_max_x = pull(result_vector)[0]
    region_props['bbox_max_x'] = bbox_max_x

    crop(max_per_label, result_vector, measurements_start_x, 13, 0)
    bbox_max_y = pull(result_vector)[0]
    region_props['bbox_max_y'] = bbox_max_y

    crop(max_per_label, result_vector, measurements_start_x, 15, 0)
    bbox_max_z = pull(result_vector)[0]
    region_props['bbox_max_z'] = bbox_max_z

    if len(intensity_image.shape) == 2:
        bbox = [
            bbox_min_y,
            bbox_min_x,
            bbox_max_y - bbox_min_y + 1,
            bbox_max_x - bbox_min_x + 1,
        ]
    else: # 3-dimensional image
        bbox = [
            bbox_min_z,
            bbox_min_y,
            bbox_min_x,
            bbox_max_z - bbox_min_z + 1,
            bbox_max_y - bbox_min_y + 1,
            bbox_max_x - bbox_min_x + 1,
        ]
    region_props['bbox_width'] = bbox_max_x - bbox_min_x + 1
    region_props['bbox_height'] = bbox_max_y - bbox_min_y + 1
    region_props['bbox_depth'] = bbox_max_z - bbox_min_z + 1

    #     MINIMUM_INTENSITY = 10
    #     MAXIMUM_INTENSITY = 11
    crop(min_per_label, result_vector, measurements_start_x, 8, 0)
    region_props['min_intensity'] = pull(result_vector)[0]
    crop(max_per_label, result_vector, measurements_start_x, 9, 0)
    region_props['max_intensity'] = pull(result_vector)[0]

    #     MEAN_INTENSITY = 12
    #     SUM_INTENSITY = 13
    #     PIXEL_COUNT = 15
    crop(sum_per_label, result_vector, measurements_start_x, 7, 0)
    region_props['sum_intensity'] = pull(result_vector)[0]

    crop(sum_per_label, sum_dim, measurements_start_x, 3, 0)
    region_props['area'] = pull(sum_dim)[0]
    paste(sum_dim, label_statistics_image, measurements_start_x, 7, 0)

    divide_images(result_vector, sum_dim, avg_dim)
    region_props['mean_intensity'] = pull(avg_dim)[0]
    paste(avg_dim, label_statistics_image, measurements_start_x, 6, 0)

    #     SUM_INTENSITY_TIMES_X = 16
    #     SUM_INTENSITY_TIMES_Y = 17
    #     SUM_INTENSITY_TIMES_Z = 18
    #     MASS_CENTER_X = 19
    #     MASS_CENTER_Y = 20
    #     MASS_CENTER_Z = 21
    dim_names = ['x', 'y', 'z']
    crop(sum_per_label, result_vector, measurements_start_x, 4 + 3, 0)
    for dim in range(0, 3):
        crop(sum_per_label, sum_dim, measurements_start_x, 4 + dim, 0)
        region_props['sum_intensity_times_' + dim_names[dim]] = pull(sum_dim)[0]
        divide_images(sum_dim, result_vector, avg_dim)
        region_props['mass_center_' + dim_names[dim]] = pull(avg_dim)[0]
        paste(avg_dim, label_statistics_image, measurements_start_x, 3 + dim, 0)

    #     SUM_X = 22
    #     SUM_Y = 23
    #     SUM_Z = 24
    #     CENTROID_X = 25
    #     CENTROID_Y = 26
    #     CENTROID_Z = 27
    crop(sum_per_label, result_vector, measurements_start_x, 3, 0)
    for dim in range(0, 3):
        crop(sum_per_label, sum_dim, measurements_start_x, dim, 0)
        region_props['sum_' + dim_names[dim]] = pull(sum_dim)[0]
        divide_images(sum_dim, result_vector, avg_dim)
        region_props['centroid_' + dim_names[dim]] = pull(avg_dim)[0]
        paste(avg_dim, label_statistics_image, measurements_start_x, dim, 0)

    # ================================================================
    # second part: determine parmeters which depend on other parameters, such as standard_deviation

    label_statistics_stack = create([6, height, num_labels])
    set(label_statistics_stack, 0)

    # accumulate statistics slice-by-slice
    parameters = {
        'dst': label_statistics_stack,
        'src_statistics': label_statistics_image,
        'src_label': label_image,
        'src_image': intensity_image,
        'sum_background': 0 # don't analyse background
    }
    for z in range(0, depth):
        # print('z', z)
        parameters['z'] = z

        from .._tier0 import execute
        execute(__file__, 'standard_deviation_per_label_x.cl', 'standard_deviation_per_label', dimensions, parameters)

    sum_statistics = sum_y_projection(label_statistics_stack)
    max_statistics = maximum_y_projection(label_statistics_stack)

    # area
    crop(sum_per_label, result_vector, measurements_start_x, 3, 0)

    # distance to centroid
    crop(sum_statistics, sum_dim, measurements_start_x, 0, 0)
    region_props['sum_distance_to_centroid'] = pull(sum_dim)[0]
    divide_images(sum_dim, result_vector, avg_dim)
    region_props['mean_distance_to_centroid'] = pull(avg_dim)[0]

    # distance to center of mass
    crop(sum_statistics, sum_dim, measurements_start_x, 1, 0)
    region_props['sum_distance_to_mass_center'] = pull(sum_dim)[0]
    divide_images(sum_dim, result_vector, avg_dim)
    region_props['mean_distance_to_mass_center'] = pull(avg_dim)[0]

    # standard deviation intensity
    crop(sum_statistics, sum_dim, measurements_start_x, 2, 0)
    power(sum_dim, result_vector, 0.5)
    region_props['standard_deviation_intensity'] = pull(result_vector)[0]

    crop(max_statistics, result_vector, measurements_start_x, 4, 0)
    region_props['max_distance_to_centroid'] = pull(result_vector)[0]
    crop(max_statistics, result_vector, measurements_start_x, 5, 0)
    region_props['max_distance_to_mass_center'] = pull(result_vector)[0]

    region_props['mean_max_distance_to_centroid_ratio'] = region_props['max_distance_to_centroid'] / region_props[
        'mean_distance_to_centroid']
    region_props['mean_max_distance_to_mass_center_ratio'] = region_props['max_distance_to_mass_center'] / region_props[
        'mean_distance_to_mass_center']

    return region_props
