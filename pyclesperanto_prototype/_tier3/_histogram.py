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
from .._tier0 import create_none
from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier2 import minimum_of_all_pixels
from .._tier2 import maximum_of_all_pixels
from .._tier1 import sum_z_projection
from .._tier1 import copy_slice

@plugin_function(output_creator=create_none)
def histogram(source : Image, destination : Image = None, num_bins = 256, minimum_intensity : float = None, maximum_intensity : float = None, determine_min_max : bool = True):
    """Determines the histogram of a given image.
    
    The histogram image is of dimensions number_of_bins/1/1; a 3D image with 
    height=1 and depth=1. 
    Histogram bins contain the number of pixels with intensity in this corresponding 
    bin. 
    The histogram bins are uniformly distributed between given minimum and 
    maximum grey value intensity. 
    If the flag determine_min_max is set, minimum and maximum intensity will 
    be determined. 
    When calling this operation many times, it is recommended to determine 
    minimum and maximum intensity 
    once at the beginning and handing over these values. 
    
    Author(s): Robert Haase adapted work from Aaftab Munshi, Benedict Gaster, Timothy Mattson, James Fung, Dan Ginsburg
    
    License: // adapted code from
    // https://github.com/bgaster/opencl-book-samples/blob/master/src/Chapter_14/histogram/histogram_image.cl
    //
    // It was published unter BSD license according to
    // https://code.google.com/archive/p/opencl-book-samples/
    //
    // Book:      OpenCL(R) Programming Guide
    // Authors:   Aaftab Munshi, Benedict Gaster, Timothy Mattson, James Fung, Dan Ginsburg
    // ISBN-10:   0-321-74964-2
    // ISBN-13:   978-0-321-74964-2
    // Publisher: Addison-Wesley Professional
    // URLs:      http://safari.informit.com/9780132488006/
    //            http://www.openclprogrammingguide.com
    
    Parameters
    ----------
    source : Image
    destination : Image
    number_of_bins : Number
    minimum_intensity : Number
    maximum_intensity : Number
    determine_min_max : Boolean
    
    Returns
    -------
    destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.histogram(source, destination, number_of_bins, minimum_intensity, maximum_intensity, determine_min_max)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_histogram
    """
    image_to_process = source

    # workaround for 2D images; the 2D kernel doesn't work as
    # in Java (global_id starts a 1 instead of 0, only tested
    # on AMD Ryzen 4700U, Vega 7)
    # thus, we copy the 2D image in a 3D stack with one slice
    if (len(image_to_process.shape) == 2):
        temp = image_to_process
        image_to_process = create([1, temp.shape[0], temp.shape[1]])
        copy_slice(temp, image_to_process, 0)

    # print("image shape " + str(image_to_process.shape))
    # print(str(pull(image_to_process)[0]))

    if minimum_intensity is None or maximum_intensity is None or determine_min_max:
        minimum_intensity = minimum_of_all_pixels(source)
        maximum_intensity = maximum_of_all_pixels(source)

    number_of_partial_histograms = source.shape[-2]

    # determine multiple histograms. one for each Y (row) in the image
    partial_histograms = create([number_of_partial_histograms, 1, num_bins])

    parameters = {
        "src":image_to_process,
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
                "../clij-opencl-kernels/kernels/histogram_" + str(len(image_to_process.shape)) + "d_x.cl",
                "histogram_" + str(len(image_to_process.shape)) + "d",
                global_sizes,
                parameters,
                constants=constants)

    # sum partial histograms
    if destination is None:
        destination = create([num_bins])

    sum_z_projection(partial_histograms, destination)

    return destination

