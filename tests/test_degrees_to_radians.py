import pyclesperanto_prototype as cle
import numpy as np

def test_degrees_to_radians():
    test = cle.push(np.asarray([
        [180, 0, -90]
    ]))

    reference = cle.push(np.asarray([
        [np.pi, 0, -0.5 * np.pi]
    ]))

    result = cle.degrees_to_radians(test)

    a = cle.pull(result)
    b = cle.pull(reference)

    assert (np.allclose(a,b,0.01))
