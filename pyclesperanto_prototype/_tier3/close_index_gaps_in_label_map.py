import numpy as np
from .._tier0 import pull
from .._tier0 import push
from .._tier1 import replace_intensities
from .._tier2 import maximum_of_all_pixels

def close_index_gaps_in_label_map(input, output):
    max_label = maximum_of_all_pixels(input)
    print(max_label)

    new_indices = np.zeros([int(max_label) + 1, 1])

    arr = pull(input)

    count = 0
    for x in np.nditer(arr):
        key = int(x)
        if (key > 0 and new_indices[key][0] == 0):
            count += 1
            new_indices[key][0] = count

    new_indices_gpu = push(new_indices)
    replace_intensities(input, new_indices_gpu, output)

    return output