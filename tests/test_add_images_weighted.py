import pyclesperanto_prototype as cle
import numpy as np

def test_add_images_weighted_missing_parameters():

    input1 = np.asarray([[1, 2, 3]])
    input2 = np.asarray([[4, 5, 6]])

    reference = np.asarray([[5, 7, 9]])
    output = cle.add_images_weighted(input1, input2)
    result = cle.pull_zyx(output)

    print(result)
    print(reference)
    assert(np.array_equal(result, reference))

def test_add_images_weighted_none_output():


    input1 = np.asarray([[1, 2, 3]])
    input2 = np.asarray([[4, 5, 6]])

    reference = np.asarray([[9, 12, 15]])
    output = cle.add_images_weighted(input1, input2, None, 1, 2)
    result = cle.pull_zyx(output)

    print(result)
    print(reference)
    assert(np.array_equal(result, reference))

def test_add_images_weighted_named_parameters():


    input1 = np.asarray([[1, 2, 3]])
    input2 = np.asarray([[4, 5, 6]])

    reference = np.asarray([[9, 12, 15]])
    output = cle.add_images_weighted(input1, input2, None, factor1=1, factor2=2)
    result = cle.pull_zyx(output)

    print(result)
    print(reference)
    assert(np.array_equal(result, reference))

def test_add_images_weighted_wrong_parameter_order():

    input1 = np.asarray([[1, 2, 3]])
    input2 = np.asarray([[4, 5, 6]])

    reference = np.asarray([[9, 12, 15]])
    output = cle.add_images_weighted(input1, input2, factor1=1, factor2=2)
    result = cle.pull_zyx(output)

    print(result)
    print(reference)
    assert(np.array_equal(result, reference))

def test_add_images_weighted_parameters_wrong_order_and_missing():

    input1 = np.asarray([[1, 2, 3]])
    input2 = np.asarray([[4, 5, 6]])

    reference = np.asarray([[9, 12, 15]])
    output = cle.add_images_weighted(input1, input2, factor2=2, factor1=1)
    result = cle.pull_zyx(output)

    print(result)
    print(reference)
    assert(np.array_equal(result, reference))
