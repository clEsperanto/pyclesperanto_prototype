from warnings import warn

from skimage.measure._regionprops import RegionProperties
import numpy as np
from .._tier0 import push

def push_regionprops(props : RegionProperties, first_row_index : int = 0):
    """
    
    See Also
    --------
    STATISTICS_ENTRY

    Parameters
    ----------
    props

    Returns
    -------

    """
    from ._statistics_entry import STATISTICS_ENTRY

    num_columns = 36
    if hasattr(props[0], 'original_label'):
        labels = [r.original_label for r in props]
    else:
        labels = [r.label for r in props]
    num_rows = np.max(labels) + 1 - first_row_index

    matrix = np.zeros([num_rows, num_columns])

    for j, label_props in enumerate(props):
        if hasattr(label_props, 'original_label'):
            i = label_props.original_label
        else:
            i = label_props.label
        if i >= first_row_index:
            i = i - first_row_index

            # label id
            matrix[i][STATISTICS_ENTRY.IDENTIFIER.value] = i + first_row_index

            # bounding box
            bbox = label_props.bbox
            if len(bbox) == 4:
                matrix[i][STATISTICS_ENTRY.BOUNDING_BOX_X.value] = bbox[1]
                matrix[i][STATISTICS_ENTRY.BOUNDING_BOX_Y.value] = bbox[0]
                matrix[i][STATISTICS_ENTRY.BOUNDING_BOX_Z.value] = 0

                matrix[i][STATISTICS_ENTRY.BOUNDING_BOX_END_X.value] = bbox[3] - 1
                matrix[i][STATISTICS_ENTRY.BOUNDING_BOX_END_Y.value] = bbox[2] - 1
                matrix[i][STATISTICS_ENTRY.BOUNDING_BOX_END_Z.value] = 0
            else:
                matrix[i][STATISTICS_ENTRY.BOUNDING_BOX_X.value] = bbox[2]
                matrix[i][STATISTICS_ENTRY.BOUNDING_BOX_Y.value] = bbox[1]
                matrix[i][STATISTICS_ENTRY.BOUNDING_BOX_Z.value] = bbox[0]

                matrix[i][STATISTICS_ENTRY.BOUNDING_BOX_END_X.value] = bbox[5] - 1
                matrix[i][STATISTICS_ENTRY.BOUNDING_BOX_END_Y.value] = bbox[4] - 1
                matrix[i][STATISTICS_ENTRY.BOUNDING_BOX_END_Z.value] = bbox[3] - 1

            matrix[i][STATISTICS_ENTRY.BOUNDING_BOX_WIDTH.value] = matrix[i][STATISTICS_ENTRY.BOUNDING_BOX_END_X.value] - matrix[i][STATISTICS_ENTRY.BOUNDING_BOX_X.value] + 1
            matrix[i][STATISTICS_ENTRY.BOUNDING_BOX_HEIGHT.value] = matrix[i][STATISTICS_ENTRY.BOUNDING_BOX_END_Y.value] - matrix[i][STATISTICS_ENTRY.BOUNDING_BOX_Y.value] + 1
            matrix[i][STATISTICS_ENTRY.BOUNDING_BOX_DEPTH.value] = matrix[i][STATISTICS_ENTRY.BOUNDING_BOX_END_Z.value] - matrix[i][STATISTICS_ENTRY.BOUNDING_BOX_Z.value] + 1

            # intensity measurements
            matrix[i][STATISTICS_ENTRY.MINIMUM_INTENSITY.value] = label_props.min_intensity
            matrix[i][STATISTICS_ENTRY.MAXIMUM_INTENSITY.value] = label_props.max_intensity
            matrix[i][STATISTICS_ENTRY.MEAN_INTENSITY.value] = label_props.mean_intensity
            # sum intensity
            matrix[i][STATISTICS_ENTRY.SUM_INTENSITY.value] = label_props.mean_intensity * label_props.area
            # stddev intensity
            if hasattr(label_props, 'standard_deviation_intensity'):
                matrix[i][STATISTICS_ENTRY.STANDARD_DEVIATION_INTENSITY.value] = label_props.standard_deviation_intensity
            else:
                warn("regionprops didn't contains stanard_deviation_intensity. Consider using cle.statistics_of_labelled_pixels to determine the standard deviation. ")
                matrix[i][STATISTICS_ENTRY.STANDARD_DEVIATION_INTENSITY.value] = -1

            # area
            matrix[i][15] = label_props.area

            # center of mass
            if (len(label_props.weighted_centroid) == 3):
                matrix[i][STATISTICS_ENTRY.MASS_CENTER_X.value] = label_props.weighted_centroid[2]
                matrix[i][STATISTICS_ENTRY.MASS_CENTER_Y.value] = label_props.weighted_centroid[1]
                matrix[i][STATISTICS_ENTRY.MASS_CENTER_Z.value] = label_props.weighted_centroid[0]
            else:
                matrix[i][STATISTICS_ENTRY.MASS_CENTER_X.value] = label_props.weighted_centroid[1]
                matrix[i][STATISTICS_ENTRY.MASS_CENTER_Y.value] = label_props.weighted_centroid[0]
                matrix[i][STATISTICS_ENTRY.MASS_CENTER_Z.value] = 0

            # centroid
            if (len(label_props.centroid) == 3):
                matrix[i][STATISTICS_ENTRY.CENTROID_X.value] = label_props.centroid[2]
                matrix[i][STATISTICS_ENTRY.CENTROID_Y.value] = label_props.centroid[1]
                matrix[i][STATISTICS_ENTRY.CENTROID_Z.value] = label_props.centroid[0]
            else:
                matrix[i][STATISTICS_ENTRY.CENTROID_X.value] = label_props.centroid[1]
                matrix[i][STATISTICS_ENTRY.CENTROID_Y.value] = label_props.centroid[0]
                matrix[i][STATISTICS_ENTRY.CENTROID_Z.value] = 0

            # moments / shape descriptors
            if hasattr(label_props, 'sum_distance_to_mass_center'):
                matrix[i][STATISTICS_ENTRY.SUM_DISTANCE_TO_MASS_CENTER.value] = label_props['sum_distance_to_mass_center']
            if hasattr(label_props, 'mean_distance_to_mass_center'):
                matrix[i][STATISTICS_ENTRY.MEAN_DISTANCE_TO_MASS_CENTER.value] = label_props['mean_distance_to_mass_center']
            if hasattr(label_props, 'max_distance_to_mass_center'):
                matrix[i][STATISTICS_ENTRY.MAX_DISTANCE_TO_MASS_CENTER.value] = label_props['max_distance_to_mass_center']
            if hasattr(label_props, 'mean_max_distance_to_mass_center_ratio'):
                matrix[i][STATISTICS_ENTRY.MAX_MEAN_DISTANCE_TO_MASS_CENTER_RATIO.value] = label_props['mean_max_distance_to_mass_center_ratio']

            if hasattr(label_props, 'sum_distance_to_centroid'):
                matrix[i][STATISTICS_ENTRY.SUM_DISTANCE_TO_CENTROID.value] = label_props['sum_distance_to_centroid']
            if hasattr(label_props, 'mean_distance_to_centroid'):
                matrix[i][STATISTICS_ENTRY.MEAN_DISTANCE_TO_CENTROID.value] = label_props['mean_distance_to_centroid']
            if hasattr(label_props, 'max_distance_to_centroid'):
                matrix[i][STATISTICS_ENTRY.MAX_DISTANCE_TO_CENTROID.value] = label_props['max_distance_to_centroid']
            if hasattr(label_props, 'mean_max_distance_to_centroid_ratio'):
                matrix[i][STATISTICS_ENTRY.MAX_MEAN_DISTANCE_TO_CENTROID_RATIO.value] = label_props['mean_max_distance_to_centroid_ratio']

    return push(matrix)