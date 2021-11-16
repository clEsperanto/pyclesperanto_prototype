import os
from functools import lru_cache
from pathlib import Path

import numpy as np

import pyopencl as cl
from ._pycl import _OCLImage
from ._device import Device
from ._program import OCLProgram

if not os.getenv("PYOPENCL_COMPILER_OUTPUT"):
    import warnings
    warnings.filterwarnings('ignore', 'Non-empty compiler output', module='pyopencl')


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
    if anchor is None:
        kernel = Path(opencl_kernel_filename).read_text()
    else:
        kernel = (Path(anchor).parent / opencl_kernel_filename).read_text()
    return "\n".join([preamble(), kernel])

COMMON_HEADER = """
#define CONVERT_{key}_PIXEL_TYPE clij_convert_{pixel_type}_sat
#define IMAGE_{key}_PIXEL_TYPE {pixel_type}
#define POS_{key}_TYPE {pos_type}
#define POS_{key}_INSTANCE(pos0,pos1,pos2,pos3) ({pos_type}){pos}
"""

SIZE_HEADER = """
#define IMAGE_SIZE_{key}_WIDTH {width}
#define IMAGE_SIZE_{key}_HEIGHT {height}
#define IMAGE_SIZE_{key}_DEPTH {depth}
"""

ARRAY_HEADER = COMMON_HEADER + """
#define IMAGE_{key}_TYPE {size_parameters} __global {pixel_type}*
#define READ_{key}_IMAGE(a,b,c) read_buffer{img_dims}d{typeId}(GET_IMAGE_WIDTH(a),GET_IMAGE_HEIGHT(a),GET_IMAGE_DEPTH(a),a,b,c)
#define WRITE_{key}_IMAGE(a,b,c) write_buffer{img_dims}d{typeId}(GET_IMAGE_WIDTH(a),GET_IMAGE_HEIGHT(a),GET_IMAGE_DEPTH(a),a,b,c)
"""

IMAGE_HEADER = COMMON_HEADER + """
#define IMAGE_{key}_TYPE {size_parameters} {type_name} 
#define READ_{key}_IMAGE(a,b,c) read_image{typeId}(a,b,c)
#define WRITE_{key}_IMAGE(a,b,c) write_image{typeId}(a,b,c)
"""

