from .._tier0 import execute, create_binary_like
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(categories=['binary processing', 'label processing', 'in assistant'], output_creator=create_binary_like)
def binary_edge_detection(source : Image, destination : Image = None):
    """Determines pixels/voxels which are on the surface of binary objects and 
    sets only them to 1 in the 
    destination image. All other pixels are set to 0.
    
    Parameters
    ----------
    source : Image
        The binary input image where edges will be searched.
    destination : Image
        The output image where edge pixels will be 1.
     
    
    Returns
    -------
    destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.binary_edge_detection(source, destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_binaryEdgeDetection
    """


    parameters = {
        "dst": destination,
        "src":source
    }

    execute(__file__, '../clij-opencl-kernels/kernels/binary_edge_detection_' + str(len(destination.shape)) + 'd_x.cl', 'binary_edge_detection_' + str(len(destination.shape)) + 'd', destination.shape, parameters)
    return destination
