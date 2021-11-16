from .._tier0._device import filter_devices
from typing import List

def available_device_names(dev_type: str = None, score_key = None) -> List[str]:
    """Retrieve a list of names of available OpenCL-devices

    Parameters
    ----------
    dev_type : str
        'cpu', 'gpu', or None; None means any type of device
    score_key : callable
        scoring function, accepts device and returns int, defaults to None

    Returns
    -------
        list of OpenCL-device names

    See Also
    --------
    filter_devices : Returns list of devices instead of device names

    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> gpu_devices = cle.available_device_names(dev_type="gpu")
    >>> print("Available GPU OpenCL devices:" + str(gpu_devices))
    >>>
    >>> cpu_devices = cle.available_device_names(dev_type="cpu")
    >>> print("Available CPU OpenCL devices:" + str(cpu_devices))
    """

    devices = filter_devices(dev_type=dev_type, score_key=score_key)
    device_names = [device.name for device in devices]

    # intermediate solution to add cupy
    try:
        import cupy
        from ._cuda_backend import cuda_backend
        device_names = device_names + [str(cuda_backend())]
    except ImportError:
        pass

    return device_names