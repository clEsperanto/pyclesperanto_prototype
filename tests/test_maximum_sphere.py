import pyclesperanto_prototype as cle
import numpy as np

def test_maximum_sphere_1():
    test = cle.push_zyx(np.asarray([
        [1, 1, 1],
        [1, 2, 1],
        [1, 1, 1]
    ]))

    test2 = cle.create(test)
    cle.maximum_sphere(test, test2, 1, 1, 1)

    a = cle.pull_zyx(test2)
    assert (np.min(a) == 1)
    assert (np.max(a) == 2)

    cle.set(test, 5)
    # print(test)
    # print(cle.pull(test))

    a = cle.pull_zyx(test)
    assert (np.min(a) == 5)
    assert (np.max(a) == 5)
    assert (np.mean(a) == 5)


def test_maximum_sphere_2():
    gpu_a = cle.push_zyx(np.asarray([[1, 1, 1], [1, 2, 1], [1, 1, 1]]))
    gpu_b = cle.create(gpu_a)
    cle.maximum_sphere(gpu_a, gpu_b, 1, 1, 1)

    a = cle.pull_zyx(gpu_b)
    assert np.min(a) == 1
    assert np.max(a) == 2

    cle.set(gpu_a, 5)
    assert np.all(cle.pull_zyx(gpu_a) == 5)