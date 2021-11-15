
class Backend():
    def __init__(self):
        from ._opencl_backend import opencl_backend
        self._current_backend = opencl_backend()
        #from ._cuda_backend import cuda_backend
        #self._current_backend = cuda_backend()

    def set(self, backend):
        self._current_backend = backend

    def get(self):
        return self._current_backend

    @classmethod
    def get_instance(cls):
        if not hasattr(cls, "instance"):
            cls.instance = Backend()
        return cls.instance

