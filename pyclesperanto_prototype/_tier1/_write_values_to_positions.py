from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import create
from .._tier0 import create_none
from .._tier1 import maximum_x_projection
from .._tier0 import pull

@plugin_function(output_creator=create_none)
def write_values_to_positions(positions_and_values : Image, destination : Image = None):
    """Takes an image with three/four rows (2D: height = 3; 3D: height = 4): 
    x, y [, z] and v and target image. 
    
    The value v will be written at position x/y[/z] in the target image. 
    
    Parameters
    ----------
    positions_and_values : Image
    destination : Image
    
    Returns
    -------
    destination
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_writeValuesToPositions
    """

    if destination is None:
        max_pos = pull(maximum_x_projection(positions_and_values)).T.astype(int)
        max_pos = max_pos[0]
        
        if len(max_pos) == 4: # 3D image requested
            destination = create([max_pos[2] + 1,max_pos[1] + 1,max_pos[0] + 1])
        elif len(max_pos) == 3:  # 2D image requested
            destination = create([max_pos[1] + 1,max_pos[0] + 1])
        else:
            raise Exception("Size not supported: " + str(max_pos))

    parameters = {
        "dst":destination,
        "src":positions_and_values
    }

    execute(__file__, '../clij-opencl-kernels/kernels/write_values_to_positions_' + str(len(destination.shape)) + 'd_x.cl', 'write_values_to_positions_' + str(len(destination.shape)) + 'd', positions_and_values.shape, parameters)
    return destination
