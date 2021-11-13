from ._backends import _current_backend
def execute(anchor, opencl_kernel_filename, kernel_name, global_size, parameters, constants = None):
    return _current_backend.execute(anchor, opencl_kernel_filename, kernel_name, global_size, parameters, constants)