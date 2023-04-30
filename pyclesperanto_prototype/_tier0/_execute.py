from ._backends import Backend
def execute(anchor, opencl_kernel_filename:str, kernel_name:str, global_size, parameters, prog = None, constants = None, image_size_independent_kernel_compilation : bool = None, device = None):
    """
    Call opencl kernels (.cl files)

    Parameters
    ----------
    anchor: str
            Enter __file__ when calling this method and the corresponding open.cl
            file lies in the same folder as the python file calling it.
    opencl_kernel_filename: str
        Filename of the open.cl file to be called
    kernel_name: str
        kernel method inside the open.cl file to be called
        most clij/clesperanto kernel functions have the same name as the file they are in
    global_size: list(int)
        global_size according to OpenCL definition (usually shape of the destination image).
    parameters: dict(str, any), optional
        dictionary containing parameters. Take care: They must be of the
        right type and in the right order as specified in the open.cl file.
    constants: dict(str, any), optional
        dictionary with names/values which will be added to the define
        statements. They are necessary, e.g. to create arrays of a given
        maximum size in OpenCL as variable array lengths are not supported.
    image_size_independent_kernel_compilation: bool, optional
        if set to true, the kernel can handle images of different size and
        is a bit slower. If set to false, it can handle only images of a
        specific size and is a bit faster

    See Also
    --------
    https://github.com/clij/clij-clearcl/blob/master/src/main/java/net/haesleinhuepf/clij/clearcl/util/CLKernelExecutor.java

    """
    return Backend.get_instance().get().execute(anchor, opencl_kernel_filename, kernel_name, global_size, parameters, prog, constants, image_size_independent_kernel_compilation, device)
