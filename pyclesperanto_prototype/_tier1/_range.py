from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image, create_none, create

@plugin_function(categories=['transform', 'in assistant'], output_creator=create_none)
def range(source : Image,
          destination : Image = None,
          start_x: int = None,
          stop_x: int = None,
          step_x: int = None,
          start_y:int = None,
          stop_y: int = None,
          step_y: int = None,
          start_z:int = None,
          stop_z: int = None,
          step_z: int = None
          ) -> Image:

    if start_x is None:
        start_x = 0
    if stop_x is None:
        stop_x = source.shape[-1]
    if step_x is None:
        step_x = 1
    if start_y is None:
        start_y = 0
    if stop_y is None:
        stop_y = source.shape[-2]
    if step_y is None:
        step_y = 1

    if len(source.shape) > 2:
        if start_z is None:
            start_z = 0
        if stop_z is None:
            stop_z = source.shape[0]
        if step_z is None:
            step_z = 1
    else:
        start_z = 0
        stop_z = 1
        step_z = 1

    if destination is None:
        if len(source.shape) > 2:
            destination = create((stop_z - start_z, stop_y - start_y, stop_x - start_x), source.dtype)
        else:
            destination = create((stop_y - start_y, stop_x - start_x), source.dtype)

    parameters = {
        "dst":destination,
        "src":source,
        "start_x": start_x,
        "step_x": step_x,
        "start_y": start_y,
        "step_y": step_y,
        "start_z": start_z,
        "step_z": step_z,
    }

    execute(__file__, 'range_x.cl', 'range', destination.shape, parameters)
    return destination
