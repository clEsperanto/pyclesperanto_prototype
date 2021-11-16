import cupy as cp
import numpy as np

preamble = """
#define MINMAX_TYPE int
#define sampler_t int

#define FLT_MIN          1.19209e-07

#define MAX_ARRAY_SIZE 1000

#define uchar unsigned char
#define ushort unsigned short
#define uint unsigned int
#define ulong unsigned long

__device__ inline int2 operator+(int2 a, int2 b)
{
    return make_int2(a.x + b.x, a.y + b.y);
}

__device__ inline int4 operator+(int4 a, int4 b)
{
    return make_int4(a.x + b.x, a.y + b.y, a.z + b.z,  a.w + b.w);
}

__device__ inline int2 operator*(int b, int2 a)
{
    return make_int2(b * a.x, b * a.y);
}

__device__ inline int4 operator*(int b, int4 a)
{
    return make_int4(b * a.x, b * a.y, b * a.z, b * a.w);
}

__device__ inline float pow ( float  x, int  y ) {
    return pow(float(x), float(y));
}

__device__ inline float2 sqrt ( float2  a ) {
    return make_float2(sqrt(a.x), sqrt(a.y));
}

__device__ inline float4 cross(float4 a, float4 b)
{ 
    return make_float4(a.y*b.z - a.z*b.y, a.z*b.x - a.x*b.z, a.x*b.y - a.y*b.x, 0); 
}

__device__ inline float dot(float4 a, float4 b)
{ 
    return a.x * b.x + a.y * b.y + a.z * b.z + a.w * b.w;
}

__device__ inline float length(float4 v)
{
    return sqrtf(dot(v, v));
}

__device__ inline uchar clij_convert_uchar_sat(float value) {
    if (value > 255) {
        return 255;
    }
    if (value < 0) {
        return 0;
    }
    return (uchar)value;
}


__device__ inline char clij_convert_char_sat(float value) {
    if (value > 127) {
        return 127;
    }
    if (value < -128) {
        return -128;
    }
    return (char)value;
}


__device__ inline ushort clij_convert_ushort_sat(float value) {
    if (value > 65535) {
        return 65535;
    }
    if (value < 0) {
        return 0;
    }
    return (ushort)value;
}


__device__ inline short clij_convert_short_sat(float value) {
    if (value > 32767) {
        return 32767;
    }
    if (value < -32768) {
        return -32768;
    }
    return (short)value;
}

__device__ inline uint clij_convert_uint_sat(float value) {
    if (value > 4294967295) {
        return 4294967295;
    }
    if (value < 0) {
        return 0;
    }
    return (uint)value;
}

__device__ inline uint convert_uint_sat(float value) {
    if (value > 4294967295) {
        return 4294967295;
    }
    if (value < 0) {
        return 0;
    }
    return (uint)value;
}


__device__ inline int clij_convert_int_sat(float value) {
    if (value > 2147483647) {
        return 2147483647;
    }
    if (value < -2147483648) {
        return -2147483648;
    }
    return (int)value;
}


__device__ inline uint clij_convert_ulong_sat(float value) {
    if (value > 18446744073709551615) {
        return 18446744073709551615;
    }
    if (value < 0) {
        return 0;
    }
    return (ulong)value;
}

__device__ inline int clij_convert_long_sat(float value) {
    if (value > 9223372036854775807) {
        return 9223372036854775807;
    }
    if (value < -9223372036854775808 ) {
        return -9223372036854775808 ;
    }
    return (long)value;
}

__device__ inline float clij_convert_float_sat(float value) {
    return value;
}

__device__ inline int get_global_id(int dim) {
    if (dim == 0) {
        return blockDim.x * blockIdx.x + threadIdx.x;
    } else if (dim == 1) {
        return blockDim.y * blockIdx.y + threadIdx.y;
    } else { //if (dim == 2) {
        return blockDim.z * blockIdx.z + threadIdx.z;
    } 
}

#define get_global_size(dim) global_size_ ## dim ## _size

#define READ_IMAGE(a,b,c) READ_ ## a ## _IMAGE(a,b,c)
#define WRITE_IMAGE(a,b,c) WRITE_ ## a ## _IMAGE(a,b,c)

#define GET_IMAGE_WIDTH(image_key) IMAGE_SIZE_ ## image_key ## _WIDTH
#define GET_IMAGE_HEIGHT(image_key) IMAGE_SIZE_ ## image_key ## _HEIGHT
#define GET_IMAGE_DEPTH(image_key) IMAGE_SIZE_ ## image_key ## _DEPTH

#define CLK_NORMALIZED_COORDS_FALSE 1
#define CLK_ADDRESS_CLAMP_TO_EDGE 2
#define CLK_FILTER_NEAREST 4
#define CLK_NORMALIZED_COORDS_TRUE 8
#define CLK_ADDRESS_CLAMP 16
#define CLK_FILTER_LINEAR 32
#define CLK_ADDRESS_NONE 64
"""

