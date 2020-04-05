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




# matrix multiplication
from time import time
from clesperanto import multiplyMatrix

a_np = np.random.randn(1024 * 1024).astype(np.float32)
b_np = np.random.randn(1024 * 1024).astype(np.float32)
a_np.shape = (1024, 1024)
b_np.shape = (1024, 1024)

# push data to GPU
start = time()
gpu_a = push(a_np)
gpu_b = push(b_np)

# allocate memory for result on GPU
gpu_c = create((1024, 1024))
print('push+alloc time', (time() - start) * 1000)

# multiply matrix onGPU
start = time()
multiplyMatrix(gpu_a, gpu_b, gpu_c)
print('cle1 time', (time() - start) * 1000)

start = time()
multiplyMatrix(gpu_a, gpu_b, gpu_c)
print('cle2 time', (time() - start) * 1000)

# multiply matrix on CPU
start = time()
np.dot(a_np, b_np)
print('np1 time', (time() - start) * 1000)

start = time()
np.dot(a_np, b_np)
print('np2 time', (time() - start) * 1000)

