import pyclesperanto_prototype as cle
import numpy as np

def test_small_hessian_eigenvalue_2d():
    test = np.asarray([
        [1, -1],
        [1, -1]
    ])

    reference_small_hessian_eigenvalue = np.asarray([
        [-2, 0],
        [-2, 0]
    ])

    small_hessian_eigenvalue = cle.small_hessian_eigenvalue(test)

    print(small_hessian_eigenvalue)

    assert np.allclose(reference_small_hessian_eigenvalue, small_hessian_eigenvalue)

def test_small_hessian_eigenvalue_3d():
    test = np.asarray([
        [
            [1, -1],
            [1, -1]
        ], [
            [2, -2],
            [2, -2]
        ],
    ])

    reference_small_hessian_eigenvalue = np.asarray([
        [
            [-2.1, -1.1],
            [-2.1, -1.1]
        ], [
            [-4.1, 0],
            [-4.1, 0]
        ],
    ])

    small_hessian_eigenvalue = cle.small_hessian_eigenvalue(test)

    print(small_hessian_eigenvalue)

    assert np.allclose(reference_small_hessian_eigenvalue, small_hessian_eigenvalue, atol=0.1)
