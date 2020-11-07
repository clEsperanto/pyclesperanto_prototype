from pyclesperanto_prototype._tier0._create import create_like
from pyclesperanto_prototype._tier1 import copy
from pyclesperanto_prototype._tier0._execute import execute
from ._set import set

def execute_separable_kernel(src, dst, anchor, opencl_kernel_filename, kernel_name, kernel_size_x, kernel_size_y, kernel_size_z, sigma_x, sigma_y, sigma_z, dimensions) :

    n = [kernel_size_x, kernel_size_y, kernel_size_z]
    sigma = [sigma_x, sigma_y, sigma_z]

    # todo: ensure that temp1 and temp2 become of type float
    temp1 = create_like(src);
    temp2 = create_like(src);

    if (sigma[0] > 0) :
        param_src = src;
        if (dimensions == 2):
            param_dst = temp1
        else :
            param_dst = temp2

        parameters = {
            "dst": param_dst,
            "src": param_src,
            "dim": int(0),
            "N": int(n[0]),
            "s": float(sigma[0])
        }

        execute(anchor, opencl_kernel_filename, kernel_name, src.shape, parameters)

    else :
        if (dimensions == 2):
            copy(src, temp1)
        else :
            copy(src, temp2)

    if (sigma[1] > 0) :
        if (dimensions == 2):
            param_src = temp1
            param_dst = dst
        else :
            param_src = temp2
            param_dst = temp1

        parameters = {
            "dst": param_dst,
            "src": param_src,
            "dim": int(1),
            "N": int(n[1]),
            "s": float(sigma[1])
        }

        execute(anchor, opencl_kernel_filename, kernel_name, src.shape, parameters)
    else :
        if (dimensions == 2):
            copy(temp1, dst)
        else :
            copy(temp2, temp1)

    if (dimensions == 3):
        if (sigma[2] > 0):

            parameters = {
                "dst": dst,
                "src": temp1,
                "dim": int(2),
                "N": int(n[2]),
                "s": float(sigma[2])
            }
            execute(anchor, opencl_kernel_filename, kernel_name, src.shape, parameters)
        else:
            copy(temp1, dst)

    return dst