import pyclesperanto_prototype as cle
import numpy as np

def test_connected_components_labeling_box():
    
    gpu_input = cle.push(np.asarray([
        [
            [1, 0, 1],
            [1, 0, 0],
            [0, 0, 1]
        ]
    ]))

    gpu_reference = cle.push(np.asarray([
        [
            [1, 0, 2],
            [1, 0, 0],
            [0, 0, 3]
        ]
    ]))

    gpu_output = cle.connected_components_labeling_box(gpu_input)

    a = cle.pull(gpu_output)
    b = cle.pull(gpu_reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))

def test_connected_components_labeling_box_blobs():
    import pyclesperanto_prototype as cle

    from skimage.io import imread, imsave

    # initialize GPU
    cle.select_device("GTX")
    print("Used GPU: " + cle.get_device().name)

    # load data
    image = imread('https://imagej.nih.gov/ij/images/blobs.gif')
    print("Loaded image size: " + str(image.shape))

    # push image to GPU memory
    input = cle.push(image)
    print("Image size in GPU: " + str(input.shape))

    # process the image
    inverted = cle.subtract_image_from_scalar(image, scalar=255)
    blurred = cle.gaussian_blur(inverted, sigma_x=1, sigma_y=1)
    binary = cle.threshold_otsu(blurred)
    labeled = cle.connected_components_labeling_box(binary)

    # The maxmium intensity in a label image corresponds to the number of objects
    num_labels = cle.maximum_of_all_pixels(labeled)

    # print out result
    print("Num objects in the image: " + str(num_labels))

    assert num_labels == 63