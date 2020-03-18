import numpy as np
from clesperanto import push
from clesperanto import create
from clesperanto import addImageAndScalar

# push an array to the GPU
flip = push(np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]))

# print input
print(flip)

# create memory for the output
flop = create((10,))

# add a constant to all pixels
addImageAndScalar(flip, flop, 100.0)

# print result
print(flop)
