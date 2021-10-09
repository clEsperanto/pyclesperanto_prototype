from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import execute, create, create_labels_like, create_like, create_none
from .._tier1 import set, copy, add_image_and_scalar

@plugin_function(categories=['label processing', 'in assistant'], output_creator=create_none)
def watershed(image:Image, markers:Image, mask:Image=None,output:Image = None):
    """
    Watershed algorithm takes seed labels (markers) and enlarges
    their areas according to the landscape / altitude map provided as image.

    The API of this algorithm is different from the implementation in CLIJ2 [1]

    The results may be similar, but not identical to the results by the implementation in scikit-image[2].

    Parameters
    ----------
    image : Image
        landscape or altitude image
    markers : Image
        seeds
    mask : Image, optional
        limit label enlarging to this region
    output : Image, optional
        label image with resulting basins

    Returns
    -------
    output

    See Also
    --------
    [1] https://clij.github.io/clij2-docs/reference_watershed
    [2] https://scikit-image.org/docs/dev/api/skimage.segmentation.html#skimage.segmentation.watershed

    """
    flag = create([1, 1, 1])
    set(flag, 1)

    if mask is None:
        mask = create_like(image)
        set(mask, 1)

    if output is None:
        output = create_labels_like(markers)
    set(output, 0)

    temp = image * -1 # negate to make API similar to skimage
    distance_map1 = add_image_and_scalar(temp, scalar=-temp.min()) # make sure it's positive
    print(distance_map1.min())
    print(distance_map1.max())

    distance_map2 = create_like(image)
    set(distance_map2, 0)

    label_map_1 = create_labels_like(markers)
    copy(markers, label_map_1)
    label_map_2 = create_labels_like(markers)
    set(label_map_2, 0)

    iteration = 0
    # enlarge labels according to image gradient iteratively
    while(flag[0,0,0] > 0):
        set(flag, 0)
        if iteration % 2 == 0:
            _dilate_labels_until_no_change(distance_map1, label_map_1, flag, distance_map2, label_map_2, mask, temp)
        else:
            _dilate_labels_until_no_change(distance_map2, label_map_2, flag, distance_map1, label_map_1, mask, temp)

        if iteration % 10 == 0:
            from .._tier9 import imshow
            imshow(distance_map1)

        iteration += 1

    if iteration % 2 == 0:
        copy(label_map_1, output)
    else:
        copy(label_map_2, output)

    return output

def _dilate_labels_until_no_change(distanceMapIn:Image, labelMapIn:Image, flag:Image, distanceMapOut:Image, labelMapOut:Image, mask:Image, original_distance_map:Image):
    parameters = {
    "src_labelmap": labelMapIn,
    "src_distancemap": distanceMapIn,
    "dst_labelmap": labelMapOut,
    "dst_distancemap": distanceMapOut,
    "flag_dst": flag,
    "src_mask": mask,
    "src_original_distance_map": original_distance_map}

    execute(__file__, "watershed_local_maximum_" + str(len(distanceMapIn.shape)) + "d_x.cl", "watershed_local_maximum_" + str(len(distanceMapIn.shape)) + "d", distanceMapIn.shape, parameters)
