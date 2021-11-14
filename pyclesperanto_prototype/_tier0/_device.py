import pyopencl as cl
from typing import Callable, List, Optional
from functools import lru_cache

# TODO: we should discuss whether this collection is actually the best thing to pass
# around. might be better to work lower level with contexts...
class Device:
    """Just a container for a device, context and queue."""

    def __init__(self, device: cl.Device, context: cl.Context, queue: cl.CommandQueue):
        self.device = device
        self.context = context
        self.queue = queue

    def __repr__(self) -> str:
        refs = self.context.reference_count
        return f"<{self.name} on Platform: {self.device.platform.name} ({refs} refs)>"

    @property
    def name(self) -> str:
        return self.device.name

    @lru_cache(maxsize=128)
    def program_from_source(self, source):
        from ._program import OCLProgram
        return OCLProgram(src_str=source, dev=self)


def score_device(dev: cl.Device) -> float:
    score = 4e12 if dev.type == cl.device_type.GPU else 2e12
    score += dev.get_info(cl.device_info.GLOBAL_MEM_SIZE)
    return score


# container for singleton device
class _current_device:
    _instance: Optional[Device] = None
    score_key: Callable[[cl.Device], float] = score_device


def get_device() -> Device:
    """Get the current device GPU class."""
    return _current_device._instance or select_device()


def select_device(name: str = None, dev_type: str = None, score_key=None) -> Device:
    """Set current GPU device based on optional parameters.

    :param name: First device that contains ``name`` will be returned, defaults to None
    :type name: str, optional
    :param dev_type: {'cpu', 'gpu', or None}, defaults to None
    :type dev_type: str, optional
    :param score_key: scoring function, accepts device and returns int, defaults to None
    :type score_key: callable, optional
    :return: The current GPU instance.
    :rtype: GPU
    """

    # intermediate solution to be able to select cupy
    try:
        import cupy
        from ._cuda_backend import cuda_backend
        cuda_b = cuda_backend()
        if name in str(cuda_b) or name == str(cuda_b):
            from ._backends import Backend
            Backend.get_instance().set(cuda_b)
            return str(cuda_b)
    except:
        pass


    device = filter_devices(name, dev_type, score_key)[-1]
    if _current_device._instance and device == _current_device._instance.device:
        return _current_device._instance
    context = cl.Context(devices=[device])
    queue = cl.CommandQueue(context)
    _current_device._instance = Device(device, context, queue)
    return _current_device._instance

def new_device(name: str = None, dev_type: str = None, score_key=None) -> Device:
    device = filter_devices(name, dev_type, score_key)[-1]
    context = cl.Context(devices=[device])
    queue = cl.CommandQueue(context)
    return Device(device, context, queue)

def filter_devices(
    name: str = None, dev_type: str = None, score_key=None
) -> List[cl.Device]:
    """Filter devices based on various options

    :param name: First device that contains ``name`` will be returned, defaults to None
    :type name: str, optional
    :param dev_type: {'cpu', 'gpu', or None}, defaults to None
    :type dev_type: str, optional
    :param score_key: scoring function, accepts device and returns int, defaults to None
    :type score_key: callable, optional
    :return: list of devices
    :rtype: List[cl.Device]
    """
    devices = []
    for platform in cl.get_platforms():
        for device in platform.get_devices():
            if name and name.lower() in device.name.lower():
                return [device]
            if dev_type is not None:
                if isinstance(dev_type, str):
                    if dev_type.lower() == "cpu":
                        dev_type = cl.device_type.CPU
                    elif dev_type.lower() == "gpu":
                        dev_type = cl.device_type.GPU
                if device.type != dev_type:
                    continue
            devices.append(device)
    return sorted(devices, key=score_key or _current_device.score_key)


def set_device_scoring_key(func: Callable[[cl.Device], int]) -> None:
    if not callable(func):
        raise TypeError(
            "Scoring key must be a callable that takes a device and returns an int"
        )
    try:
        filter_devices(score_key=func)
    except Exception as e:
        raise ValueError(f"Scoring algorithm invalid: {e}")
    _current_device.score_key = func

