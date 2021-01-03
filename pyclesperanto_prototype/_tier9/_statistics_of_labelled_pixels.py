from skimage.measure import regionprops

from .._tier0 import Image
from .._tier0 import create_none
from .._tier0 import plugin_function

@plugin_function(output_creator=create_none)
def statistics_of_labelled_pixels(input : Image = None, labelmap : Image = None, measure_shape : bool = True, extra_properties = [], use_gpu : bool = False):
    """Determines bounding box, area (in pixels/voxels), min, max, mean and standard deviation
    intensity of labelled objects in a label map and corresponding pixels in the
    original image. 
    
    Instead of a label map, you can also use a binary image as a binary image is a 
    label map with just one label.
    
    This method is executed on the CPU and not on the GPU/OpenCL device. Under the hood, it uses
    skimage.measure.regionprops [2] and thus, offers the same output. Additionally, `standard_deviation_intensity` and
    is stored in the `regionprops` object.
    
    Parameters
    ----------
    input : Image
    labelmap : Image
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_statisticsOfLabelledPixels
    .. [2] https://scikit-image.org/docs/stable/api/skimage.measure.html#skimage.measure.regionprops
    """
    if use_gpu:
        return _statistics_of_labelled_pixels_gpu(input, labelmap, measure_shape)



    from .._tier0 import create_like
    from .._tier0 import pull_zyx
    from .._tier0 import push_zyx
    from .._tier1 import replace_intensities
    from .._tier3 import squared_difference

    if labelmap is None:
        raise Exception("A label image must be provided")

    label_image = pull_zyx(labelmap).astype(int)
    if input is None:
        intensity_image = label_image
        label_and_intensity_equal = True
    else:
        intensity_image = pull_zyx(input)
        label_and_intensity_equal = False

    # Inspired by: https://forum.image.sc/t/how-to-measure-standard-deviation-of-intensities-with-scikit-image-regionprops/46948/2
    import numpy as np

    # arguments must be in the specified order, matching regionprops
    def standard_deviation_intensity(region, intensities):
        return np.std(intensities[region])

    extra_properties.append(standard_deviation_intensity)

    props = regionprops(label_image, intensity_image=intensity_image, cache=True, extra_properties=extra_properties)

    if measure_shape:

        # todo: the following block could make things faster
        # determine shape descriptors by generating another image with distances of all labeled pixels to the label centroid
        # from ._centroids_of_labels import centroids_of_labels
        #centroids_pointlist = centroids_of_labels(labelmap, regionprops=props, include_background=True)
        #print(centroids_pointlist)
        centroids_pointlist = None

        from ._euclidean_distance_from_label_centroid_map import euclidean_distance_from_label_centroid_map
        distance_map = euclidean_distance_from_label_centroid_map(labelmap, centroids_pointlist)

        # todo: do the same as above with the mass_center instead of the centroid

        distance_props = regionprops(label_image, intensity_image=pull_zyx(distance_map))

        for region_prop, distance_prop in zip(props, distance_props):
            #print(str(region_prop.label) + "/" + str(distance_prop.label))

            region_prop.mean_distance_to_centroid = distance_prop.mean_intensity
            #print(str(region_prop.mean_distance_to_centroid))
            region_prop.max_distance_to_centroid = distance_prop.max_intensity
            region_prop.sum_distance_to_centroid = distance_prop.mean_intensity * region_prop.area
            region_prop.mean_max_distance_to_centroid_ratio = region_prop.max_distance_to_centroid / region_prop.mean_distance_to_centroid

            if label_and_intensity_equal:
                region_prop.mean_distance_to_mass_center = region_prop.mean_distance_to_centroid
                region_prop.max_distance_to_mass_center = region_prop.max_distance_to_centroid
                region_prop.sum_distance_to_mass_center = region_prop.sum_distance_to_centroid
                region_prop.mean_max_distance_to_mass_center_ratio = region_prop.mean_max_distance_to_centroid_ratio

    # save regionprops label
    for r in props:
        r.original_label = r.label

    return props

