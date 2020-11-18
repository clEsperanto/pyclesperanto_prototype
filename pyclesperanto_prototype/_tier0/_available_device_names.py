from .._tier0._pycl import filter_devices
from typing import List

def available_device_names(*args, **kwargs) -> List[str]:
    """Retrieve a list of names of available OpenCL-devices

    Arguments are forwarded to `filter_devices`.

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
    devices = filter_devices(*args, **kwargs)
    device_names = [device.name for device in devices]
    return device_names