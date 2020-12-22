from pyclesperanto_prototype._tier0 import Image
from pyclesperanto_prototype._tier0 import create_like
from pyclesperanto_prototype._tier1 import binary_and
from pyclesperanto_prototype._tier1 import binary_or
from pyclesperanto_prototype._tier2 import sum_of_all_pixels

def jaccard_index(source1 : Image, source2 : Image):
    """Determines the overlap of two binary images using the Jaccard index. 
    
    A value of 0 suggests no overlap, 1 means perfect overlap.
    The resulting Jaccard index is saved to the results table in the 
    'Jaccard_Index' column.
    Note that the Sorensen-Dice coefficient can be calculated from the Jaccard 
    index j using this formula:
    <pre>s = f(j) = 2 j / (j + 1)</pre> 
    
    Parameters
    ----------
    source1 : Image
    source2 : Image
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.jaccard_index(source1, source2)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_jaccardIndex
    """

    intersection = create_like(source1)
    binary_and(source1, source2, intersection)

    union = create_like(source1)
    binary_or(source1, source2, union)

    return sum_of_all_pixels(intersection) / sum_of_all_pixels(union)