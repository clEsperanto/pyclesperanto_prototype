from skimage.measure._regionprops import RegionProperties
import numpy as np
from .._tier0 import push

def push_regionprops(props : RegionProperties, first_row_index : int = 0):
    """

    IDENTIFIER(0),
    BOUNDING_BOX_X(1),
    BOUNDING_BOX_Y(2),
    BOUNDING_BOX_Z(3),
    BOUNDING_BOX_END_X(4),
    BOUNDING_BOX_END_Y(5),
    BOUNDING_BOX_END_Z(6),
    BOUNDING_BOX_WIDTH(7),
    BOUNDING_BOX_HEIGHT(8),
    BOUNDING_BOX_DEPTH(9),
    MINIMUM_INTENSITY(10),
    MAXIMUM_INTENSITY(11),
    MEAN_INTENSITY(12),
    SUM_INTENSITY(13),
    STANDARD_DEVIATION_INTENSITY(14),
    PIXEL_COUNT(15),
    SUM_INTENSITY_TIMES_X(16),
    SUM_INTENSITY_TIMES_Y(17),
    SUM_INTENSITY_TIMES_Z(18),
    MASS_CENTER_X(19),
    MASS_CENTER_Y(20),
    MASS_CENTER_Z(21),
    SUM_X(22),
    SUM_Y(23),
    SUM_Z(24),
    CENTROID_X(25),
    CENTROID_Y(26),
    CENTROID_Z(27),
    SUM_DISTANCE_TO_MASS_CENTER(28),
    MEAN_DISTANCE_TO_MASS_CENTER(29),
    MAX_DISTANCE_TO_MASS_CENTER(30),
    MAX_MEAN_DISTANCE_TO_MASS_CENTER_RATIO(31),
    SUM_DISTANCE_TO_CENTROID(32),
    MEAN_DISTANCE_TO_CENTROID(33),
    MAX_DISTANCE_TO_CENTROID(34),
    MAX_MEAN_DISTANCE_TO_CENTROID_RATIO(35);

    Parameters
    ----------
    props

    Returns
    -------

    """

    num_columns = 36
    num_rows = len(props)

    matrix = np.zeros([num_rows, num_columns])

    for i, label_props in enumerate(props):
        # label id
        matrix[i][0] = i + first_row_index

        # bounding box
        bbox = label_props.bbox
        if len(bbox) == 4:
            matrix[i][1] = bbox[1]
            matrix[i][2] = bbox[0]
            matrix[i][3] = 0

            matrix[i][4] = bbox[3]
            matrix[i][5] = bbox[2]
            matrix[i][6] = 0
        else:
            matrix[i][1] = bbox[2]
            matrix[i][2] = bbox[1]
            matrix[i][3] = bbox[0]

            matrix[i][4] = bbox[5]
            matrix[i][5] = bbox[4]
            matrix[i][6] = bbox[3]

        matrix[i][7] = matrix[i][4] - matrix[i][1] + 1
        matrix[i][8] = matrix[i][5] - matrix[i][2] + 1
        matrix[i][9] = matrix[i][6] - matrix[i][3] + 1

        # intensity measurements
        matrix[i][10] = label_props.min_intensity
        matrix[i][11] = label_props.max_intensity
        matrix[i][12] = label_props.mean_intensity
        # sum intensity
        matrix[i][13] = label_props.mean_intensity * label_props.area
        # stddev intensity
        matrix[i][14] = -1 # not implemented

        # area
        matrix[i][15] = label_props.area

        # center of mass
        if (len(label_props.weighted_centroid) == 3):
            matrix[i][19] = label_props.weighted_centroid[2]
            matrix[i][20] = label_props.weighted_centroid[1]
            matrix[i][21] = label_props.weighted_centroid[0]
        else:
            matrix[i][19] = label_props.weighted_centroid[1]
            matrix[i][20] = label_props.weighted_centroid[0]
            matrix[i][21] = 0

        # centroid
        if (len(label_props.centroid) == 3):
            matrix[i][25] = label_props.centroid[2]
            matrix[i][26] = label_props.centroid[1]
            matrix[i][27] = label_props.centroid[0]
        else:
            matrix[i][25] = label_props.centroid[1]
            matrix[i][26] = label_props.centroid[0]
            matrix[i][27] = 0

    return push(matrix)