def execute(anchor, opencl_kernel_filename, kernel_name, global_size, parameters, prog : OCLProgram = None, constants = None, image_size_independent_kernel_compilation : bool = None, device: Device = None):
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
    :param image_size_independent_kernel_compilation:  bool, if set to true, the kernel can handle images of different
                       size and isa bit slower. If set to false, it can handle only images of a specific size and is
                       a bit faster
    :return:
    """
    # import time
    # time_stamp = time.time()
    defines = ["#define MAX_ARRAY_SIZE 1000"]

    if image_size_independent_kernel_compilation != None:
        warnings.warn(
            "The `image_size_independent_kernel_compilation` parameter of pyclesperanto_prototype.execute is deprecated since 0.11.0. It will be removed in 0.12.0.",
            DeprecationWarning
        )
    else:
        image_size_independent_kernel_compilation = True


    if image_size_independent_kernel_compilation:
        defines.extend([
            "#define GET_IMAGE_WIDTH(image_key) image_size_ ## image_key ## _width",
            "#define GET_IMAGE_HEIGHT(image_key) image_size_ ## image_key ## _height",
            "#define GET_IMAGE_DEPTH(image_key) image_size_ ## image_key ## _depth"
        ])
    else:
        defines.extend([
            "#define GET_IMAGE_WIDTH(image_key) IMAGE_SIZE_ ## image_key ## _WIDTH",
            "#define GET_IMAGE_HEIGHT(image_key) IMAGE_SIZE_ ## image_key ## _HEIGHT",
            "#define GET_IMAGE_DEPTH(image_key) IMAGE_SIZE_ ## image_key ## _DEPTH"
        ])

    if constants is not None:
        for key, value in constants.items():
            defines.append("#define " + str(key) + " " + str(value))

    arguments = []

    for key, value in parameters.items():

        if isinstance(value, cl.array.Array):
            if value.dtype == np.dtype("uint8"):
                pixel_type = "uchar"
                type_id = "uc"
            elif value.dtype == np.dtype("uint16"):
                pixel_type = "ushort"
                type_id = "us"
            elif value.dtype == np.dtype("uint32"):
                pixel_type = "uint"
                type_id = "ui"
            elif value.dtype == np.dtype("uint64"):
                pixel_type = "ulong"
                type_id = "ul"
            elif value.dtype == np.dtype("int8"):
                pixel_type = "char"
                type_id = "c"
            elif value.dtype == np.dtype("int16"):
                pixel_type = "short"
                type_id = "s"
            elif value.dtype == np.dtype("int32"):
                pixel_type = "int"
                type_id = "i"
            elif value.dtype == np.dtype("int64"):
                pixel_type = "long"
                type_id = "l"
            elif value.dtype == np.dtype("float32"):
                pixel_type = "float"
                type_id = "f"
            else:
                raise TypeError(f"Type {value.dtype} is currently unsupported for buffers/arrays")

            # image type handling
            depth_height_width = [1, 1, 1]
            depth_height_width[-len(value.shape) :] = value.shape
            depth, height, width = depth_height_width
            ndim = value.ndim

            if image_size_independent_kernel_compilation:
                size_parameters = "int image_size_" + key + "_width" + \
                                  ", int image_size_" + key + "_height" + \
                                  ", int image_size_" + key + "_depth, "

                arguments.append(np.array([int(width)], np.int32))
                arguments.append(np.array([int(height)], np.int32))
                arguments.append(np.array([int(depth)], np.int32))
            else:
                size_parameters = ""

            arguments.append(value.base_data)


            params = {
                "typeId": type_id,
                "key": key,
                "pos_type": "int2" if value.ndim < 3 else "int4",
                "pos": ["(pos0, 0)", "(pos0, pos1)", "(pos0, pos1, pos2, 0)"][ndim - 1],
                "img_dims": 2 if ndim < 3 else 3,
                "depth": depth,
                "height": height,
                "width": width,
                "size_parameters":size_parameters,
                "pixel_type":pixel_type
            }
            defines.extend(ARRAY_HEADER.format(**params).split("\n"))

            if not image_size_independent_kernel_compilation:
                defines.extend(SIZE_HEADER.format(**params).split("\n"))


        elif isinstance(value, _OCLImage):

            if value.dtype == np.dtype("uint8"):
                pixel_type = "uchar"
                type_id = "ui"
            elif value.dtype == np.dtype("uint16"):
                pixel_type = "ushort"
                type_id = "us"
            elif value.dtype == np.dtype("uint32"):
                pixel_type = "uint"
                type_id = "ui"
            elif value.dtype == np.dtype("uint64"):
                pixel_type = "ulong"
                type_id = "ul"
            elif value.dtype == np.dtype("int8"):
                pixel_type = "char"
                type_id = "ui"
            elif value.dtype == np.dtype("int16"):
                pixel_type = "short"
                type_id = "us"
            elif value.dtype == np.dtype("int32"):
                pixel_type = "int"
                type_id = "ui"
            elif value.dtype == np.dtype("int64"):
                pixel_type = "long"
                type_id = "ul"
            elif value.dtype == np.dtype("float32"):
                pixel_type = "float"
                type_id = "f"
            else:
                raise TypeError(f"Type {value.dtype} is currently unsupported for buffers/arrays")

            # image type handling
            depth_height_width = [1, 1, 1]
            depth_height_width[-len(value.shape) :] = value.shape
            depth, height, width = depth_height_width
            ndim = len(value.shape)

            if image_size_independent_kernel_compilation:
                size_parameters = "int image_size_" + key + "_width" + \
                                  ", int image_size_" + key + "_height" + \
                                  ", int image_size_" + key + "_depth, "
                arguments.append(np.array([int(width)], np.int32))
                arguments.append(np.array([int(height)], np.int32))
                arguments.append(np.array([int(depth)], np.int32))
            else:
                size_parameters = ""

            arguments.append(value.data)

            if "destination" in key or "output" in key or "dst" in key:
                type_name = "__write_only image" + str(ndim) + "d_t"
            else:
                type_name = "__read_only image" + str(ndim) + "d_t"

            params = {
                "typeId": type_id, # can alternatively only be ui
                "type_name": type_name,
                "key": key,
                "pos_type": "int2" if ndim < 3 else "int4",
                "pos": ["(pos0, 0)", "(pos0, pos1)", "(pos0, pos1, pos2, 0)"][ndim - 1],
                "img_dims": 2 if ndim < 3 else 3,
                "depth": depth,
                "height": height,
                "width": width,
                "size_parameters":size_parameters,
                "pixel_type":pixel_type
            }
            defines.extend(IMAGE_HEADER.format(**params).split("\n"))
            if not image_size_independent_kernel_compilation:
                defines.extend(SIZE_HEADER.format(**params).split("\n"))

        elif isinstance(value, np.int8):
            arguments.append(np.asarray([value]).astype(np.int32))
        elif isinstance(value, np.uint8):
            arguments.append(np.array([value], np.uint8))
        elif isinstance(value, np.int16):
            arguments.append(np.array([value], np.int16))
        elif isinstance(value, np.uint16):
            arguments.append(np.array([value], np.uint16))
        elif isinstance(value, int) or isinstance(value, np.int32):
            arguments.append(np.array([value], np.int32))
        elif isinstance(value, float) or isinstance(value, np.float32):
            arguments.append(np.array([value], np.float32))
        elif isinstance(value, np.int64):
            arguments.append(np.array([value], np.int64))
        elif isinstance(value, np.uint64):
            arguments.append(np.array([value], np.uint64))
        elif isinstance(value, np.float64):
            arguments.append(np.array([value], np.float64))
        else:
            var_type = str(type(value))
            raise TypeError(
                f"other types than float and int aren`t supported yet for parameters {key} : {value} . \n"
                f"function {kernel_name}"
                f"type {var_type}"
            )

    # print("Assembling " + opencl_kernel_filename + " took " + str((time.time() - time_stamp) * 1000) + " ms")
    if prog is None:
        # time_stamp = time.time()

        defines.append(get_ocl_source(anchor, opencl_kernel_filename))

        if device is None:
            from ._device import get_device
            device = get_device()
        else:
            warnings.warn(
                "The `device` parameter of pyclesperanto_prototype.execute is deprecated since 0.11.0. It will be removed in 0.12.0.",
                DeprecationWarning
            )

        prog = device.program_from_source("\n".join(defines))
        #prog = OCLProgram.from_source("\n".join(defines))

        # Todo: the order of the arguments matters; fix that
        # print("Compilation " + opencl_kernel_filename + " took " + str((time.time() - time_stamp) * 1000) + " ms")
    else:
        warnings.warn(
            "The `prog` parameter of pyclesperanto_prototype.execute is deprecated since 0.11.0. It will be removed in 0.12.0.",
            DeprecationWarning
        )

    prog.run_kernel(kernel_name, tuple(global_size[::-1]), None, *arguments)

    return prog
