import numpy as np
import clesperanto as cle

# push an array to the GPU
flip = cle.push(np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]))

# print input
print(flip)

# create memory for the output
flop = cle.create((10,))

# add a constant to all pixels
cle.add_image_and_scalar(flip, flop, 100.0)

# print result
print(flop)




# matrix multiplication
from time import time

a_np = np.random.randn(1024 * 1024).astype(np.float32)
b_np = np.random.randn(1024 * 1024).astype(np.float32)
a_np.shape = (1024, 1024)
b_np.shape = (1024, 1024)

# push data to GPU
start = time()
gpu_a = cle.push(a_np)
gpu_b = cle.push(b_np)

# allocate memory for result on GPU
gpu_c = cle.create((1024, 1024))
print('push+alloc time', (time() - start) * 1000)

# multiply matrix onGPU
start = time()
cle.multiply_matrix(gpu_a, gpu_b, gpu_c)
print('cle1 time', (time() - start) * 1000)

start = time()
cle.multiply_matrix(gpu_a, gpu_b, gpu_c)
print('cle2 time', (time() - start) * 1000)

# multiply matrix on CPU
start = time()
np.dot(a_np, b_np)
print('np1 time', (time() - start) * 1000)

start = time()
np.dot(a_np, b_np)
print('np2 time', (time() - start) * 1000)

