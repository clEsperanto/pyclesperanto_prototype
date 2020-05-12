import numpy as np
from gputools import OCLProgram, OCLArray
import pyopencl
import os

########################################################################################################################
## methods API; potentially auto-generatable

def radius_to_kernel_size(radius):
    return radius * 2 + 1;

def maximum_sphere(input, output, radius_x, radius_y, radius_z=0):
    kernel_size_x = radius_to_kernel_size(radius_x);
    kernel_size_y = radius_to_kernel_size(radius_y);
    kernel_size_z = radius_to_kernel_size(radius_z);

    parameters = {
        "src":input,
        "dst":output,
        "Nx":kernel_size_x,
        "Ny":kernel_size_y
    };

    if (len(output.shape) == 2):
        execute(__file__, 'maximum_sphere_2d_x.cl', 'maximum_sphere_2d', output.shape, parameters);
    else:
        parameters.update({"Nz":kernel_size_z});
        execute(__file__, 'maximum_sphere_3d_x.cl', 'maximum_sphere_3d', output.shape, parameters);

def minimum_sphere(input, output, radius_x, radius_y, radius_z=0):
    kernel_size_x = radius_to_kernel_size(radius_x);
    kernel_size_y = radius_to_kernel_size(radius_y);
    kernel_size_z = radius_to_kernel_size(radius_z);

    parameters = {
        "src":input,
        "dst":output,
        "Nx":kernel_size_x,
        "Ny":kernel_size_y
    };

    if (len(output.shape) == 2):
        execute(__file__, 'minimum_sphere_2d_x.cl', 'minimum_sphere_2d', output.shape, parameters);
    else:
        parameters.update({"Nz":kernel_size_z});
        execute(__file__, 'minimum_sphere_3d_x.cl', 'minimum_sphere_3d', output.shape, parameters);

def top_hat_sphere(input, output, radius_x, radius_y, radius_z=0):
    temp1 = create(input.shape);
    temp2 = create(input.shape);
    minimum_sphere(input, temp1, radius_x, radius_y, radius_z);
    maximum_sphere(temp1, temp2, radius_x, radius_y, radius_z);
    add_images_weighted(input, temp2, output, 1, -1);

def add_image_and_scalar(input, output, scalar):
    parameters = {
        "src":input,
        "dst":output,
        "scalar":scalar
    };
    if (len(output.shape) == 2):
        execute(__file__, 'add_image_and_scalar_2d_x.cl', 'add_image_and_scalar_2d', output.shape, parameters);
    else:
        execute(__file__, 'add_image_and_scalar_3d_x.cl', 'add_image_and_scalar_3d', output.shape, parameters);

def add_images_weighted(input1, input2, output, weight1, weight2):
    parameters = {
        "src":input1,
        "src1":input2,
        "dst":output,
        "factor":weight1,
        "factor1":weight2
    };
    if (len(output.shape) == 2):
        execute(__file__, 'add_images_weighted_2d_x.cl', 'add_images_weighted_2d', output.shape, parameters);
    else:
        execute(__file__, 'add_images_weighted_3d_x.cl', 'add_images_weighted_3d', output.shape, parameters);


def multiplyMatrix(input1, input2, output):
    parameters = {
        "src1":input1,
        "src2":input2,
        "dst_matrix":output
    };
    execute(__file__, "multiply_matrix_x.cl", "multiply_matrix", output.shape, parameters);







########################################################################################################################
## Core methods

def push(nparray):
    '''
    converts a numpy arrat to an OpenCL array

    This method does the same as the converters in CLIJ but is less flexible
    https://github.com/clij/clij-core/tree/master/src/main/java/net/haesleinhuepf/clij/converters/implementations


    :param nparray: input numpy array
    :return: opencl-array
    '''
    return OCLArray.from_array(nparray.astype(np.float32))

def create(dimensions):
    '''
    Convenience method for creating images on the GPU. This method basicall does the same as in CLIJ:

    https://github.com/clij/clij2/blob/master/src/main/java/net/haesleinhuepf/clij2/CLIJ2.java#L156

    :param dimensions: size of the image
    :return: OCLArray, potentially with random values
    '''
    return OCLArray.empty(dimensions, np.float32)

def pull(oclarray):
    return np.asarray(oclarray);

