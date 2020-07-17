import numpy as np
from .._tier0 import pull
from .._tier0 import push
from .._tier0 import create
from .._tier1 import replace_intensities
from .._tier1 import set
from .._tier2 import flag_existing_intensities
from .._tier2 import maximum_of_all_pixels
from .._tier2 import sum_reduction_x
from .._tier2 import block_enumerate


def close_index_gaps_in_label_map(input, output, blocksize = 4096):
    max_label = maximum_of_all_pixels(input)

    flagged_indices = create([int(max_label) + 1, 1])
    set(flagged_indices, 0)
    flag_existing_intensities(input, flagged_indices)

    # sum existing labels per blocks
    block_sums = create([int((int(max_label) + 1) / blocksize) + 1, 1])
    sum_reduction_x(flagged_indices, block_sums, blocksize)

    # distribute new numbers
    new_indices = create([int(max_label) + 1, 1])
    block_enumerate(flagged_indices, block_sums, new_indices, blocksize)

    replace_intensities(input, new_indices, output)

    return output