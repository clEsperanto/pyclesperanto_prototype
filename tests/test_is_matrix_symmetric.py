import pyclesperanto_prototype as cle
import numpy as np

def test_is_matrix_symmetric_1():
    test = cle.push(np.asarray([
        [1, 0, 0],
        [1, 1, 0],
        [1, 1, 1]
    ]))
    assert cle.is_matrix_symmetric(test) == False

def test_is_matrix_symmetric_2():
    test = cle.push(np.asarray([
        [1, 0, 0],
        [1, 1, 0],
    ]))
    assert cle.is_matrix_symmetric(test) == False

def test_is_matrix_symmetric_3():
    test = cle.push(np.asarray([
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0]
    ]))
    assert cle.is_matrix_symmetric(test) == True
