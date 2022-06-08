from pyclesperanto_prototype._tier0 import Image, plugin_function, execute
from pyclesperanto_prototype._tier3 import mean_of_all_pixels
import numpy as np

@plugin_function(categories=['filter', 'combine', 'in assistant'])
def cross_correlation(source: Image, convolution_kernel: Image, destination: Image = None,
                      radius_x: float = 1, radius_y: float = 1, radius_z: float = 1) -> Image:
    source_mean = mean_of_all_pixels(source)
    kernel_mean = mean_of_all_pixels(convolution_kernel)
    source_std = np.std(source)
    kernel_std = np.std(convolution_kernel)

    # source_mean = mean_box(source, radius_x=radius_x, radius_y=radius_y, radius_z=radius_z)
    # kernel_mean = mean_box(convolution_kernel, radius_x=radius_x, radius_y=radius_y, radius_z=radius_z)

    parameters = {
        "src1": source,
        "mean_src1": source_mean,
        "std_src1": source_std,
        "src2": convolution_kernel,
        "mean_src2": kernel_mean,
        "std_src2": kernel_std,
        "dst": destination,
    }

    execute(__file__, 'cross_correlation.cl',
                'cross_correlation', destination.shape, parameters)
    return destination
