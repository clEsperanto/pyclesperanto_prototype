def test_add():
    import numpy as np
    import pyclesperanto_prototype as cle

    input1 =    cle.push(np.asarray([[1, 2, 3]]))
    input2 =    cle.push(np.asarray([[4, 5, 6]]))
    reference = cle.push(np.asarray([[5, 7, 9]]))

    output = input1 + input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)

def test_add_with_scalar():
    import numpy as np
    import pyclesperanto_prototype as cle

    input1 =    cle.push(np.asarray([[1, 2, 3]]))
    input2 =    5
    reference = cle.push(np.asarray([[6, 7, 8]]))

    output = input1 + input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)

def test_add_with_np():
    import numpy as np
    import pyclesperanto_prototype as cle

    input1 =    cle.push(np.asarray([[4, 2, -8]]))
    input2 =             np.asarray([[2, 2, 2]])
    reference = cle.push(np.asarray([[6, 4, -6]]))

    output = input1 + input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)

def test_subtract():
    import numpy as np
    import pyclesperanto_prototype as cle

    input1 =    cle.push(np.asarray([[4, 2, 3]]))
    input2 =    cle.push(np.asarray([[1, 5, 6]]))
    reference = cle.push(np.asarray([[3, -3, -3]]))

    output = input1 - input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)

def test_subtract_with_scalar():
    import numpy as np
    import pyclesperanto_prototype as cle

    input1 =    cle.push(np.asarray([[4, 2, 3]]))
    input2 =    5
    reference = cle.push(np.asarray([[-1, -3, -2]]))

    output = input1 - input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)

def test_subtract_with_np():
    import numpy as np
    import pyclesperanto_prototype as cle

    input1 =    cle.push(np.asarray([[4, 2, 3]]))
    input2 =             np.asarray([[1, 5, 6]])
    reference = cle.push(np.asarray([[3, -3, -3]]))

    output = input1 - input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)

def test_divide():
    import numpy as np
    import pyclesperanto_prototype as cle

    input1 =    cle.push(np.asarray([[4, 2, -8]]))
    input2 =    cle.push(np.asarray([[2, 2, 2]]))
    reference = cle.push(np.asarray([[2, 1, -4]]))

    output = input1 / input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)



def test_divide_with_scalar():
    import numpy as np
    import pyclesperanto_prototype as cle

    input1 =    cle.push(np.asarray([[4, 2, -8]]))
    input2 =    2
    reference = cle.push(np.asarray([[2, 1, -4]]))

    output = input1 / input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)

def test_divide_with_np():
    import numpy as np
    import pyclesperanto_prototype as cle

    input1 =    cle.push(np.asarray([[4, 2, -8]]))
    input2 =             np.asarray([[2, 2, 2]])
    reference = cle.push(np.asarray([[2, 1, -4]]))

    output = input1 / input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)

def test_multiply():
    import numpy as np
    import pyclesperanto_prototype as cle

    input1 =    cle.push(np.asarray([[4, 2, -8]]))
    input2 =    cle.push(np.asarray([[2, 2, 2]]))
    reference = cle.push(np.asarray([[8, 4, -16]]))

    output = input1 * input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)


def test_multiply_with_scalar():
    import numpy as np
    import pyclesperanto_prototype as cle

    input1 =    cle.push(np.asarray([[4, 2, -8]]))
    input2 =    2
    reference = cle.push(np.asarray([[8, 4, -16]]))

    output = input1 * input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)

def test_multiply_with_np():
    import numpy as np
    import pyclesperanto_prototype as cle

    input1 =    cle.push(np.asarray([[4, 2, -8]]))
    input2 =             np.asarray([[2, 2, 2]])
    reference = cle.push(np.asarray([[8, 4, -16]]))

    output = input1 * input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)

def test_gt():
    import numpy as np
    import pyclesperanto_prototype as cle

    input1 =    cle.push(np.asarray([[4, 2, -8]]))
    input2 =    cle.push(np.asarray([[2, 2, 2]]))
    reference = cle.push(np.asarray([[1, 0, 0]]))

    output = input1 > input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)


def test_gt_with_scalar():
    import numpy as np
    import pyclesperanto_prototype as cle

    input1 =    cle.push(np.asarray([[4, 2, -8]]))
    input2 =    2
    reference = cle.push(np.asarray([[1, 0, 0]]))

    output = input1 > input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)

def test_gt_with_np():
    import numpy as np
    import pyclesperanto_prototype as cle

    input1 =    cle.push(np.asarray([[4, 2, -8]]))
    input2 =             np.asarray([[2, 2, 2]])
    reference = cle.push(np.asarray([[1, 0, 0]]))

    output = input1 > input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)

def test_ge():
    import numpy as np
    import pyclesperanto_prototype as cle

    input1 =    cle.push(np.asarray([[4, 2, -8]]))
    input2 =    cle.push(np.asarray([[2, 2, 2]]))
    reference = cle.push(np.asarray([[1, 1, 0]]))

    output = input1 >= input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)


