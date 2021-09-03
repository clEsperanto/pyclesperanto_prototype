
import pyopencl as cl
import warnings
from functools import lru_cache

class OCLProgram(cl.Program):
    """ a wrapper class representing a CPU/GPU Program
    example:
         prog = OCLProgram("mykernels.cl",build_options=["-D FLAG"])
    """
    _wait_for_kernel_finish = None

    def __init__(self, file_name=None, src_str=None, build_options=[], dev=None):
        if file_name is not None:
            with open(file_name, "r") as f:
                src_str = f.read()

        if src_str is None:
            raise ValueError("empty src_str! ")

        if dev is None:
            from ._device import get_device
            dev = get_device()

        self._dev = dev
        self._kernel_dict = {}
        super().__init__(self._dev.context, src_str)
        self.build(options=build_options)

    def run_kernel(self, name, global_size, local_size, *args, **kwargs):
        if name not in self._kernel_dict:
            self._kernel_dict[name] = getattr(self, name)

        self._kernel_dict[name](
            self._dev.queue, global_size, local_size, *args, **kwargs
        )
        if OCLProgram._wait_for_kernel_finish:
            self._dev.queue.finish()

    @classmethod
    @lru_cache(maxsize=128)
    def from_source(cls, source):
        warnings.warn("OCLProgram.from_source is deprecated. Use Device.program_from_source instead.")
        return cls(src_str=source)