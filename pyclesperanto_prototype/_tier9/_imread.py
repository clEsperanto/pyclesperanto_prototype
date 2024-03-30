from .._tier0 import Image

def imread(filename : str) -> Image:
    import warnings
    warnings.warn("cle.imread is deprecated, use skimage.io.imread instead.")
    from skimage.io import imread as skimread
    image = skimread(filename)

    from .._tier0 import push
    return push(image)

