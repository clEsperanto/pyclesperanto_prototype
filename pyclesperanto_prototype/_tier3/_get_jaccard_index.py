from pyclesperanto_prototype._tier0 import Image
from pyclesperanto_prototype._tier0 import create_like
from pyclesperanto_prototype._tier1 import binary_and
from pyclesperanto_prototype._tier1 import binary_or
from pyclesperanto_prototype._tier2 import sum_of_all_pixels

def get_jaccard_index(src1 : Image, src2 : Image):
    """

    :param input:
    :return:
    """

    intersection = create_like(src1)
    binary_and(src1, src2, intersection)

    union = create_like(src1)
    binary_or(src1, src2, union)

    return sum_of_all_pixels(intersection) / sum_of_all_pixels(union)