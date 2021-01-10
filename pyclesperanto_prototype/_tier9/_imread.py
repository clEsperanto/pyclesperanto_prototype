from .._tier0 import Image

def imread(filename : str) -> Image:
    from skimage.io import imread as skimread
    image = skimread(filename)

    from .._tier0 import push
    return push(image)

