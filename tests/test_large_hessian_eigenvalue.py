import pyclesperanto_prototype as cle
import numpy as np

def test_large_hessian_eigenvalue_2d():
    test = np.asarray([
        [1, -1],
        [1, -1]
    ])

    reference_large_hessian_eigenvalue = np.asarray([
        [0, 2],
        [0, 2]
    ])

    large_hessian_eigenvalue = cle.large_hessian_eigenvalue(test)

    print(large_hessian_eigenvalue)

    assert np.allclose(reference_large_hessian_eigenvalue, large_hessian_eigenvalue)

def test_large_hessian_eigenvalue_3d():
    test = np.asarray([
        [
            [1, -1],
            [1, -1]
        ], [
            [2, -2],
            [2, -2]
        ],
    ])

    reference_large_hessian_eigenvalue = np.asarray([
        [
            [1.1, 2.1],
            [1.1, 2.1]
        ], [
            [0, 4.1],
            [0, 4.1]
        ],
    ])

    large_hessian_eigenvalue = cle.large_hessian_eigenvalue(test)

    print(large_hessian_eigenvalue)

    assert np.allclose(reference_large_hessian_eigenvalue, large_hessian_eigenvalue, atol=0.1)
