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
    print('---')
    print(gpu_example.max(axis=0))
    print(example.max(axis=0))
    print('---')
    print(gpu_example.max(axis=1))
    print(example.max(axis=1))
    print('---')
    print(gpu_example.max(axis=2))
    print(example.max(axis=2))

    assert np.allclose(gpu_example.min(axis=0), example.min(axis=0))
    assert np.allclose(gpu_example.min(axis=1), example.min(axis=1))
    assert np.allclose(gpu_example.min(axis=2), example.min(axis=2))
    assert np.allclose(gpu_example.min(), example.min())

    assert np.allclose(gpu_example.max(axis=0), example.max(axis=0))
    assert np.allclose(gpu_example.max(axis=1), example.max(axis=1))
    assert np.allclose(gpu_example.max(axis=2), example.max(axis=2))
    assert np.allclose(gpu_example.max(), example.max())

    assert np.allclose(gpu_example.sum(axis=0), example.sum(axis=0))
    assert np.allclose(gpu_example.sum(axis=1), example.sum(axis=1))
    assert np.allclose(gpu_example.sum(axis=2), example.sum(axis=2))
    assert np.allclose(gpu_example.sum(), example.sum())

def test_min_out():
    example = np.asarray([[
        [0, 0, 0, 1],
        [0, 0, 3, 1],
    ], [
        [0, 0, 3, 1],
        [1, 1, 1, 1]
    ]])

    gpu_example = cle.push(example)

    minimum = example.min(axis=0)
    copy = minimum.copy()
    gpu_example.min(axis=0, out=copy)
    assert np.allclose(minimum, copy)

    minimum = example.min(axis=1)
    copy = minimum.copy()
    gpu_example.min(axis=1, out=copy)
    assert np.allclose(minimum, copy)

    minimum = example.min(axis=2)
    copy = minimum.copy()
    gpu_example.min(axis=2, out=copy)
    assert np.allclose(minimum, copy)


def test_max_out():
    example = np.asarray([[
        [0, 0, 0, 1],
        [0, 0, 3, 1],
    ], [
        [0, 0, 3, 1],
        [1, 1, 1, 1]
    ]])

    gpu_example = cle.push(example)

    maximum = example.max(axis=0)
    copy = maximum.copy()
    gpu_example.max(axis=0, out=copy)
    assert np.allclose(maximum, copy)

    maximum = example.max(axis=1)
    copy = maximum.copy()
    gpu_example.max(axis=1, out=copy)
    assert np.allclose(maximum, copy)

    maximum = example.max(axis=2)
    copy = maximum.copy()
    gpu_example.max(axis=2, out=copy)
    assert np.allclose(maximum, copy)


def test_sum_out():
    example = np.asarray([[
        [0, 0, 0, 1],
        [0, 0, 3, 1],
    ], [
        [0, 0, 3, 1],
        [1, 1, 1, 1]
    ]])

    gpu_example = cle.push(example)

    sum = example.sum(axis=0)
    copy = sum.copy()
    gpu_example.sum(axis=0, out=copy)
    assert np.allclose(sum, copy)

    sum = example.sum(axis=1)
    copy = sum.copy()
    gpu_example.sum(axis=1, out=copy)
    assert np.allclose(sum, copy)

    sum = example.sum(axis=2)
    copy = sum.copy()
    gpu_example.sum(axis=2, out=copy)
    assert np.allclose(sum, copy)
