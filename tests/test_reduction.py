import pyclesperanto_prototype as cle
import numpy as np

def test_min():
    example = np.asarray([[
            [0, 0, 0, 1],
            [0, 0, 3, 1],
        ],[
            [0, 0, 3, 1],
            [1, 1, 1, 1]
    ]])

    gpu_example = cle.push(example)

    assert gpu_example.min() == example.min()

def test_min_max_xyz():
    example = np.asarray([[
            [0, 0, 0, 1],
            [0, 0, 3, 1],
        ],[
            [0, 0, 3, 1],
            [1, 1, 1, 1]
    ]])

    gpu_example = cle.push(example)

    print(gpu_example.min(axis=0))
    print(example.min(axis=0))
    print('---')
    print(gpu_example.min(axis=1))
    print(example.min(axis=1))
    print('---')
    print(gpu_example.min(axis=2))
    print(example.min(axis=2))

    assert np.allclose(gpu_example.min(axis=0), example.min(axis=0))
    assert np.allclose(gpu_example.min(axis=1), example.min(axis=1))
    assert np.allclose(gpu_example.min(axis=2), example.min(axis=2))
    assert np.allclose(gpu_example.min(axis=0), example.min(axis=0))
    assert np.allclose(gpu_example.min(axis=1), example.min(axis=1))
    assert np.allclose(gpu_example.min(axis=2), example.min(axis=2))

