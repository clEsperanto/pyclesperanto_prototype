import numpy as np
def prepare(arr):
    return np.require(arr, None, "C")
