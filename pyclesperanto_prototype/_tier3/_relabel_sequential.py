from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import create, create_labels_like
from .._tier1 import replace_intensities
from .._tier1 import set
from .._tier1 import set_column
from .._tier2 import flag_existing_intensities
from .._tier2 import maximum_of_all_pixels
from .._tier2 import sum_reduction_x
from .._tier2 import block_enumerate

@plugin_function(output_creator=create_labels_like, categories=['label processing', 'in assistant'])
def relabel_sequential(input : Image, output : Image = None, blocksize : int = 4096):
    """Analyses a label map and if there are gaps in the indexing (e.g. label 
    5 is not present) all 
    subsequent labels will be relabelled. 
    
    Thus, afterwards number of labels and maximum label index are equal.
    This operation is mostly performed on the CPU. 
    
    Parameters
    ----------
    labeling_input : Image
    labeling_destination : Image
    blocksize : int, optional
        Renumbering is done in blocks for performance reasons.
        Change the blocksize to adapt to your data and hardware
    
    Returns
    -------
    labeling_destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.relabel_sequential(labeling_input, labeling_destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_closeIndexGapsInLabelMap
    """
    max_label = maximum_of_all_pixels(input)

    flagged_indices = create([1, int(max_label) + 1])
    set(flagged_indices, 0)
    flag_existing_intensities(input, flagged_indices)
    set_column(flagged_indices, 0, 0) # background shouldn't be relabelled

    # sum existing labels per blocks
    block_sums = create([1, int((int(max_label) + 1) / blocksize) + 1])
    sum_reduction_x(flagged_indices, block_sums, blocksize)

    # distribute new numbers
    new_indices = create([1, int(max_label) + 1])
    block_enumerate(flagged_indices, block_sums, new_indices, blocksize)

    replace_intensities(input, new_indices, output)

    return output