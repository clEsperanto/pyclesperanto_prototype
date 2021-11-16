import pyclesperanto_prototype as cle
import numpy as np
import pyopencl as cl

def test_add_image_and_scalar():
    data = np.arange(100).reshape(10, 10)
    # push an array to the GPU
    flip = cle.push(data)
    assert flip.shape == (10, 10)
    assert isinstance(flip, cle._tier0._backends.Backend.get_instance().get().array_type())
    # create memory for the output
    flop = cle.create_like(data)
    assert flop.shape == (10, 10)
    assert isinstance(flop, cle._tier0._backends.Backend.get_instance().get().array_type())
    # add a constant to all pixels
    cle.add_image_and_scalar(flip, flop, 100.0)
    # Note the transposition!
    np.testing.assert_allclose(data + 100, flop.get())