from pyclesperanto_prototype._tier0 import Image, plugin_function, execute
from pyclesperanto_prototype._tier1 import mean_box
from pyclesperanto_prototype._tier3 import mean_of_all_pixels

@plugin_function(categories=['filter', 'combine', 'in assistant'])
def cross_correlation(source: Image, convolution_kernel: Image, destination: Image = None,
                      radius_x: float = 1, radius_y: float = 1, radius_z: float = 1) -> Image:

    if len(convolution_kernel.shape) == 2:
        source_mean = mean_box(source, radius_x=convolution_kernel.shape[1] / 2,
                               radius_y=convolution_kernel.shape[0] / 2)

    else:
        source_mean = mean_box(source, radius_x=convolution_kernel.shape[2]/2, radius_y=convolution_kernel.shape[1]/2, radius_z=convolution_kernel.shape[0]/2)

    kernel_mean = mean_of_all_pixels(convolution_kernel)

    # source_mean = mean_box(source, radius_x=radius_x, radius_y=radius_y, radius_z=radius_z)
    # kernel_mean = mean_box(convolution_kernel, radius_x=radius_x, radius_y=radius_y, radius_z=radius_z)

    parameters = {
        "src1": source,
        "mean_src1": source_mean,
        "src2": convolution_kernel,
        "mean_src2": kernel_mean,
        "dst": destination,
    }

    execute(__file__, 'cross_correlation.cl',
                'cross_correlation', destination.shape, parameters)
    return destination
