import pyclesperanto_prototype as cle
import numpy as np

def test_crop():
    test1 = cle.push(np.asarray([
        [0, 0, 0, 1],
        [0, 0, 3, 1],
        [0, 0, 3, 1],
        [1, 1, 1, 1]
    ]))

    reference = cle.push(np.asarray([
        [0, 0, 0],
        [0, 0, 3],
        [0, 0, 3]
    ]))

    result = cle.create(reference)
    cle.crop(test1, result, 0, 0)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    assert (np.array_equal(a, b))

def test_crop_2d():
    input_image = cle.create([100, 100])
    print(input_image.shape)

    output_image = cle.crop(input_image, width=10, height=10)

    print(output_image.shape)
    assert(len(output_image.shape) == 2)
    assert(output_image.shape[0] == 10)
    assert(output_image.shape[1] == 10)

def test_crop_3d():
    input_image = cle.create([100, 100, 100])
    print(input_image.shape)

    output_image = cle.crop(input_image, width=10, height=10, depth=10)

    print(output_image.shape)
    assert(len(output_image.shape) == 3)
    assert(output_image.shape[0] == 10)
    assert(output_image.shape[1] == 10)
    assert(output_image.shape[2] == 10)
