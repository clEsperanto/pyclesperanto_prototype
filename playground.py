import pyclesperanto_prototype as cle
import numpy as np

print(cle.cl_info())


gpu_input = cle.push(np.asarray([
    [
        [1, 0, 1],
        [1, 0, 0],
        [0, 0, 1]
    ]
]))
gpu_output = cle.create_like(gpu_input)

gpu_reference = cle.push(np.asarray([
    [
        [1, 0, 2],
        [1, 0, 0],
        [0, 0, 3]
    ]
]))



result = cle.connected_components_labeling_box(gpu_input, gpu_output)

a = cle.pull_zyx(gpu_output)
b = cle.pull_zyx(gpu_reference)

print(a)
print(b)

assert (np.array_equal(a, b))

