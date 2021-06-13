from skimage.data import grass
from scipy.fftpack import fftn, ifftn, fftshift
import numpy as np
import numpy.testing as npt
import pyclesperanto_prototype as cle
import pytest

_ = pytest.importorskip("reikna")

GRASS = grass().astype("float32")


def test_scipy_fft():
    scipy_fgrass = fftn(GRASS)
    scipy_ifgrass = ifftn(scipy_fgrass)

    assert not np.allclose(scipy_fgrass, GRASS, atol=100)
    assert scipy_fgrass.dtype == np.complex64
    assert scipy_fgrass.shape == GRASS.shape
    # inverse
    npt.assert_allclose(scipy_ifgrass.real, GRASS, atol=1e-4)


def test_cle_fft():
    gpu_fgrass = cle.fftn(GRASS)
    fgrass = cle.pull(gpu_fgrass)

    assert not np.allclose(fgrass, GRASS, atol=100)
    npt.assert_allclose(fgrass, fftn(GRASS), atol=2e-1)

    gpu_ifgrss = cle.ifftn(gpu_fgrass)
    ifgrss = cle.pull(gpu_ifgrss)
    npt.assert_allclose(ifgrss.real, GRASS, atol=1e-4)


def test_cle_fft_output_array():
    input = cle.push(GRASS, np.complex64)
    out = cle.create(input, np.complex64)
    cle.fftn(input, out)
    npt.assert_allclose(cle.pull(out), fftn(GRASS), atol=2e-1)


def test_cle_fft_inplace():
    input = cle.push(GRASS, np.complex64)
    cle.fftn(input, inplace=True)
    npt.assert_allclose(cle.pull(input), fftn(GRASS), atol=2e-1)


def test_cle_fft_errors():

    with pytest.raises(TypeError):
        # existing OCLArray must be of complex type
        cle.fftn(cle.push(GRASS))

    cle.fftn(cle.push(GRASS, np.complex64))
    cle.fftn(GRASS)

    input = cle.push(GRASS, np.complex64)
    out = cle.create(input, np.complex64)

    with pytest.raises(ValueError):
        # cannot provide both output and inplace
        cle.fftn(input, out, inplace=True)

    with pytest.raises(ValueError):
        # cannot use inplace with numpy array
        cle.fftn(GRASS, inplace=True)


def test_cle_fftshift():
    scp_shift = fftshift(GRASS)
    cle_shift = cle.fftshift(GRASS).get()
    npt.assert_allclose(scp_shift, cle_shift)
