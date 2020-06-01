from ..core import execute


def replace_intensities(src, map, dst):
    """Replaces integer intensities specified in a vector image. 
    
    The vector image must be 3D with size (m, 1, 1) where m corresponds to the maximum intensity in the original image. Assuming the vector image contains values (0, 1, 0, 2) means: 
     * All pixels with value 0 (first entry in the vector image) get value 0
     * All pixels with value 1 get value 1
     * All pixels with value 2 get value 0
     * All pixels with value 3 get value 2
    

    Available for: 2D, 3D

    Parameters
    ----------
    (Image input, Image new_values_vector, ByRef Image destination)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_replaceIntensities


    Returns
    -------

    """


    parameters = {
        "dst": dst,
        "src": src,
        "map": map
    }

    execute(__file__, 'replace_intensities_x.cl', 'replace_intensities', dst.shape, parameters)

