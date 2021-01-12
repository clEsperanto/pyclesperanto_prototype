from .._tier2 import maximum_of_all_pixels
from .._tier0 import create_none
from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(output_creator=create_none)
def centroids_of_labels(labels:Image, pointlist_destination :Image = None, include_background :bool = False):
    """Determines the centroids of all labels in a label image or image stack. 
    
    It writes the resulting  coordinates in a pointlist image. Depending on 
    the dimensionality d of the labelmap and the number  of labels n, the 
    pointlist image will have n*d pixels. 
    
    Parameters
    ----------
    labels : Image
        input label image
    pointlist_destination : Image
        target image of size d*n for a d-dimensional label image with n labels. In case the background should be
        determined as well, this image needs to be one pixel wider
    include_background : bool
        measure the centroid of the background as well
    regionprops : list of skimage.measure._regionprops.RegionProperties
        in case regionprops of the label image were determined earlier, one can hand them over to prevent re-generation
    use_gpu : bool
        in case the centroid determination can't handle a large number of labels, one can turn this flag of and let
        the centroid determination be done by scikit-image regionprops
    
    Returns
    -------
    pointlist_destination
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_centroidsOfLabels
    """
    from .._tier2 import maximum_of_all_pixels
    num_labels = int(maximum_of_all_pixels(labels)) + 1

    width = labels.shape[-1]
    height = labels.shape[-2]
    if len(labels.shape) == 3:
        depth = labels.shape[0]
    else:
        depth = 1

    #print("------------------------------------------------")
    #print("w/h/d/l", width, height, depth, num_labels)

    from .._tier0 import create
    from .._tier1 import set
    from .._tier1 import sum_x_projection
    from .._tier1 import sum_y_projection
    from .._tier1 import sum_z_projection
    from .._tier1 import crop
    from .._tier1 import paste
    from .._tier1 import divide_images

    sum_per_label_image = create([4, height, num_labels])
    set(sum_per_label_image, 0)

    dimensions = [1, height, 1]

    parameters = {
        'dst': sum_per_label_image,
        'src': labels,
        'sum_background': 1 if include_background else 0
    }

    for z in range(0, depth):
        #print('z', z)
        parameters['z'] = z

        from .._tier0 import execute
        execute(__file__, 'sum_per_label_x.cl', 'sum_per_label', dimensions, parameters)

    sum_per_label = sum_y_projection(sum_per_label_image)

    #print(sum_per_label)

    num_dimensions = len(labels.shape)

    if pointlist_destination is None:
        if include_background:
            pointlist_destination = create([num_dimensions, num_labels])
        else:
            pointlist_destination = create([num_dimensions, num_labels - 1])

    if include_background:
        target_x = 0
    else:
        target_x = 1

    sum = create([1, num_labels])
    crop(sum_per_label, sum, target_x, 3, 0)

    sum_dim = create([1, num_labels])
    avg_dim = create([1, num_labels])



    for dim in range(0, num_dimensions):

        crop(sum_per_label, sum_dim, target_x, dim, 0)
        divide_images(sum_dim, sum, avg_dim)
        paste(avg_dim, pointlist_destination, 0, dim, 0)

    #print(pointlist_destination)
    return pointlist_destination




