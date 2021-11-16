from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(categories=['combine', 'in assistant'])
def paste (source : Image, destination : Image = None, destination_x : int = 0, destination_y : int = 0, destination_z : int = 0):
    """Pastes an image into another image at a given position. 
    
    Parameters
    ----------
    source : Image
    destination : Image
    destination_x : Number
    destination_y : Number
    destination_z : Number
    
    Returns
    -------
    destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.paste(source, destination, destination_x, destination_y, destination_z)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_paste3D
    """


    parameters = {
        "dst":destination,
        "src":source,
        "destination_x": int(destination_x),
        "destination_y": int(destination_y)
    }


    if (len(destination.shape) == 3):
        parameters.update({"destination_z": int(destination_z)});

    execute(__file__, 'paste_' + str(len(destination.shape)) + 'd_x.cl', 'paste_' + str(len(destination.shape)) + 'd', source.shape, parameters)
    return destination