preamble_per_type = """
__device__ inline {pixel_type}2 read_buffer3d{typeId}(int read_buffer_width, int read_buffer_height, int read_buffer_depth, {pixel_type} * buffer_var, int sampler, int4 position )
{
    int4 pos = make_int4(position.x, position.y, position.z, 0);
    pos.x = max((MINMAX_TYPE)pos.x, (MINMAX_TYPE)0);
    pos.y = max((MINMAX_TYPE)pos.y, (MINMAX_TYPE)0);
    pos.z = max((MINMAX_TYPE)pos.z, (MINMAX_TYPE)0);
    pos.x = min((MINMAX_TYPE)pos.x, (MINMAX_TYPE)read_buffer_width - 1);
    pos.y = min((MINMAX_TYPE)pos.y, (MINMAX_TYPE)read_buffer_height - 1);
    pos.z = min((MINMAX_TYPE)pos.z, (MINMAX_TYPE)read_buffer_depth - 1);

    int pos_in_buffer = pos.x + pos.y * read_buffer_width + pos.z * read_buffer_width * read_buffer_height;
    if (pos.x < 0 || pos.x >= read_buffer_width || pos.y < 0 || pos.y >= read_buffer_height || pos.z < 0 || pos.z >= read_buffer_depth) {
        return make_{pixel_type}2(0, 0);
    }
    return make_{pixel_type}2(buffer_var[pos_in_buffer],0);
}

__device__ inline void write_buffer3d{typeId}(int write_buffer_width, int write_buffer_height, int write_buffer_depth, {pixel_type} * buffer_var, int4 pos, {pixel_type} value )
{
    int pos_in_buffer = pos.x + pos.y * write_buffer_width + pos.z * write_buffer_width * write_buffer_height;
    if (pos.x < 0 || pos.x >= write_buffer_width || pos.y < 0 || pos.y >= write_buffer_height || pos.z < 0 || pos.z >= write_buffer_depth) {
        return;
    }
    buffer_var[pos_in_buffer] = value;
}


__device__ inline {pixel_type}2 read_buffer2d{typeId}(int read_buffer_width, int read_buffer_height, int read_buffer_depth, {pixel_type} * buffer_var, int sampler, int2 position )
{
    int4 pos = make_int4(position.x, position.y, 0, 0);
    pos.x = max((MINMAX_TYPE)pos.x, (MINMAX_TYPE)0);
    pos.y = max((MINMAX_TYPE)pos.y, (MINMAX_TYPE)0);
    pos.z = max((MINMAX_TYPE)pos.z, (MINMAX_TYPE)0);
    pos.x = min((MINMAX_TYPE)pos.x, (MINMAX_TYPE)read_buffer_width - 1);
    pos.y = min((MINMAX_TYPE)pos.y, (MINMAX_TYPE)read_buffer_height - 1);
    pos.z = min((MINMAX_TYPE)pos.z, (MINMAX_TYPE)read_buffer_depth - 1);

    int pos_in_buffer = pos.x + pos.y * read_buffer_width;
    if (pos.x < 0 || pos.x >= read_buffer_width || pos.y < 0 || pos.y >= read_buffer_height) {
        return make_{pixel_type}2(0, 0);
    }
    //printf("Read2d %d %d %f \\n", pos.x, pos.y, float(buffer_var[pos_in_buffer]));
    return make_{pixel_type}2(buffer_var[pos_in_buffer],0);
}

__device__ inline void write_buffer2d{typeId}(int write_buffer_width, int write_buffer_height, int write_buffer_depth, {pixel_type} * buffer_var, int2 pos, {pixel_type} value )
{
    int pos_in_buffer = pos.x + pos.y * write_buffer_width;
    if (pos.x < 0 || pos.x >= write_buffer_width || pos.y < 0 || pos.y >= write_buffer_height) {
        return;
    }
    buffer_var[pos_in_buffer] = value;
}
"""

type_dict = {
    "f" : "float",
    "d" : "double",
    "c" : "char",
    "uc" : "uchar",
    "s" : "short",
    "us" : "ushort",
    "i" : "int",
    "ui" : "uint",
    "l" : "long",
    "ul" : "ulong"
    }

for type_id, pixel_type in type_dict.items():
    preamble = preamble + preamble_per_type.replace("{typeId}",type_id).replace("{pixel_type}", pixel_type)

COMMON_HEADER = """
#define CONVERT_{key}_PIXEL_TYPE clij_convert_{pixel_type}_sat
#define IMAGE_{key}_PIXEL_TYPE {pixel_type}
#define POS_{key}_TYPE {pos_type}
#define POS_{key}_INSTANCE(pos0,pos1,pos2,pos3) make_{pos_type}{pos}
"""

SIZE_HEADER = """
#define IMAGE_SIZE_{key}_WIDTH {width}
#define IMAGE_SIZE_{key}_HEIGHT {height}
#define IMAGE_SIZE_{key}_DEPTH {depth}
"""

ARRAY_HEADER = COMMON_HEADER + """
#define IMAGE_{key}_TYPE {size_parameters} {pixel_type}*
#define READ_{key}_IMAGE(a,b,c) read_buffer{img_dims}d{typeId}(GET_IMAGE_WIDTH(a),GET_IMAGE_HEIGHT(a),GET_IMAGE_DEPTH(a),a,b,c)
#define WRITE_{key}_IMAGE(a,b,c) write_buffer{img_dims}d{typeId}(GET_IMAGE_WIDTH(a),GET_IMAGE_HEIGHT(a),GET_IMAGE_DEPTH(a),a,b,c)
"""

