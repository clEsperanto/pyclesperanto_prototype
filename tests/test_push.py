import numpy as np
import pyclesperanto_prototype as cle
import pytest

def test_push_np():
    reference = np.asarray([
        [1, 2],
        [-3, 4]
    ])

    image = cle.push(reference)

    result = cle.pull(image)

    assert np.allclose(result, reference)

@pytest.mark.parametrize("dtype", [np.float32, np.uint8, np.int8, np.uint16, np.int16, np.uint32, np.int32, np.uint64, np.int64])
def test_push_np_dtypes(dtype):
    reference = np.asarray([
        [1, 2],
        [-3, 4]
    ]).astype(dtype)

    image = cle.push(reference)

    result = cle.pull(image)

    assert np.allclose(result, reference)
    assert result.dtype == reference.dtype


def test_push_list():
    reference = [
        [1, 2],
        [-3, 4]
    ]

    image = cle.push(reference)

    result = cle.pull(image)

    assert np.allclose(result, reference)


def test_push_tuple():
    reference = (
        [1, 2],
        [-3, 4]
    )

    image = cle.push(reference)

    result = cle.pull(image)

    assert np.allclose(result, reference)