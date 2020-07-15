from ..tier0 import execute


def mask_label (src, labelmap, dst, label_id):
    """Computes a masked image by applying a label mask to an image. 
    
    All pixel values x of image X will be copied
    to the destination image in case pixel value m at the same position in the label_map image has the right index value i.
    
    f(x,m,i) = (x if (m == i); (0 otherwise))

    Available for: 2D, 3D

    Parameters
    ----------
    (Image source, Image label_map, ByRef Image destination, Number label_index)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_maskLabel


    Returns
    -------

    """


    parameters = {
        "src":src,
        "src_label_map":labelmap,
        "label_id": float(label_id),
        "dst": dst
    }

    execute(__file__, 'mask_label_' + str(len(dst.shape)) + 'd_x.cl', 'mask_label_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

