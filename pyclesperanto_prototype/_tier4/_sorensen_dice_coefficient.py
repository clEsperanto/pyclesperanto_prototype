from .._tier3 import jaccard_index
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def sorensen_dice_coefficient(source1 : Image, source2 : Image):
    """Determines the overlap of two binary images using the Sorensen-Dice 
    coefficent. 
    
    A value of 0 suggests no overlap, 1 means perfect overlap.
    The Sorensen-Dice coefficient is saved in the colum 'Sorensen_Dice_coefficient'.
    Note that the Sorensen-Dice coefficient s can be calculated from the Jaccard 
    index j using this formula:
    <pre>s = f(j) = 2 j / (j + 1)</pre> 
    
    Parameters
    ----------
    source1 : Image
    source2 : Image
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.sorensen_dice_coefficient(source1, source2)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_sorensenDiceCoefficient
    """

    j = jaccard_index(source1, source2)

    return 2.0 * j / (j + 1)