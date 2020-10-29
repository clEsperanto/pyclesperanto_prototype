import pyclesperanto_prototype as cle
import numpy as np
import pytest
import pyopencl as cl

from . import LINUX, CI

@pytest.mark.xfail('LINUX and CI', reason='INVALID_ARG_SIZE on CI', raises=cl.LogicError)
def test_center_of_mass():

    test = cle.push_zyx(np.asarray([
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0]
    ]))

    c = cle.center_of_mass(test)

    print(c)

    assert (np.array_equal(c, [2, 1, 0]))
    print("ok center_of_mass")


