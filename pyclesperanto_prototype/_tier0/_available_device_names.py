from .._tier0._pycl import filter_devices
def available_device_names():
    """Retrieve a list of available OpenCL-devices

    Returns
    -------
        list of OpenCL-Devices
    """
    devices = filter_devices()
    device_names = [device.name for device in devices]
    return device_names