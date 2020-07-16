import pyclesperanto_prototype as cle
import numpy as np
import pyopencl as cl

from . import LINUX, CI


@pytest.mark.xfail('LINUX and CI', reason='INVALID_ARG_SIZE on CI', raises=cl.LogicError)
def test_maximum_sphere():
    test = cle.push(np.asarray([
        [1, 1, 1],
        [1, 2, 1],
        [1, 1, 1]
    ]))

    test2 = cle.create(test)
    cle.maximum_sphere(test, test2, 1, 1, 1)

    a = cle.pull(test2)
    assert (np.min(a) == 1)
    assert (np.max(a) == 2)

    cle.set(test, 5)
    # print(test)
    # print(cle.pull(test))

    a = cle.pull(test)
    assert (np.min(a) == 5)
    assert (np.max(a) == 5)
    assert (np.mean(a) == 5)

    print("ok maximum sphere")



def test_maximum_sphere():
    gpu_a = cle.push(np.asarray([[1, 1, 1], [1, 2, 1], [1, 1, 1]]))
    gpu_b = cle.create(gpu_a)
    cle.maximum_sphere(gpu_a, gpu_b, 1, 1, 1)

    a = cle.pull(gpu_b)
    assert np.min(a) == 1
    assert np.max(a) == 2

    cle.set(gpu_a, 5)
    assert np.all(cle.pull(gpu_a) == 5)