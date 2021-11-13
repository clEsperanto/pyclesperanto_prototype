import cupy as cp
import numpy as np

preamble = """
#define MINMAX_TYPE int
#define sampler_t int

__device__ inline float2 read_buffer3df(int read_buffer_width, int read_buffer_height, int read_buffer_depth, float * buffer_var, int sampler, int4 position )
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
        return make_float2(0, 0);
    }
    return make_float2(buffer_var[pos_in_buffer],0);
}

__device__ inline void write_buffer3df(int write_buffer_width, int write_buffer_height, int write_buffer_depth, float * buffer_var, int4 pos, float value )
{
    int pos_in_buffer = pos.x + pos.y * write_buffer_width + pos.z * write_buffer_width * write_buffer_height;
    if (pos.x < 0 || pos.x >= write_buffer_width || pos.y < 0 || pos.y >= write_buffer_height || pos.z < 0 || pos.z >= write_buffer_depth) {
        return;
    }
    buffer_var[pos_in_buffer] = value;
}


__device__ inline float2 read_buffer2df(int read_buffer_width, int read_buffer_height, int read_buffer_depth, float * buffer_var, int sampler, int2 position )
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
        return make_float2(0, 0);
    }
    return make_float2(buffer_var[pos_in_buffer],0);
}

__device__ inline void write_buffer2df(int write_buffer_width, int write_buffer_height, int write_buffer_depth, float * buffer_var, int2 pos, float value )
{
    int pos_in_buffer = pos.x + pos.y * write_buffer_width;
    if (pos.x < 0 || pos.x >= write_buffer_width || pos.y < 0 || pos.y >= write_buffer_height) {
        return;
    }
    buffer_var[pos_in_buffer] = value;
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

#define READ_IMAGE(a,b,c) READ_ ## a ## _IMAGE(a,b,c)
#define WRITE_IMAGE(a,b,c) WRITE_ ## a ## _IMAGE(a,b,c)

#define GET_IMAGE_WIDTH(image_key) IMAGE_SIZE_ ## image_key ## _WIDTH
#define GET_IMAGE_HEIGHT(image_key) IMAGE_SIZE_ ## image_key ## _HEIGHT
#define GET_IMAGE_DEPTH(image_key) IMAGE_SIZE_ ## image_key ## _DEPTH

#define CLK_NORMALIZED_COORDS_FALSE 1
#define CLK_ADDRESS_CLAMP_TO_EDGE 2
#define CLK_FILTER_NEAREST 4
"""


COMMON_HEADER = """
#define CONVERT_{key}_PIXEL_TYPE clij_convert_{pixel_type}_sat
#define IMAGE_{key}_PIXEL_TYPE {pixel_type}
#define POS_{key}_TYPE {pos_type}
#define POS_{key}_INSTANCE(pos0,pos1,pos2,pos3) make_{pos_type}({pos})
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

    for key, value in parameters.items():
        if isinstance(value, cp.ndarray):
            width = "image_" + key + "_width"
            height = "image_" + key + "_height"
            depth = "image_" + key + "_depth"

            arguments.append(cp.int32(value.shape[-1]))
            arguments.append(cp.int32(value.shape[-2]))

            if len(value.shape) < 3:
                img_dims =2
                pos_type ="int2"
                pos = "(pos0, pos1)"
                arguments.append(cp.int32(0)) # image depth
            else:
                img_dims =3
                pos_type ="int4"
                pos = "(pos0, pos1, pos2, 0)"
                arguments.append(cp.int32(value.shape[0]))

            size_params = "int " + width + ", int " + height + ", int " + depth + ", "

            additional_code = additional_code + SIZE_HEADER.format(
                key=key,
                width=width,
                height=height,
                depth=depth
            )

            additional_code = additional_code + ARRAY_HEADER.format(
                key=key,
                img_dims=img_dims,
                pixel_type="float",
                size_parameters=size_params,
                pos_type=pos_type,
                pos=pos,
                typeId="f"
            )
            arguments.append(value)
        elif isinstance(value, int):
            arguments.append(cp.int32(value))
        elif isinstance(value, float):
            arguments.append(cp.float32(value))

    for i, a in enumerate(arguments):
        print(i, type(a), a)

    # dirty hacks
    opencl_code = opencl_code.replace("(int2){", "make_int2(")
    opencl_code = opencl_code.replace("(int4){", "make_int4(")
    opencl_code = opencl_code.replace("};", ");")

    opencl_code = opencl_code.replace("(int2)", "make_int2")
    opencl_code = opencl_code.replace("(int4)", "make_int4")
    opencl_code = opencl_code.replace("__constant sampler_t", "__device__ int")

    opencl_code = opencl_code.replace("__kernel ", "extern \"C\" __global__ ")

    cuda_kernel = "\n".join([preamble, additional_code, opencl_code])
    print(cuda_kernel)

    # CUDA specific stuff
    block_size = (np.ones((len(global_size))) * 16).astype(int)
    grid_size = np.ceil(global_size / block_size).astype(int)
    grid = tuple(grid_size.tolist())
    block = tuple(block_size.tolist())
    print("Grid", grid)
    print("Block", block)

    # load and compile
    a_kernel = cp.RawKernel(cuda_kernel, kernel_name)

    # run
    a_kernel(grid, block, tuple(arguments))

    for i, a in enumerate(arguments):
        print(i, type(a), a)


