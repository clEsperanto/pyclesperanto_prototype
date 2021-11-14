from ._backends import Backend
def execute(anchor, opencl_kernel_filename, kernel_name, global_size, parameters, constants = None):
    return Backend.get_instance().get().execute(anchor, opencl_kernel_filename, kernel_name, global_size, parameters, constants)