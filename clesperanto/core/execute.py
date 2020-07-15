from functools import lru_cache
from pathlib import Path

import numpy as np

import pyopencl as cl
from gputools import OCLProgram


# should write a test to make sure kernels and filenames always match
KERNEL_FILE_PATTERN = "{kernel_name}_{ndim}d_x.cl"


@lru_cache(maxsize=1)
def preamble():
    return (Path(__file__).parent / "preamble.cl").read_text()


@lru_cache(maxsize=128)
def get_ocl_source(kernel_name, ndim):
    from .. import plugins

    kernel_store = Path(plugins.__file__).parent
    fname = KERNEL_FILE_PATTERN.format(kernel_name=kernel_name, ndim=ndim)
    kernel = (kernel_store / fname).read_text()
    return "\n".join([preamble(), kernel])


def execute(kernel_name, global_size, parameters):
    """Convenience method for calling opencl kernel files.

    This method basically does the same as the CLKernelExecutor in CLIJ:
    https://github.com/clij/clij-clearcl/blob/master/src/main/java/net/haesleinhuepf/clij/clearcl/util/CLKernelExecutor.java

    :param anchor: Enter __file__ when calling this method and the corresponding open.cl
                   file lies in the same folder as the python file calling it.
    :param kernel_name: kernel method inside the open.cl file to be called
    :param global_size: global_size according to OpenCL definition (usually size of the
                        destination image.)
    :param parameters: dictionary containing parameters. Take care: They must be of the
                       right type
    :return:
    """

    defines = [
        "#define GET_IMAGE_WIDTH(image_key) IMAGE_SIZE_ ## image_key ## _WIDTH",
        "#define GET_IMAGE_HEIGHT(image_key) IMAGE_SIZE_ ## image_key ## _HEIGHT",
        "#define GET_IMAGE_DEPTH(image_key) IMAGE_SIZE_ ## image_key ## _DEPTH",
    ]

    arguments = []

    for key, value in parameters.items():

        if isinstance(value, cl.array.Array):
            arguments.append(value.data)

            if value.dtype != np.dtype("float32"):
                raise TypeError(
                    "Only float32 is currently supported for images/buffers/arrays"
                )

            # image type handling
            typeId = "f"
            ndim = value.ndim
            depth_height_width = [1, 1, 1]
            depth_height_width[-len(value.shape) :] = value.shape
            depth, height, width = depth_height_width
            pos_type = "int2" if ndim < 3 else "int4"
            pos = ["(pos0, 0)", "(pos0, pos1)", "(pos0, pos1, pos2, 0)"][ndim - 1]
            img_dims = 2 if ndim < 3 else 2

            defines.extend(
                [
                    f"#define CONVERT_{key}_PIXEL_TYPE clij_convert_float_sat",
                    f"#define IMAGE_{key}_TYPE __global float*",
                    f"#define IMAGE_{key}_PIXEL_TYPE float",
                    f"#define IMAGE_SIZE_{key}_WIDTH {width}",
                    f"#define IMAGE_SIZE_{key}_HEIGHT {height}",
                    f"#define IMAGE_SIZE_{key}_DEPTH {depth}",
                    f"#define POS_{key}_TYPE {pos_type}",
                    f"#define POS_{key}_INSTANCE(pos0,pos1,pos2,pos3) ({pos_type}){pos}",
                    f"#define READ_{key}_IMAGE(a,b,c) read_buffer{img_dims}d{typeId}"  # !
                    "(GET_IMAGE_WIDTH(a),GET_IMAGE_HEIGHT(a),GET_IMAGE_DEPTH(a),a,b,c)",
                    f"#define WRITE_{key}_IMAGE(a,b,c) write_buffer{img_dims}d{typeId}"  # !
                    "(GET_IMAGE_WIDTH(a),GET_IMAGE_HEIGHT(a),GET_IMAGE_DEPTH(a),a,b,c)",
                ]
            )

        elif isinstance(value, int):
            arguments.append(np.array([value], np.int))
        elif isinstance(value, float):
            arguments.append(np.array([value], np.float32))
        else:
            raise TypeError(
                "other types than float and int aren`t supported yet for parameters"
            )

    ndims = len(global_size)
    defines.append(get_ocl_source(kernel_name, ndims))
    ocl_code = "\n".join(defines)

    prog = OCLProgram(src_str=ocl_code)
    # Todo: the order of the arguments matters; fix that

    prog.run_kernel(
        f"{kernel_name}_{ndims}d", tuple(global_size[::-1]), None, *arguments
    )
