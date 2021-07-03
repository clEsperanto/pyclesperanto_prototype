import numpy as np

import pyclesperanto_prototype as cle
import pytest

def test_execute_raises_error_with_wrong_type_provided_1():
    # string is not supported as type to pass to an opencl-kernel
    # the following should fail:
    with pytest.raises(TypeError):
        cle.execute(None, 'test.cl', 'rest', [2,2], {'parameter':'text'})

