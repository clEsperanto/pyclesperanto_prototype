from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import execute, create, create_labels_like, create_like
from .._tier1 import set, copy

@plugin_function(categories=['label processing', 'in assistant'])
def watershed(image:Image, markers:Image, mask:Image,output:Image = None):
    flag = create([1, 1, 1])
    set(flag, 1)
    set(output, 0)

    distance_map1 = create_like(image)
    copy(image, distance_map1)
    distance_map2 = create_like(image)
    set(distance_map2, 0)

    label_map_1 = create_labels_like(markers)
    copy(markers, label_map_1)
    label_map_2 = create_labels_like(markers)
    set(label_map_2, 0)

    print("hello world")

    iteration = 0
    while(flag[0,0,0] > 0):
        set(flag, 0)
        if iteration % 2 == 0:
            _dilate_labels_until_no_change(distance_map1, label_map_1, flag, distance_map2, label_map_2, mask)
        else:
            _dilate_labels_until_no_change(distance_map2, label_map_2, flag, distance_map1, label_map_1, mask)

        iteration += 1

        if iteration > 10:
            break

    if iteration % 2 == 0:
        copy(label_map_1, output)
    else:
        copy(label_map_2, output)

    return output

def _dilate_labels_until_no_change(distanceMapIn:Image, labelMapIn:Image, flag:Image, distanceMapOut:Image, labelMapOut:Image, mask:Image):
    parameters = {
    "src_labelmap": labelMapIn,
    "src_distancemap": distanceMapIn,
    "dst_labelmap": labelMapOut,
    "dst_distancemap": distanceMapOut,
    "flag_dst": flag,
    "mask": mask}

    execute(__file__, "watershed_local_maximum_" + str(len(distanceMapIn.shape)) + "d_x.cl", "watershed_local_maximum_" + str(len(distanceMapIn.shape)) + "d", distanceMapIn.shape, parameters)
