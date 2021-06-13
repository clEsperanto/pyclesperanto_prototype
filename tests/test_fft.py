from skimage.data import grass
from scipy.fftpack import fftn, ifftn, fftshift
import numpy as np
import numpy.testing as npt
import pyclesperanto_prototype as cle

GRASS = grass().astype("float32")

scipy_fgrass = fftn(GRASS)
scipy_ifgrass = ifftn(scipy_fgrass)


def test_scipy_fft():
    assert not np.allclose(scipy_fgrass, GRASS, atol=100)
    assert scipy_fgrass.dtype == np.complex64
    assert scipy_fgrass.shape == (512, 512)
    # inverse
    npt.assert_allclose(scipy_ifgrass.real, GRASS, atol=1e-4)


def test_cle_fft():
    gpu_fgrass = cle.fftn(GRASS)
    fgrass = cle.pull(gpu_fgrass)

    assert not np.allclose(fgrass, GRASS, atol=100)
    npt.assert_allclose(fgrass, scipy_fgrass, atol=2e-1)

    gpu_ifgrss = cle.ifftn(gpu_fgrass)
    ifgrss = cle.pull(gpu_ifgrss)
    npt.assert_allclose(ifgrss.real, GRASS, atol=1e-4)


def test_cle_fftshift():
    scp_shift = fftshift(GRASS)
    cle_shift = cle.fftshift(GRASS).get()
    npt.assert_allclose(scp_shift, cle_shift)
