from .._tier0 import execute


def mask (src, mask, dst):
    """Computes a masked image by applying a mask to an image. 
    
    All pixel values x of image X will be copied
    to the destination image in case pixel value m at the same position in the mask image is not equal to 
    zero.
    
    <pre>f(x,m) = (x if (m != 0); (0 otherwise))</pre>

    Available for: 2D, 3D

    Parameters
    ----------
    (Image source, Image mask, ByRef Image destination)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_mask


    Returns
    -------

    """


    parameters = {
        "src":src,
        "mask":mask,
        "dst":dst
    }

    execute(__file__, 'mask_' + str(len(dst.shape)) + 'd_x.cl', 'mask_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

