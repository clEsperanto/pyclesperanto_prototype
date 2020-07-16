import pyclesperanto_prototype as cle


import numpy as np

input1 = np.asarray([[1, 2, 3]])
input2 = np.asarray([[4, 5, 6]])


def test_add_images_weighted_missing_params():
    reference = np.asarray([[5, 7, 9]])
    output = cle.add_images_weighted(input1, input2)
    result = cle.pull(output)
    assert np.array_equal(result, reference)


reference = np.asarray([[9, 12, 15]])


def test_add_images_weighted_none_output():
    output = cle.add_images_weighted(input1, input2, None, 1, 2)
    result = cle.pull(output)
    assert np.array_equal(result, reference)


def test_add_images_weighted_named_params():
    output = cle.add_images_weighted(input1, input2, None, weight1=1, weight2=2)
    result = cle.pull(output)
    assert np.array_equal(result, reference)


def test_add_images_weighted_named_params_missing_params():
    output = cle.add_images_weighted(input1, input2, weight1=1, weight2=2)
    result = cle.pull(output)
    assert np.array_equal(result, reference)


def test_add_images_weighted_wrong_order_missing_params():
    reference = np.asarray([[9, 12, 15]])
    output = cle.add_images_weighted(input1, input2, weight2=2, weight1=1)
    result = cle.pull(output)
    assert np.array_equal(result, reference)
