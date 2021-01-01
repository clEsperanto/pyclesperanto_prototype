from skimage.measure import regionprops

from .._tier0 import Image
from .._tier0 import create_none
from .._tier0 import plugin_function

@plugin_function(output_creator=create_none)
def statistics_of_labelled_pixels(input : Image = None, labelmap : Image = None, measure_shape : bool = True, extra_properties = []):
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

