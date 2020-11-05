from .._tier0 import execute

def binary_edge_detection (src, dst):
    """Determines pixels/voxels which are on the surface of binary objects and sets only them to 1 in the 
    destination image. All other pixels are set to 0.

    Available for: 2D, 3D

    Parameters
    ----------
    (Image source, ByRef Image destination)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_binaryEdgeDetection


    Returns
    -------

    """


    parameters = {
        "dst": dst,
        "src":src
    }

    execute(__file__, 'binary_edge_detection_' + str(len(dst.shape)) + 'd_x.cl', 'binary_edge_detection_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
