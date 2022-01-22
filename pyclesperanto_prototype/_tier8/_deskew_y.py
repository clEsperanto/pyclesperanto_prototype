from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import create_none, create_like

@plugin_function(categories=['transform', 'in assistant'], output_creator=create_none)
def deskew_y(source: Image,
          destination: Image = None,
          angle_in_degrees:float=30,
          linear_interpolation: bool = True,
          auto_size: bool = True):
    """
    Single-objective light-sheet image reconstruction

    Parameters
    ----------
    source
    destination
    factor_x
    factor_y
    factor_z
    centered
    linear_interpolation
    auto_size

    Returns
    -------

    """
