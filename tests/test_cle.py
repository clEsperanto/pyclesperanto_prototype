import numpy as np
import clesperanto as cle
import pyopencl as cl
import pytest


def test_add_image_and_scalar():
    data = np.arange(100).reshape(10, 10)
    # push an array to the GPU
    flip = cle.push(data)
    assert flip.shape == (10, 10)
    assert isinstance(flip, cl.array.Array)
    # create memory for the output
    flop = cle.create_like(data)
    assert flop.shape == (10, 10)
    assert isinstance(flop, cl.array.Array)
    # add a constant to all pixels
    cle.add_image_and_scalar(flip, flop, 100.0)
    # Note the transposition!
    np.testing.assert_allclose(data + 100, flop.get().T)


@pytest.mark.parametrize("shape", 2 ** np.arange(10)[5:], ids=lambda x: f"{x}x{x}")
@pytest.mark.parametrize("target", ["cpu", "gpu"])
def test_multiply_matrix(shape, benchmark, target):
    @benchmark
    def multiply():
        a_np = np.random.rand(shape, shape).astype("float32")
        b_np = np.random.rand(shape, shape).astype("float32")
        if target == 'gpu':
            # push arrays to GPU
            gpu_a = cle.push(a_np)
            gpu_b = cle.push(b_np)
            # allocate memory for result on GPU
            gpu_c = cle.create((shape, shape))
            cle.multiply_matrix(gpu_a, gpu_b, gpu_c)
            _ = gpu_c.get()
        else:
            # multiply matrix on CPU
            _ = np.dot(a_np.T, b_np.T)
        # np.testing.assert_allclose(cle.pull(gpu_c), cpu_c, atol=1e-3)