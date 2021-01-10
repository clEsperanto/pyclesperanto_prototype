import pyclesperanto_prototype as cle
import numpy as np

def test_radians_to_degrees():
    test = cle.push_zyx(np.asarray([
        [np.pi, 0, -0.5 * np.pi]
    ]))

    reference = cle.push_zyx(np.asarray([
        [180, 0, -90]
    ]))

    result = cle.radians_to_degrees(test)

    a = cle.pull_zyx(result)
    b = cle.pull_zyx(reference)

    assert (np.allclose(a,b,0.01))