def test_ge_with_scalar():
    import numpy as np
    import pyclesperanto_prototype as cle

    input1 =    cle.push(np.asarray([[4, 2, -8]]))
    input2 =    2
    reference = cle.push(np.asarray([[1, 1, 0]]))

    output = input1 >= input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)

def test_ge_with_np():
    import numpy as np
    import pyclesperanto_prototype as cle

    input1 =    cle.push(np.asarray([[4, 2, -8]]))
    input2 =             np.asarray([[2, 2, 2]])
    reference = cle.push(np.asarray([[1, 1, 0]]))

    output = input1 >= input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)

def test_lt():
    import numpy as np
    import pyclesperanto_prototype as cle

    input1 =    cle.push(np.asarray([[4, 2, -8]]))
    input2 =    cle.push(np.asarray([[2, 2, 2]]))
    reference = cle.push(np.asarray([[0, 0, 1]]))

    output = input1 < input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)


def test_lt_with_scalar():
    import numpy as np
    import pyclesperanto_prototype as cle

    input1 =    cle.push(np.asarray([[4, 2, -8]]))
    input2 =    2
    reference = cle.push(np.asarray([[0, 0, 1]]))

    output = input1 < input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)

def test_lt_with_np():
    import numpy as np
    import pyclesperanto_prototype as cle

    input1 =    cle.push(np.asarray([[4, 2, -8]]))
    input2 =             np.asarray([[2, 2, 2]])
    reference = cle.push(np.asarray([[0, 0, 1]]))

    output = input1 < input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)

def test_le():
    import numpy as np
    import pyclesperanto_prototype as cle

    input1 =    cle.push(np.asarray([[4, 2, -8]]))
    input2 =    cle.push(np.asarray([[2, 2, 2]]))
    reference = cle.push(np.asarray([[0, 1, 1]]))

    output = input1 <= input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)


def test_le_with_scalar():
    import numpy as np
    import pyclesperanto_prototype as cle

    input1 =    cle.push(np.asarray([[4, 2, -8]]))
    input2 =    2
    reference = cle.push(np.asarray([[0, 1, 1]]))

    output = input1 <= input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)

def test_le_with_np():
    import numpy as np
    import pyclesperanto_prototype as cle

    input1 =    cle.push(np.asarray([[4, 2, -8]]))
    input2 =             np.asarray([[2, 2, 2]])
    reference = cle.push(np.asarray([[0, 1, 1]]))

    output = input1 <= input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)

def test_eq():
    import numpy as np
    import pyclesperanto_prototype as cle

    input1 =    cle.push(np.asarray([[4, 2, -8]]))
    input2 =    cle.push(np.asarray([[2, 2, 2]]))
    reference = cle.push(np.asarray([[0, 1, 0]]))

    output = input1 == input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)


def test_eq_with_scalar():
    import numpy as np
    import pyclesperanto_prototype as cle

    input1 =    cle.push(np.asarray([[4, 2, -8]]))
    input2 =    2
    reference = cle.push(np.asarray([[0, 1, 0]]))

    output = input1 == input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)

def test_eq_with_np():
    import numpy as np
    import pyclesperanto_prototype as cle

    input1 =    cle.push(np.asarray([[4, 2, -8]]))
    input2 =             np.asarray([[2, 2, 2]])
    reference = cle.push(np.asarray([[0, 1, 0]]))

    output = input1 == input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)

def test_ne():
    import numpy as np
    import pyclesperanto_prototype as cle

    input1 =    cle.push(np.asarray([[4, 2, -8]]))
    input2 =    cle.push(np.asarray([[2, 2, 2]]))
    reference = cle.push(np.asarray([[1, 0, 1]]))

    output = input1 != input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)


def test_ne_with_scalar():
    import numpy as np
    import pyclesperanto_prototype as cle

    input1 =    cle.push(np.asarray([[4, 2, -8]]))
    input2 =    2
    reference = cle.push(np.asarray([[1, 0, 1]]))

    output = input1 != input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)

def test_ne_with_np():
    import numpy as np
    import pyclesperanto_prototype as cle

    input1 =    cle.push(np.asarray([[4, 2, -8]]))
    input2 =             np.asarray([[2, 2, 2]])
    reference = cle.push(np.asarray([[1, 0, 1]]))

    output = input1 != input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)

def test_pos():
    import numpy as np
    import pyclesperanto_prototype as cle

    input1 =    cle.push(np.asarray([[4, 2, -8]]))
    reference = cle.push(np.asarray([[4, 2, -8]]))

    output = +input1
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)

def test_neg():
    import numpy as np
    import pyclesperanto_prototype as cle

    input1 =    cle.push(np.asarray([[4, 2, -8]]))
    reference = cle.push(np.asarray([[-4, -2, 8]]))

    output = -input1
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)