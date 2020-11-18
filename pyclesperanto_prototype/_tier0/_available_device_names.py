from .._tier0._pycl import filter_devices
from typing import List

def available_device_names() -> List[str]:
    """Retrieve a list of names of available OpenCL-devices

    Returns
    -------
        list of OpenCL-device names
    """
    devices = filter_devices()
    device_names = [device.name for device in devices]
    return device_names