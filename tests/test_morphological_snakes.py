import pyclesperanto_prototype as cle
from skimage import morphology
from skimage import segmentation
import numpy as np

def test_morphological_chan_vese():

    image = generate_disk((50, 50), 5)

    reference = cle.push(segmentation.morphological_chan_vese(image, num_iter=1, smoothing=1, lambda1=1, lambda2=1))

    result = cle.morphological_chan_vese(image, num_iter=1, smoothing=1, lambda1=1, lambda2=1)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))


def test_morphological_chan_vese_on_membranes_2d():
    from skimage.data import cells3d
    from skimage.segmentation import morphological_chan_vese
    import pyclesperanto_prototype as cle
    cle.select_device("TX")
    print(cle.__version__)

    image2d = cells3d()[30, 0, ...]

    result_gpu = cle.morphological_chan_vese(image2d, num_iter=20, smoothing=10)
    result_cpu =     morphological_chan_vese(image2d, num_iter=20, smoothing=10)

    from skimage.io import imsave
    imsave("test1.tif", result_cpu)
    imsave("test2.tif", result_gpu)

    assert cle.array_equal(result_cpu, result_gpu)


def generate_disk(shape, radius):
    image = np.zeros(shape)
    image[image.shape[0] // 2 - radius:image.shape[0] // 2 + radius + 1, 
          image.shape[1] // 2 - radius:image.shape[1] // 2 + radius + 1] = morphology.disk(radius)
    return image
