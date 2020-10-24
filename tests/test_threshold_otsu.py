

import pytest
import pyopencl as cl

from . import LINUX, CI

@pytest.mark.xfail('LINUX and CI', reason='INVALID_ARG_SIZE on CI', raises=cl.LogicError)
def test_threshold_otsu_against_scikit_image():

    # threshold using skimage
    from skimage.data import camera
    from skimage.filters import threshold_otsu
    image = camera()
    thresh = threshold_otsu(image)
    binary = image > thresh

    print(thresh)

    #from skimage import exposure
    #counts, bin_centers = exposure.histogram(image.ravel(), 256, source_range='image')

    #print(str(counts))
    #print(str(bin_centers))


    # threshold in GPU
    import pyclesperanto_prototype as cle
    gpu_image = cle.push(image)
    gpu_binary = cle.threshold_otsu(gpu_image)

    print(str(binary))
    print(str(cle.pull(gpu_binary)))


    # compare
    import numpy as np
    assert(np.allclose(binary, (cle.pull(gpu_binary) > 0)))
