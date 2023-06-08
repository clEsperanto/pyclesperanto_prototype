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
    """Crops an image according to a defined range and step size

    Parameters
    ----------
    source: Image
    destination: Image, optional
    start_x: int, optional
    stop_x: int, optional
    step_x: int, optional
    start_y: int, optional
    stop_y: int, optional
    step_y: int, optional
    start_z: int, optional
    stop_z: int, optional
    step_z: int, optional

    Returns
    -------
    destination
    """
    start_x, stop_x, step_x = correct_range(start_x, stop_x, step_x, source.shape[-1])
    start_y, stop_y, step_y = correct_range(start_y, stop_y, step_y, source.shape[-2])
    if len(source.shape) > 2:
        start_z, stop_z, step_z = correct_range(start_z, stop_z, step_z, source.shape[-3])
    else:
        start_z = 0
        stop_z = 1
        step_z = 1

    if destination is None:
        if len(source.shape) > 2:
            destination = create((abs(stop_z - start_z), abs(stop_y - start_y), abs(stop_x - start_x)), source.dtype)
        else:
            destination = create((abs(stop_y - start_y), abs(stop_x - start_x)), source.dtype)

    parameters = {
        "dst":destination,
        "src":source,
        "start_x": int(start_x),
        "step_x": int(step_x),
        "start_y": int(start_y),
        "step_y": int(step_y),
        "start_z": int(start_z),
        "step_z": int(step_z),
    }

    execute(__file__, 'range_x.cl', 'range', destination.shape, parameters)

    return destination


def correct_range(start, stop, step, size):
    # set in case not set (passed None)
    if step is None:
        step = 1
    if start is None:
        if step >= 0:
            start = 0
        else:
            start = size - 1

    if stop is None:
        if step >= 0:
            stop = size
        else:
            stop = -1

    # Check if ranges make sense
    if start >= size:
        if step >= 0:
            start = size
        else:
            start = size - 1
    if start < -size + 1:
        start = -size + 1
    if stop > size:
        stop = size
    if stop < -size:
        if start > 0:
            stop = 0 - 1
        else:
            stop = -size

    if start < 0:
        start = size - start
    if (start > stop and step > 0) or (start < stop and step < 0):
        stop = start

    return start, stop, step
