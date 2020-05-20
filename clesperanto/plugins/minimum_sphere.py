from ..core import radius_to_kernel_size
from ..core import execute

def minimum_sphere(input, output, radius_x, radius_y, radius_z=0):
    kernel_size_x = radius_to_kernel_size(radius_x);
    kernel_size_y = radius_to_kernel_size(radius_y);
    kernel_size_z = radius_to_kernel_size(radius_z);

    parameters = {
        "dst":output,
        "src":input,
        "Nx":int(kernel_size_x),
        "Ny":int(kernel_size_y)
    };

    if (len(output.shape) == 2):
        execute(__file__, 'minimum_sphere_2d_x.cl', 'minimum_sphere_2d', output.shape, parameters);
    else:
        parameters.update({"Nz":int(kernel_size_z)});
        execute(__file__, 'minimum_sphere_3d_x.cl', 'minimum_sphere_3d', output.shape, parameters);
