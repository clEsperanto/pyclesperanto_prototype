import pyclesperanto_prototype as cle
import numpy as np
import time

# config
num_iterations = 10
num_tests = 10

# initialize GPU
print("Used GPU: " + cle.get_device().name)

# generate data; 100 MB
image = np.random.random([100, 1024, 1024])
print("Image size: " + str(image.shape))

# push image to GPU memory
flip = cle.push_zyx(image)
flop = cle.create_like(flip)

for j in range(0, num_tests):
    start = time.time()

    for i in range(0, num_iterations):
        cle.maximum_sphere(flip, flop, 10, 10, 0)
        cle.minimum_sphere(flop, flip, 10, 10, 0)

    end = time.time()

    print("Flip-flop took " + str(end - start) + "s")


for j in range(0, num_tests):
    start = time.time()

    for i in range(0, num_iterations):
        flop = cle.maximum_sphere(flip, radius_x=10, radius_y=10, radius_z=0)
        flip = cle.minimum_sphere(flop, radius_x=10, radius_y=10, radius_z=0)

    end = time.time()

    print("Re-alloc took " + str(end - start) + "s")




