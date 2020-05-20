import numpy as np

def pull(oclarray):
    temp = oclarray.get();

    if (len(temp.shape) == 2):
        temp = np.swapaxes(temp, 0, 1)
    else:
        temp = np.swapaxes(temp, 0, 2)

    return temp


def pull_zyx(oclarray):
    temp = oclarray.get();
    return temp