# Author: Robert Haase adapted work from Aaftab Munshi, Benedict Gaster, Timothy Mattson, James Fung, Dan Ginsburg
#                adapted code from
#                https://github.com/bgaster/opencl-book-samples/blob/master/src/Chapter_14/histogram/histogram_image.cl
#
#                It was published unter BSD license according to
#                https://code.google.com/archive/p/opencl-book-samples/
#
#                Book:      OpenCL(R) Programming Guide
#                Authors:   Aaftab Munshi, Benedict Gaster, Timothy Mattson, James Fung, Dan Ginsburg
#                ISBN-10:   0-321-74964-2
#                ISBN-13:   978-0-321-74964-2
#                Publisher: Addison-Wesley Professional
#                URLs:      http://safari.informit.com/9780132488006/
#                           http://www.openclprogrammingguide.com
from .._tier0 import execute
from .._tier0 import create
from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier2 import minimum_of_all_pixels
from .._tier2 import maximum_of_all_pixels
from .._tier1 import sum_z_projection
from .._tier1 import copy_slice

@plugin_function
def histogram(image : Image, hist : Image = None, num_bins = 256, minimum_intensity : float = None, maximum_intensity : float = None, determine_min_max : bool = True):
    """
    documentation placeholder
    """

    # workaround for 2D images; the 2D kernel doesn't work as
    # in Java (global_id starts a 1 instead of 0, only tested
    # on AMD Ryzen 4700U, Vega 7)
    # thus, we copy the 2D image in a 3D stack with one slice
    if (len(image.shape) == 2):
        temp = image
        image =create([1, temp.shape[0], temp.shape[1]])
        copy_slice(temp, image, 0)


    if minimum_intensity is None or maximum_intensity is None or determine_min_max:
        minimum_intensity = minimum_of_all_pixels(image)
        maximum_intensity = maximum_of_all_pixels(image)

    number_of_partial_histograms = image.shape[-2]

    # determine multiple histograms. one for each Y (row) in the image
    partial_histograms = create([number_of_partial_histograms, 1, num_bins])

    parameters = {
        "src":image,
        "dst_histogram":partial_histograms,
        "minimum": float(minimum_intensity),
        "maximum": float(maximum_intensity),
        "step_size_x": int(1),
        "step_size_y": int(1),
        "step_size_z": int(1)
    }

    constants = {
        "NUMBER_OF_HISTOGRAM_BINS":num_bins
    }

    global_sizes = [number_of_partial_histograms]
    execute(__file__,
                "histogram_" + str(len(image.shape)) + "d_x.cl",
                "histogram_" + str(len(image.shape)) + "d",
                global_sizes,
                parameters,
                constants=constants)

    # sum partial histograms
    if hist is None:
        hist = create([num_bins, 1, 1])

    sum_z_projection(partial_histograms, hist)

    return hist

