import pyclesperanto_prototype as cle
import numpy as np
import pyopencl as cl
import pytest

from . import LINUX, CI

@pytest.mark.xfail('LINUX and CI', reason='INVALID_ARG_SIZE on CI', raises=cl.LogicError)
def test_connected_components_labeling_box():
    
    gpu_input = cle.push(np.asarray([
        [
            [1, 0, 1],
            [1, 0, 0],
            [0, 0, 1]
        ]
    ]))

    gpu_reference = cle.push(np.asarray([
        [
            [1, 0, 2],
            [1, 0, 0],
            [0, 0, 3]
        ]
    ]))

    gpu_output = cle.connected_components_labeling_box(gpu_input)

    a = cle.pull_zyx(gpu_output)
    b = cle.pull_zyx(gpu_reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))