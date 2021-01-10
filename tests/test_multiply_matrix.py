import numpy as np
import pyclesperanto_prototype as cle
import pytest


@pytest.mark.parametrize("shape", 2 ** np.arange(9, 11), ids=lambda x: f"{x}x{x}")
@pytest.mark.parametrize("target", ["cpu", "gpu"])
def test_multiply_matrix(shape, benchmark, target):
    @benchmark
    def multiply():
        a_np = np.random.rand(shape, shape).astype("float32")
        b_np = np.random.rand(shape, shape).astype("float32")
        if target == "gpu":
            # push arrays to GPU
            gpu_a = cle.push_zyx(a_np)
            gpu_b = cle.push_zyx(b_np)
            # allocate memory for result on GPU
            gpu_c = cle.create((shape, shape))
            cle.multiply_matrix(gpu_a, gpu_b, gpu_c)
            _ = gpu_c.get()
        else:
            # multiply matrix on CPU
            _ = np.dot(a_np.T, b_np.T)
        # np.testing.assert_allclose(cle.pull(gpu_c), cpu_c, atol=1e-3)
