from ._backends import Backend
def execute(anchor, opencl_kernel_filename, kernel_name, global_size, parameters, prog = None, constants = None, image_size_independent_kernel_compilation : bool = None, device = None):
    return Backend.get_instance().get().execute(anchor, opencl_kernel_filename, kernel_name, global_size, parameters, prog, constants, image_size_independent_kernel_compilation, device)
