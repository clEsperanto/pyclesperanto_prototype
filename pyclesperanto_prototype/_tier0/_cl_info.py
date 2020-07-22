import pyopencl as cl
from ._pycl import get_device


def device_info(dev: cl.Device):
    info = dict()
    for c in dir(cl.device_info):
        if c[0].isupper() and c != "PARENT_DEVICE":
            try:
                info[c] = dev.get_info(getattr(cl.device_info, c))
            except cl.LogicError:
                info[c] = None
    return info


def platform_info(platform: cl.Platform):
    info = dict()
    for c in dir(cl.platform_info):
        if c[0].isupper():
            try:
                info[c] = platform.get_info(getattr(cl.platform_info, c))
            except cl.LogicError:
                info[c] = None
    return info


def cl_info():
    lines = []
    for platform in cl.get_platforms():
        lines += [platform.name]
        lines += [f"{k}:{v}" for k, v in platform_info(platform).items()]
        lines += ["\n"]
        for device in platform.get_devices():
            lines += ["    " + device.name]
            lines += [f"       {k}:{v}" for k, v in device_info(device).items()]
            lines += ["\n"]
        lines += ["\n"]

    lines += ["Current device: " + get_device().name]

    return "\n".join(lines)
