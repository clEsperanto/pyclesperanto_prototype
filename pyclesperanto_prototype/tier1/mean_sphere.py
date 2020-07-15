from ..tier0 import radius_to_kernel_size
from ..tier0 import execute

def mean_sphere(input, output, radius_x, radius_y, radius_z=0):
    """
    documentation placeholder
    """


    kernel_size_x = radius_to_kernel_size(radius_x);
    kernel_size_y = radius_to_kernel_size(radius_y);
    kernel_size_z = radius_to_kernel_size(radius_z);

    parameters = {
        "dst":output,
        "src":input,
        "Nx":int(kernel_size_x),
        "Ny":int(kernel_size_y)
    };

    if (len(output.shape) == 3):
        parameters.update({"Nz":int(kernel_size_z)});
    execute(__file__, 'mean_sphere_' + str(len(output.shape)) + 'd_x.cl', 'mean_sphere_' + str(len(output.shape)) + 'd', output.shape, parameters);
