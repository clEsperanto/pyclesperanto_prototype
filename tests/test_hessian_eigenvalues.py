import pyclesperanto_prototype as cle
import numpy as np

def test_hessian_eigenvalues_2d():
    test = np.asarray([
        [1, -1],
        [1, -1]
    ])

    reference_small_hessian_eigenvalue = np.asarray([
        [-2, 0],
        [-2, 0]
    ])

    reference_large_hessian_eigenvalue = np.asarray([
        [0, 2],
        [0, 2]
    ])

    small_hessian_eigenvalue, _, large_hessian_eigenvalue = cle.hessian_eigenvalues(test)

    print(small_hessian_eigenvalue)
    print(large_hessian_eigenvalue)

    assert np.allclose(reference_small_hessian_eigenvalue, small_hessian_eigenvalue)
    assert np.allclose(reference_large_hessian_eigenvalue, large_hessian_eigenvalue)

def test_hessian_eigenvalues_3d():
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
            [1, -1],
            [1, -1]
        ], [
            [2, -2],
            [2, -2]
        ],
    ])

    reference_large_hessian_eigenvalue = np.asarray([
        [
            [1, -1],
            [1, -1]
        ], [
            [2, -2],
            [2, -2]
        ],
    ])

    reference_middle_hessian_eigenvalue = np.asarray([
        [
            [1, -1],
            [1, -1]
        ], [
            [2, -2],
            [2, -2]
        ],
    ])

    small_hessian_eigenvalue, middle_hessian_eigenvalue, large_hessian_eigenvalue = cle.hessian_eigenvalues(test)

    print(small_hessian_eigenvalue)
    print(middle_hessian_eigenvalue)
    print(large_hessian_eigenvalue)

    assert np.allclose(reference_small_hessian_eigenvalue, small_hessian_eigenvalue)
    assert np.allclose(reference_middle_hessian_eigenvalue, middle_hessian_eigenvalue)
    assert np.allclose(reference_large_hessian_eigenvalue, large_hessian_eigenvalue)
