import pyclesperanto_prototype as cle
import numpy as np

def test_repr_html_small_image():
    test = cle.push(np.asarray([
        [1, -1],
        [1, -1]
    ]))

    result = test._repr_html_()

    assert "cle.array([[ 1. -1." in result
    assert "dtype=float32)" in result


def test_repr_html_large_image():
    test = cle.push(np.zeros((10,10)))

    result = test._repr_html_()

    assert "400.0 B" in result
    assert "<img" in result
    assert "<table" in result