def execute(anchor, opencl_kernel_filename, kernel_name, global_size, parameters, constants = None):
    from pathlib import Path
    # get code from disk
    if anchor is None:
        opencl_code = Path(opencl_kernel_filename).read_text()
    else:
        opencl_code = (Path(anchor).parent / opencl_kernel_filename).read_text()

    # assemble / translate code
    additional_code = ""

    if constants is not None:
        for key, value in constants.items():
            additional_code = additional_code + "#define " + str(key) + " " + str(value) + "\n"


    arguments = []

    arguments.append(global_size[-1])
    if len(global_size) > 1:
        arguments.append(global_size[-2])
    else:
        arguments.append(1)
    if len(global_size) > 2:
        arguments.append(global_size[0])
    else:
        arguments.append(1)
    size_params = "int global_size_0_size, int global_size_1_size, int global_size_2_size, "

    from ._cuda_backend import CUDAArray
    for key, value in parameters.items():

        if isinstance(value, CUDAArray):
            value = value.get_array()

        if isinstance(value, cp.ndarray):
            depth_height_width = [1, 1, 1]
            depth_height_width[-len(value.shape):] = value.shape
            depth, height, width = depth_height_width


            arguments.append(cp.int32(width))
            arguments.append(cp.int32(height))
            arguments.append(cp.int32(depth))

            if len(value.shape) < 3:
                img_dims =2
                pos_type ="int2"
                pos = "(pos0, pos1)"
            else:
                img_dims =3
                pos_type ="int4"
                pos = "(pos0, pos1, pos2, 0)"

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
            elif value.dtype == np.dtype("float64"):
                pixel_type = "double"
                type_id = "d"
            else:
                raise TypeError(f"Type {value.dtype} is currently unsupported for buffers/arrays")

            width = "image_" + key + "_width"
            height = "image_" + key + "_height"
            depth = "image_" + key + "_depth"

            size_params = size_params + "int " + width + ", int " + height + ", int " + depth + ", "

            additional_code = additional_code + SIZE_HEADER.format(
                key=key,
                width=width,
                height=height,
                depth=depth
            )

            additional_code = additional_code + ARRAY_HEADER.format(
                key=key,
                img_dims=img_dims,
                pixel_type=pixel_type,
                size_parameters=size_params,
                pos_type=pos_type,
                pos=pos,
                typeId=type_id
            )
            size_params = ""
            arguments.append(value)
        elif isinstance(value, int):
            arguments.append(cp.int32(value))
        elif isinstance(value, float):
            arguments.append(cp.float32(value))
        else:
            var_type = str(type(value))
            raise TypeError(
                f"other types than float and int aren`t supported yet for parameters {key} : {value} . \n"
                f"function {kernel_name}"
                f"type {var_type}"
            )

    #for i, a in enumerate(arguments):
    #    print(i, type(a), a)

    # dirty hacks
    opencl_code = opencl_code.replace("(int2){", "make_int2(")
    opencl_code = opencl_code.replace("(int4){", "make_int4(")
    opencl_code = opencl_code.replace("(int4)  {", "make_int4(")
    opencl_code = opencl_code.replace("(float4){", "make_float4(")
    opencl_code = opencl_code.replace("(float2){", "make_float2(")
    opencl_code = opencl_code.replace("int2 pos = {", "int2 pos = make_int2(")
    opencl_code = opencl_code.replace("int4 pos = {", "int4 pos = make_int4(")
    opencl_code = opencl_code.replace("};", ");")
    opencl_code = opencl_code.replace("})", "))")

    opencl_code = opencl_code.replace("(int2)", "make_int2")
    opencl_code = opencl_code.replace("(int4)", "make_int4")
    opencl_code = opencl_code.replace("__constant sampler_t", "__device__ int")
    opencl_code = opencl_code.replace("__const sampler_t", "__device__ int")
    opencl_code = opencl_code.replace("inline", "__device__ inline")
    opencl_code = opencl_code.replace("#pragma", "// #pragma")



    opencl_code = opencl_code.replace("__kernel ", "extern \"C\" __global__ ")
    opencl_code = opencl_code.replace("\nkernel void", "\nextern \"C\" __global__ void")

    cuda_kernel = "\n".join([preamble, additional_code, opencl_code])
    #print(cuda_kernel)

    # CUDA specific stuff
    block_size = (np.ones((len(global_size))) * 8).astype(int)
    grid_size = np.ceil(global_size / block_size).astype(int)
    grid = tuple(grid_size.tolist()[::-1])
    block = tuple(block_size.tolist())
    #print("Grid", grid)
    #print("Block", block)

    # load and compile
    a_kernel = cp.RawKernel(cuda_kernel, kernel_name)

    # run
    a_kernel(grid, block, tuple(arguments))

    #for i, a in enumerate(arguments):
    #    print(i, type(a), a)


