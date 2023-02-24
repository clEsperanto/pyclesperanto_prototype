from pathlib import Path

import pyclesperanto_prototype as cle
import numpy as np

def test_exclude_labels_on_edges_2d():
    
    gpu_input = cle.push(np.asarray([

            [0, 0, 2, 0, 0, 0, 0],
            [0, 1, 2, 0, 7, 0, 0],
            [0, 1, 0, 0, 7, 5, 5],
            [8, 8, 8, 0, 0, 0, 0],
            [0, 4, 4, 0, 3, 0, 0],
            [0, 4, 4, 6, 0, 0, 0],

    ]))

    gpu_reference = cle.push(np.asarray([

            [0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 3, 0, 0],
            [0, 1, 0, 0, 3, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],

    ]))

    gpu_output = cle.exclude_labels_on_edges(gpu_input)

    a = cle.pull(gpu_output)
    b = cle.pull(gpu_reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))

def test_exclude_labels_on_edges_3d():
    gpu_input = cle.push(np.asarray([
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 9, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
        ],[
            [0, 0, 2, 0, 0, 0, 0],
            [0, 1, 2, 0, 7, 0, 0],
            [0, 1, 0, 0, 7, 5, 5],
            [8, 8, 8, 0, 0, 0, 0],
            [0, 4, 4, 9, 3, 0, 0],
            [0, 4, 4, 6, 0, 0, 0],
        ],[
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 7, 0, 0],
            [0, 0, 0, 0, 7, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
        ]
    ]))

    gpu_reference = cle.push(np.asarray([
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
        ],[
            [0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
        ],[
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
        ]
    ]))

    gpu_output = cle.exclude_labels_on_edges(gpu_input)

    a = cle.pull(gpu_output)
    b = cle.pull(gpu_reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))


def test_exclude_labels_on_edges_blobs():
    import pyclesperanto_prototype as cle

    from skimage.io import imread, imsave

    # initialize GPU
    cle.select_device("GTX")
    print("Used GPU: " + cle.get_device().name)

    # load data
    root = Path(cle.__file__).parent
    filename = str(root / '..' / 'data' / 'blobs.tif')
    image = imread(filename)
    print("Loaded image size: " + str(image.shape))

    # push image to GPU memory
    input = cle.push(image)
    print("Image size in GPU: " + str(input.shape))

    # process the image
    blurred = cle.gaussian_blur(image, sigma_x=1, sigma_y=1)
    binary = cle.threshold_otsu(blurred)
    labeled = cle.connected_components_labeling_box(binary)

    wo_edges = cle.exclude_labels_on_edges(labeled)

    # The maxmium intensity in a label image corresponds to the number of objects
    num_labels = cle.maximum_of_all_pixels(wo_edges)

    # print out result
    print("Num objects in the image: " + str(num_labels))

    assert num_labels == 44

def test_exclude_labels_on_edges_blobs_2():
    import pyclesperanto_prototype as cle

    from skimage.io import imread, imsave

    # initialize GPU
    cle.select_device("GTX")
    print("Used GPU: " + cle.get_device().name)

    # load data
    root = Path(cle.__file__).parent
    filename = str(root / '..' / 'data' / 'blobs.tif')
    image = imread(filename)
    print("Loaded image size: " + str(image.shape))

    # push image to GPU memory
    input = cle.push(image)
    print("Image size in GPU: " + str(input.shape))

    # process the image
    blurred = cle.gaussian_blur(image, sigma_x=1, sigma_y=1)
    binary = cle.threshold_otsu(blurred)
    labeled = cle.connected_components_labeling_box(binary)

    wo_edges = cle.exclude_labels_on_edges(labeled, exlude_in_y=False)

    # The maxmium intensity in a label image corresponds to the number of objects
    num_labels = cle.maximum_of_all_pixels(wo_edges)

    # print out result
    print("Num objects in the image: " + str(num_labels))

    assert num_labels == 52

    wo_edges = cle.exclude_labels_on_edges(labeled, exlude_in_x=False)

    # The maxmium intensity in a label image corresponds to the number of objects
    num_labels = cle.maximum_of_all_pixels(wo_edges)

    # print out result
    print("Num objects in the image: " + str(num_labels))

    assert num_labels == 53
