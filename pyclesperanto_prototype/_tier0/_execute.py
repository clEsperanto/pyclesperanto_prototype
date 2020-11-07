from functools import lru_cache
from pathlib import Path

import numpy as np

import pyopencl as cl
from ._pycl import OCLProgram


# should write a test to make sure kernels and filenames always match
KERNEL_FILE_PATTERN = "{kernel_name}_{ndim}d_x.cl"


@lru_cache(maxsize=1)
def preamble():
    return (Path(__file__).parent / "preamble.cl").read_text()


# TODO: ultimately, this function could be used to get the ocl_source with just the kernel
# name and the ndim ... for now, use get_ocl_source so we don't have to change the signature
# of execute()

# @lru_cache(maxsize=128)
# def get_ocl_source(kernel_name, ndim):
#     from .. import plugins

#     kernel_store = Path(plugins.__file__).parent
#     fname = KERNEL_FILE_PATTERN.format(kernel_name=kernel_name, ndim=ndim)
#     kernel = (kernel_store / fname).read_text()
#     return "\n".join([preamble(), kernel])


# @lru_cache(maxsize=128)
def get_ocl_source(anchor, opencl_kernel_filename):
    kernel = (Path(anchor).parent / opencl_kernel_filename).read_text()
    return "\n".join([preamble(), kernel])


IMAGE_HEADER = """
#define CONVERT_{key}_PIXEL_TYPE clij_convert_float_sat
#define IMAGE_{key}_TYPE __global float*
#define IMAGE_{key}_PIXEL_TYPE float
#define IMAGE_SIZE_{key}_WIDTH {width}
#define IMAGE_SIZE_{key}_HEIGHT {height}
#define IMAGE_SIZE_{key}_DEPTH {depth}
#define POS_{key}_TYPE {pos_type}
#define POS_{key}_INSTANCE(pos0,pos1,pos2,pos3) ({pos_type}){pos}
#define READ_{key}_IMAGE(a,b,c) read_buffer{img_dims}d{typeId}(GET_IMAGE_WIDTH(a),GET_IMAGE_HEIGHT(a),GET_IMAGE_DEPTH(a),a,b,c)
#define WRITE_{key}_IMAGE(a,b,c) write_buffer{img_dims}d{typeId}(GET_IMAGE_WIDTH(a),GET_IMAGE_HEIGHT(a),GET_IMAGE_DEPTH(a),a,b,c)
"""


def execute(anchor, opencl_kernel_filename, kernel_name, global_size, parameters, prog : OCLProgram = None, constants = None):
    """
    Convenience method for calling opencl kernel files

    This method basically does the same as the CLKernelExecutor in CLIJ:
    https://github.com/clij/clij-clearcl/blob/master/src/main/java/net/haesleinhuepf/clij/clearcl/util/CLKernelExecutor.java

    :param anchor: Enter __file__ when calling this method and the corresponding open.cl
                   file lies in the same folder as the python file calling it.
    :param opencl_kernel_filename: Filename of the open.cl file
    :param kernel_name: kernel method inside the open.cl file to be called
    :param global_size: global_size according to OpenCL definition (usually size of the
                        destination image).
    :param parameters: dictionary containing parameters. Take care: They must be of the
                       right type
    :param constants:  dictionary with names/values which will be added to the define
                       statements. They are necessary, e.g. to create arrays of a given
                       maximum size in OpenCL as variable array lengths are not
                       supported.

    :return:
    """
    # import time
    # time_stamp = time.time()

    defines = [
        "#define GET_IMAGE_WIDTH(image_key) IMAGE_SIZE_ ## image_key ## _WIDTH",
        "#define GET_IMAGE_HEIGHT(image_key) IMAGE_SIZE_ ## image_key ## _HEIGHT",
        "#define GET_IMAGE_DEPTH(image_key) IMAGE_SIZE_ ## image_key ## _DEPTH",
    ]

    if constants is not None:
        for key, value in constants.items():
            defines.append("#define " + str(key) + " " + str(value))

    arguments = []

    for key, value in parameters.items():

        if isinstance(value, cl.array.Array):
            arguments.append(value.data)

            if value.dtype != np.dtype("float32"):
                raise TypeError(
                    "Only float32 is currently supported for images/buffers/arrays"
                )

            # image type handling
            depth_height_width = [1, 1, 1]
            depth_height_width[-len(value.shape) :] = value.shape
            depth, height, width = depth_height_width
            ndim = value.ndim
            params = {
                "typeId": "f",
                "key": key,
                "pos_type": "int2" if value.ndim < 3 else "int4",
                "pos": ["(pos0, 0)", "(pos0, pos1)", "(pos0, pos1, pos2, 0)"][ndim - 1],
                "img_dims": 2 if ndim < 3 else 3,
                "depth": depth,
                "height": height,
                "width": width,
            }
            defines.extend(IMAGE_HEADER.format(**params).split("\n"))

        elif isinstance(value, int):
            arguments.append(np.array([value], np.int32))
        elif isinstance(value, float):
            arguments.append(np.array([value], np.float32))
        else:
            raise TypeError(
                f"other types than float and int aren`t supported yet for parameters {value}"
            )

    # print("Assembling " + opencl_kernel_filename + " took " + str((time.time() - time_stamp) * 1000) + " ms")
    if prog is None:
        # time_stamp = time.time()

        defines.append(get_ocl_source(anchor, opencl_kernel_filename))
        prog = OCLProgram.from_source("\n".join(defines))
        # Todo: the order of the arguments matters; fix that
        # print("Compilation " + opencl_kernel_filename + " took " + str((time.time() - time_stamp) * 1000) + " ms")

    prog.run_kernel(kernel_name, tuple(global_size[::-1]), None, *arguments)

    return prog
