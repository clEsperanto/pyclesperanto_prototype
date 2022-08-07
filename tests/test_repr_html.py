import pyclesperanto_prototype as cle
import numpy as np

def test_repr_html():
    test = cle.push(np.asarray([
        [1, -1],
        [1, -1]
    ]))

    result = test._repr_html_()

    assert "16.0 B" in result
    assert "[ 1. -1.]" in result
