from enum import Enum

class STATISTICS_ENTRY(Enum):
    """This enum allows to access a specific column in a measurement table corresponding to a specific measurement.
    It is the python counter part for the Java version in CLIJ2:
    https://github.com/clij/clij2/blob/master/src/main/java/net/haesleinhuepf/clij2/plugins/StatisticsOfLabelledPixels.java#L30
    
    """
    IDENTIFIER = 0
    BOUNDING_BOX_X = 1
    BOUNDING_BOX_Y = 2
    BOUNDING_BOX_Z = 3
    BOUNDING_BOX_END_X = 4
    BOUNDING_BOX_END_Y = 5
    BOUNDING_BOX_END_Z = 6
    BOUNDING_BOX_WIDTH = 7
    BOUNDING_BOX_HEIGHT = 8
    BOUNDING_BOX_DEPTH = 9
    MINIMUM_INTENSITY = 10
    MAXIMUM_INTENSITY = 11
    MEAN_INTENSITY = 12
    SUM_INTENSITY = 13
    STANDARD_DEVIATION_INTENSITY = 14
    PIXEL_COUNT = 15
    SUM_INTENSITY_TIMES_X = 16
    SUM_INTENSITY_TIMES_Y = 17
    SUM_INTENSITY_TIMES_Z = 18
    MASS_CENTER_X = 19
    MASS_CENTER_Y = 20
    MASS_CENTER_Z = 21
    SUM_X = 22
    SUM_Y = 23
    SUM_Z = 24
    CENTROID_X = 25
    CENTROID_Y = 26
    CENTROID_Z = 27
    SUM_DISTANCE_TO_MASS_CENTER = 28
    MEAN_DISTANCE_TO_MASS_CENTER = 29
    MAX_DISTANCE_TO_MASS_CENTER = 30
    MAX_MEAN_DISTANCE_TO_MASS_CENTER_RATIO = 31
    SUM_DISTANCE_TO_CENTROID = 32
    MEAN_DISTANCE_TO_CENTROID = 33
    MAX_DISTANCE_TO_CENTROID = 34
    MAX_MEAN_DISTANCE_TO_CENTROID_RATIO = 35

    NUMBER_OF_ENTRIES = 36
