import pyclesperanto_prototype as cle
import numpy as np

def test_binary_and_1():

    test = cle.push(np.asarray([
        [1, 0],
        [1, 0]
    ]))

    test1 = cle.push(np.asarray([
        [1, 1],
        [0, 0]
    ]))

    test2 = cle.create(test)
    cle.binary_and(test, test1, test2)

    print(test2)

    a = cle.pull(test2)
    assert (np.min(a) == 0)
    assert (np.max(a) == 1)
    assert (np.mean(a) == 0.25)
    print ("ok binary_and")



def test_binary_and_2():
    a = np.asarray([[1, 0], [1, 0]])
    b = np.asarray([[1, 1], [0, 0]])
    gpu_a = cle.push(a)
    gpu_b = cle.push(b)
    gpu_c = cle.create(gpu_a)
    cle.binary_and(gpu_a, gpu_b, gpu_c)

    result = cle.pull(gpu_c)
    assert np.allclose(result, a & b)