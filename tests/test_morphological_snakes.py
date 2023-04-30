import pyclesperanto_prototype as cle
from skimage import morphology
from skimage import segmentation
import numpy as np

def test_morphological_snakes():

    image = generate_disk((50, 50), 5)

    reference = cle.push(segmentation.morphological_chan_vese(image, num_iter=1, smoothing=1, lambda1=1, lambda2=1))

    result = cle.morphological_snakes(image, num_iter=1, smoothing=1, lambda1=1, lambda2=1)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))


def generate_disk(shape, radius):
    image = np.zeros(shape)
    image[image.shape[0] // 2 - radius:image.shape[0] // 2 + radius + 1, 
          image.shape[1] // 2 - radius:image.shape[1] // 2 + radius + 1] = morphology.disk(radius)
    return image