def _statistics_of_labelled_pixels_gpu(intensity_image : Image = None, label_image : Image = None, measure_shape : bool = True):

    if intensity_image is None and label_image is None:
        raise ValueError("Either intensity image or labels must be set")

    include_background: bool = False
    if include_background:
        target_x = 0
    else:
        target_x = 1

    from .._tier2 import maximum_of_all_pixels
    num_labels = int(maximum_of_all_pixels(label_image)) + target_x

    width = label_image.shape[-1]
    height = label_image.shape[-2]
    if len(label_image.shape) == 3:
        depth = label_image.shape[0]
    else:
        depth = 1

    # print("------------------------------------------------")
    # print("w/h/d/l", width, height, depth, num_labels)

    from .._tier0 import create
    from .._tier0 import create_like
    from .._tier1 import set
    from .._tier1 import sum_y_projection
    from .._tier1 import minimum_y_projection
    from .._tier1 import maximum_y_projection
    from .._tier1 import mean_y_projection
    from .._tier1 import crop
    from .._tier1 import paste
    from .._tier1 import divide_images
    from .._tier1 import set_ramp_x
    from .._tier1 import set_plane
    from .._tier0 import pull_zyx
    from .._tier1 import power
    import numpy as np

    region_props = {}

    sum_per_label_image = create([16, height, num_labels])
    set(sum_per_label_image, 0)

    min_value = np.finfo(np.float32).min
    max_value = np.finfo(np.float32).max

    set_plane(sum_per_label_image, 8, max_value)
    set_plane(sum_per_label_image, 9, min_value)
    set_plane(sum_per_label_image, 10, max_value)
    set_plane(sum_per_label_image, 11, min_value)
    set_plane(sum_per_label_image, 12, max_value)
    set_plane(sum_per_label_image, 13, min_value)
    set_plane(sum_per_label_image, 14, max_value)
    set_plane(sum_per_label_image, 15, min_value)

    dimensions = [1, height, 1]

    if label_image is None:
        label_image = create_like(intensity_image)
        set(label_image, 1) # all pixels belong to label 1

    if intensity_image is None:
        intensity_image = label_image

    parameters = {
        'dst': sum_per_label_image,
        'src_label': label_image,
        'src_image': intensity_image,
        'sum_background': 1 if include_background else 0
    }

    for z in range(0, depth):
        #print('z', z)
        parameters['z'] = z

        from .._tier0 import execute
        execute(__file__, 'statistics_per_label_x.cl', 'statistics_per_label', dimensions, parameters)

    sum_per_label = sum_y_projection(sum_per_label_image)
    min_per_label = minimum_y_projection(sum_per_label_image)
    max_per_label = maximum_y_projection(sum_per_label_image)

    label_statistics_image = create([1, 8, num_labels])

    # print(sum_per_label)

    num_dimensions = len(label_image.shape)

    # IDENTIFIER = 0
    region_props['label'] = range(target_x, num_labels)
    region_props['original_label'] = range(target_x, num_labels)



    result_vector = create([1, num_labels - target_x])
    sum_dim = create([1, num_labels - target_x])
    avg_dim = create([1, num_labels - target_x])

    #     BOUNDING_BOX_X = 1
    #     BOUNDING_BOX_Y = 2
    #     BOUNDING_BOX_Z = 3
    #     BOUNDING_BOX_WIDTH = 7
    #     BOUNDING_BOX_HEIGHT = 8
    #     BOUNDING_BOX_DEPTH = 9
    crop(min_per_label, result_vector, target_x, 10, 0)
    bbox_min_x = pull_zyx(result_vector)[0]
    region_props['bbox_min_x'] = bbox_min_x

    crop(min_per_label, result_vector, target_x, 12, 0)
    bbox_min_y = pull_zyx(result_vector)[0]
    region_props['bbox_min_y'] = bbox_min_y

    crop(min_per_label, result_vector, target_x, 14, 0)
    bbox_min_z = pull_zyx(result_vector)[0]
    region_props['bbox_min_z'] = bbox_min_z

    crop(max_per_label, result_vector, target_x, 11, 0)
    bbox_max_x = pull_zyx(result_vector)[0]
    region_props['bbox_max_x'] = bbox_max_x

    crop(max_per_label, result_vector, target_x, 13, 0)
    bbox_max_y = pull_zyx(result_vector)[0]
    region_props['bbox_max_y'] = bbox_max_y

    crop(max_per_label, result_vector, target_x, 15, 0)
    bbox_max_z = pull_zyx(result_vector)[0]
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

    region_props['bbox'] = bbox

    #     MINIMUM_INTENSITY = 10
    #     MAXIMUM_INTENSITY = 11
    crop(min_per_label, result_vector, target_x, 8, 0)
    region_props['min_intensity'] = pull_zyx(result_vector)[0]
    crop(max_per_label, result_vector, target_x, 9, 0)
    region_props['max_intensity'] = pull_zyx(result_vector)[0]

    #     MEAN_INTENSITY = 12
    #     SUM_INTENSITY = 13
    #     PIXEL_COUNT = 15
    crop(sum_per_label, result_vector, target_x, 7, 0)
    region_props['sum_intensity'] = pull_zyx(result_vector)[0]

    crop(sum_per_label, sum_dim, target_x, 3, 0)
    region_props['area'] = pull_zyx(sum_dim)[0]
    paste(sum_dim, label_statistics_image, target_x, 7, 0)

    divide_images(result_vector, sum_dim, avg_dim)
    region_props['mean_intensity'] = pull_zyx(avg_dim)[0]
    paste(avg_dim, label_statistics_image, target_x, 6, 0)
    #print("mean_intens", avg_dim)

    #     SUM_INTENSITY_TIMES_X = 16
    #     SUM_INTENSITY_TIMES_Y = 17
    #     SUM_INTENSITY_TIMES_Z = 18
    #     MASS_CENTER_X = 19
    #     MASS_CENTER_Y = 20
    #     MASS_CENTER_Z = 21
    mass_centers = None
    if measure_shape:###
        mass_centers = create([num_dimensions, num_labels])###
    dim_names = ['x', 'y', 'z']
    crop(sum_per_label, result_vector, target_x, 4 + 3, 0)
    for dim in range(0, 3):
        crop(sum_per_label, sum_dim, target_x, 4 + dim, 0)
        region_props['sum_intensity_times_' + dim_names[dim]] = pull_zyx(sum_dim)[0]
        divide_images(sum_dim, result_vector, avg_dim)
        region_props['mass_center_' + dim_names[dim]] = pull_zyx(avg_dim)[0]
        if mass_centers is not None: ###
            paste(avg_dim, mass_centers, target_x, dim, 0) ###
        paste(avg_dim, label_statistics_image, target_x, 3 + dim, 0)

    if len(intensity_image.shape) == 2:
        region_props['weighted_centroid'] = [
            region_props['mass_center_y'],
            region_props['mass_center_x'],
        ]
    else:
        region_props['weighted_centroid'] = [
            region_props['mass_center_z'],
            region_props['mass_center_y'],
            region_props['mass_center_x'],
        ]

    #     SUM_X = 22
    #     SUM_Y = 23
    #     SUM_Z = 24
    #     CENTROID_X = 25
    #     CENTROID_Y = 26
    #     CENTROID_Z = 27
    centroids = None
    if measure_shape:
        centroids = create([num_dimensions, num_labels])
    crop(sum_per_label, result_vector, target_x, 3, 0)
    for dim in range(0, 3):
        crop(sum_per_label, sum_dim, target_x, dim, 0)
        region_props['sum_' + dim_names[dim]] = pull_zyx(sum_dim)[0]
        divide_images(sum_dim, result_vector, avg_dim)
        region_props['centroid_' + dim_names[dim]] = pull_zyx(avg_dim)[0]
        if centroids is not None:
            paste(avg_dim, centroids, target_x, dim, 0)
        paste(avg_dim, label_statistics_image, target_x, dim, 0)

    if len(intensity_image.shape) == 2:
        region_props['centroid'] = [
            region_props['centroid_y'],
            region_props['centroid_x'],
        ]
    else:
        region_props['centroid'] = [
            region_props['centroid_z'],
            region_props['centroid_y'],
            region_props['centroid_x'],
        ]

    # ================================================================

    label_statistics_stack = create([6, height, num_labels])
    set(label_statistics_stack, 0)

    #print("stats")
    #print(label_statistics_image)

    parameters = {
        'dst': label_statistics_stack,
        'src_statistics': label_statistics_image,
        'src_label': label_image,
        'src_image': intensity_image,
        'sum_background': 1 if include_background else 0
    }

    for z in range(0, depth):
        # print('z', z)
        parameters['z'] = z

        from .._tier0 import execute
        execute(__file__, 'standard_deviation_per_label_x.cl', 'standard_deviation_per_label', dimensions, parameters)

    sum_statistics = sum_y_projection(label_statistics_stack)
    #mean_statistics = mean_y_projection(label_statistics_stack)
    max_statistics = maximum_y_projection(label_statistics_stack)

    # area
    crop(sum_per_label, result_vector, target_x, 3, 0)

    # distance to centroid
    crop(sum_statistics, sum_dim, target_x, 0, 0)
    region_props['sum_distance_to_centroid'] = pull_zyx(sum_dim)[0]
    divide_images(sum_dim, result_vector, avg_dim)
    region_props['mean_distance_to_centroid'] = pull_zyx(avg_dim)[0]

    # distance to center of mass
    crop(sum_statistics, sum_dim, target_x, 1, 0)
    region_props['sum_distance_to_mass_center'] = pull_zyx(sum_dim)[0]
    divide_images(sum_dim, result_vector, avg_dim)
    region_props['mean_distance_to_mass_center'] = pull_zyx(avg_dim)[0]

    # standard deviation intensity
    crop(sum_statistics, sum_dim, target_x, 2, 0)
    #print("sum_dim", sum_dim)
    # divide_images(sum_dim, result_vector, avg_dim)
    power(sum_dim, result_vector, 0.5)
    region_props['standard_deviation_intensity'] = pull_zyx(result_vector)[0]

    crop(max_statistics, result_vector, target_x, 4, 0)
    region_props['max_distance_to_centroid'] = pull_zyx(result_vector)[0]
    crop(max_statistics, result_vector, target_x, 5, 0)
    region_props['max_distance_to_mass_center'] = pull_zyx(result_vector)[0]

    region_props['mean_max_distance_to_centroid_ratio'] = region_props['max_distance_to_centroid'] / region_props[
        'mean_distance_to_centroid']
    region_props['mean_max_distance_to_mass_center_ratio'] = region_props['max_distance_to_mass_center'] / region_props[
        'mean_distance_to_mass_center']


    # WRITE_IMAGE(dst, POS_dst_INSTANCE(former_label, y, 0, 0), CONVERT_dst_PIXEL_TYPE(sum_distance_centroid));
    # WRITE_IMAGE(dst, POS_dst_INSTANCE(former_label, y, 1, 0), CONVERT_dst_PIXEL_TYPE(sum_distance_mass_center));
    # WRITE_IMAGE(dst, POS_dst_INSTANCE(former_label, y, 2, 0), CONVERT_dst_PIXEL_TYPE(sum_squared_difference));
    # WRITE_IMAGE(dst, POS_dst_INSTANCE(former_label, y, 3, 0), CONVERT_dst_PIXEL_TYPE(sum));
    # WRITE_IMAGE(dst, POS_dst_INSTANCE(former_label, y, 4, 0), CONVERT_dst_PIXEL_TYPE(max_distance_centroid));
    # WRITE_IMAGE(dst, POS_dst_INSTANCE(former_label, y, 5, 0), CONVERT_dst_PIXEL_TYPE(max_distance_mass_center));

    return region_props



    #         WRITE_IMAGE(dst,POS_dst_INSTANCE(former_label,y,0,0), CONVERT_dst_PIXEL_TYPE(sum_x));
    #         WRITE_IMAGE(dst,POS_dst_INSTANCE(former_label,y,1,0), CONVERT_dst_PIXEL_TYPE(sum_y));
    #         WRITE_IMAGE(dst,POS_dst_INSTANCE(former_label,y,2,0), CONVERT_dst_PIXEL_TYPE(sum_z));
    #         WRITE_IMAGE(dst,POS_dst_INSTANCE(former_label,y,3,0), CONVERT_dst_PIXEL_TYPE(sum));
    #
    #         WRITE_IMAGE(dst,POS_dst_INSTANCE(former_label,y,4,0), CONVERT_dst_PIXEL_TYPE(sum_intensity_x));
    #         WRITE_IMAGE(dst,POS_dst_INSTANCE(former_label,y,5,0), CONVERT_dst_PIXEL_TYPE(sum_intensity_y));
    #         WRITE_IMAGE(dst,POS_dst_INSTANCE(former_label,y,6,0), CONVERT_dst_PIXEL_TYPE(sum_intensity_z));
    #         WRITE_IMAGE(dst,POS_dst_INSTANCE(former_label,y,7,0), CONVERT_dst_PIXEL_TYPE(sum_intensity));
    #
    #         WRITE_IMAGE(dst,POS_dst_INSTANCE(former_label,y,8,0), CONVERT_dst_PIXEL_TYPE(min_intensity));
    #         WRITE_IMAGE(dst,POS_dst_INSTANCE(former_label,y,9,0), CONVERT_dst_PIXEL_TYPE(max_intensity));
    #
    #         WRITE_IMAGE(dst,POS_dst_INSTANCE(former_label,y,10,0), CONVERT_dst_PIXEL_TYPE(min_x));
    #         WRITE_IMAGE(dst,POS_dst_INSTANCE(former_label,y,11,0), CONVERT_dst_PIXEL_TYPE(max_x));
    #         WRITE_IMAGE(dst,POS_dst_INSTANCE(former_label,y,12,0), CONVERT_dst_PIXEL_TYPE(min_y));
    #         WRITE_IMAGE(dst,POS_dst_INSTANCE(former_label,y,13,0), CONVERT_dst_PIXEL_TYPE(max_y));
    #         WRITE_IMAGE(dst,POS_dst_INSTANCE(former_label,y,14,0), CONVERT_dst_PIXEL_TYPE(min_z));
    #         WRITE_IMAGE(dst,POS_dst_INSTANCE(former_label,y,15,0), CONVERT_dst_PIXEL_TYPE(max_z));

#     STANDARD_DEVIATION_INTENSITY = 14


#     SUM_DISTANCE_TO_MASS_CENTER = 28
#     MEAN_DISTANCE_TO_MASS_CENTER = 29
#     MAX_DISTANCE_TO_MASS_CENTER = 30
#     MAX_MEAN_DISTANCE_TO_MASS_CENTER_RATIO = 31
#     SUM_DISTANCE_TO_CENTROID = 32
#     MEAN_DISTANCE_TO_CENTROID = 33
#     MAX_DISTANCE_TO_CENTROID = 34
#     MAX_MEAN_DISTANCE_TO_CENTROID_RATIO = 35