def execute(anchor, opencl_kernel_filename, kernel_name, global_size, parameters):
    '''
    Convenience method for calling opencl kernel files

    This method basically does the same as the CLKernelExecutor in CLIJ:
    https://github.com/clij/clij-clearcl/blob/master/src/main/java/net/haesleinhuepf/clij/clearcl/util/CLKernelExecutor.java

    :param anchor: Enter __file__ when calling this method and the corresponding open.cl file lies in the same folder as the python file calling it.
    :param opencl_kernel_filename: Filename of the open.cl file
    :param kernel_name: kernel method inside the open.cl file to be called
    :param global_size: global_size according to OpenCL definition (usually size of the destination image.
    :param parameters: dictionary containing parameters. Take care: They must be of the right type
    :return:
    '''
    anchor_path = os.path.dirname(os.path.realpath(anchor)).replace("\\", "/") + "/"
    cle_path = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/") + "/"
    ocl_code = __readFile(cle_path + 'preamble.cl') + '\n' + __readFile(anchor_path + opencl_kernel_filename)
    #print(ocl_code)

    defines = ""
    defines = defines + '\n#define GET_IMAGE_WIDTH(image_key) IMAGE_SIZE_ ## image_key ## _WIDTH'
    defines = defines + '\n#define GET_IMAGE_HEIGHT(image_key) IMAGE_SIZE_ ## image_key ## _HEIGHT'
    defines = defines + '\n#define GET_IMAGE_DEPTH(image_key) IMAGE_SIZE_ ## image_key ## _DEPTH'

    arguments = []

    for key in parameters:
        #print(key)
        value = parameters[key]
        #print(value)
        if (isinstance(value, pyopencl.array.Array)):
            arguments.append(value.data)

            if(value.dtype ==  np.dtype('float32') ):
                typeId = 'f'

                # image type handling
                defines = defines + '\n#define CONVERT_' + key + '_PIXEL_TYPE clij_convert_float_sat'
                defines = defines + '\n#define IMAGE_' + key + '_TYPE __global float*'
                defines = defines + '\n#define IMAGE_' + key + '_PIXEL_TYPE float'

                # image size handling
                defines = defines + '\n#define IMAGE_SIZE_' + key + '_WIDTH ' + str(value.shape[0])
                if (value.ndim > 2):
                    defines = defines + '\n#define IMAGE_SIZE_' + key + '_HEIGHT ' + str(value.shape[1])
                else:
                    defines = defines + '\n#define IMAGE_SIZE_' + key + '_HEIGHT 1'
                if (value.ndim > 2):
                    defines = defines + '\n#define IMAGE_SIZE_' + key + '_DEPTH ' + str(value.shape[2])
                else:
                    defines = defines + '\n#define IMAGE_SIZE_' + key + '_DEPTH 1'

                # positions (dimensionality) handling
                if (value.ndim < 3):
                    defines = defines + '\n#define POS_' + key + '_TYPE int2'
                    if (value.ndim == 1):
                        defines = defines + '\n#define POS_' + key + '_INSTANCE(pos0,pos1,pos2,pos3) (int2)(pos0, 0)'
                    else:
                        defines = defines + '\n#define POS_' + key + '_INSTANCE(pos0,pos1,pos2,pos3) (int2)(pos0, pos1)'

                else:
                    defines = defines + '\n#define POS_' + key + '_TYPE int4'
                    defines = defines + '\n#define POS_' + key + '_INSTANCE(pos0,pos1,pos2,pos3) (int4)(pos0, pos1, pos2, 0)'

                # read/write images
                dimensions = 3
                if (value.ndim < 3):
                    dimensions = 2

                defines = defines + '\n#define READ_' + key + '_IMAGE(a,b,c) read_buffer' + str(dimensions) + 'd' + typeId + '(GET_IMAGE_WIDTH(a),GET_IMAGE_HEIGHT(a),GET_IMAGE_DEPTH(a),a,b,c)'
                defines = defines + '\n#define WRITE_' + key + '_IMAGE(a,b,c) write_buffer' + str(dimensions) + 'd' + typeId + '(GET_IMAGE_WIDTH(a),GET_IMAGE_HEIGHT(a),GET_IMAGE_DEPTH(a),a,b,c)'

            else:
                raise TypeError('other types than float32 aren`t supported yet for images/buffers/arrays')
        else:
            if (isinstance(value, int) ):
                arguments.append(np.array([value], np.int))
            elif (isinstance(value, float)):
                arguments.append(np.array([value], np.float32))
            else:
                raise TypeError('other types than float and int aren`t supported yet for parameters')


    defines = defines + '\n'
    ocl_code = defines + ocl_code;
    # print(defines)

    prog = OCLProgram(src_str=ocl_code)
    prog.run_kernel(kernel_name, global_size, None, *arguments)


########################################################################################################################
# internal stuff

def __readFile(filename):
    with open(filename, 'r') as myfile:
        data = myfile.read()
    return data
