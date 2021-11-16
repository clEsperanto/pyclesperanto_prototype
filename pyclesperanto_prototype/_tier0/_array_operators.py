import numpy as np

cl_buffer_datatype_dict = {
    np.bool: "bool",
    np.uint8: "uchar",
    np.uint16: "ushort",
    np.uint32: "uint",
    np.uint64: "ulong",
    np.int8: "char",
    np.int16: "short",
    np.int32: "int",
    np.int64: "long",
    np.float32: "float",
    np.complex64: "cfloat_t",
    int: "int",
    float: "float",
    np.float64: "float",
}

_supported_numeric_types = tuple(cl_buffer_datatype_dict.keys())

class ArrayOperators():
    def min(self, axis=None, out=None):
        from .._tier2 import minimum_of_all_pixels
        from .._tier1 import minimum_x_projection
        from .._tier1 import minimum_y_projection
        from .._tier1 import minimum_z_projection

        if axis==0:
            result = minimum_z_projection(self)
        elif axis==1:
            result = minimum_y_projection(self)
        elif axis==2:
            result = minimum_x_projection(self)
        elif axis is None:
            result = minimum_of_all_pixels(self)
        else:
            raise ValueError("Axis " + axis + " not supported")
        if out is not None:
            np.copyto(out, result.get().astype(out.dtype))
        return result

    def max(self, axis=None, out=None):
        from .._tier2 import maximum_of_all_pixels
        from .._tier1 import maximum_x_projection
        from .._tier1 import maximum_y_projection
        from .._tier1 import maximum_z_projection

        if axis==0:
            result = maximum_z_projection(self)
        elif axis==1:
            result = maximum_y_projection(self)
        elif axis==2:
            result = maximum_x_projection(self)
        elif axis is None:
            result = maximum_of_all_pixels(self)
        else:
            raise ValueError("Axis " + axis + " not supported")
        if out is not None:
            np.copyto(out, result.get().astype(out.dtype))
        return result

    def sum(self, axis=None, out=None):
        from .._tier2 import sum_of_all_pixels
        from .._tier1 import sum_x_projection
        from .._tier1 import sum_y_projection
        from .._tier1 import sum_z_projection

        if axis==0:
            result = sum_z_projection(self)
        elif axis==1:
            result = sum_y_projection(self)
        elif axis==2:
            result = sum_x_projection(self)
        elif axis is None:
            result = sum_of_all_pixels(self)
        else:
            raise ValueError("Axis " + axis + " not supported")
        if out is not None:
            np.copyto(out, result.get().astype(out.dtype))
        return result

    # TODO: Not sure if the following are necessary / could be circumvented.
    #       For now tests fail if we remove them.
    def __iadd__(x1, x2):
        from .._tier1 import copy
        temp = copy(x1)
        if isinstance(x2, _supported_numeric_types) :
            from .._tier1 import add_image_and_scalar
            return add_image_and_scalar(temp, x1, scalar=x2)
        else:
            from .._tier1 import add_images_weighted
            return add_images_weighted(temp, x2, x1)

    def __sub__(x1, x2):
        if isinstance(x2, _supported_numeric_types):
            from .._tier1 import add_image_and_scalar
            return add_image_and_scalar(x1, scalar=-x2)
        else:
            from .._tier1 import add_images_weighted
            return add_images_weighted(x1, x2, factor2=-1)

    def __div__(x1, x2):
        if isinstance(x2, _supported_numeric_types):
            from .._tier1 import multiply_image_and_scalar
            return multiply_image_and_scalar(x1, scalar=1.0 / x2)
        else:
            from .._tier1 import divide_images
            return divide_images(x1, x2)
    def __truediv__(x1, x2):
        return x1.__div__(x2)

    def __idiv__(x1, x2):
        from .._tier1 import copy
        temp = copy(x1)
        if isinstance(x2, _supported_numeric_types):
            from .._tier1 import multiply_image_and_scalar
            return multiply_image_and_scalar(temp, x1, scalar=1.0 / x2)
        else:
            from .._tier1 import divide_images
            return divide_images(temp, x2, x1)

    def __itruediv__(x1, x2):
        return x1.__idiv__(x2)

    def __mul__(x1, x2):
        if isinstance(x2, _supported_numeric_types):
            from .._tier1 import multiply_image_and_scalar
            return multiply_image_and_scalar(x1, scalar=x2)
        else:
            from .._tier1 import multiply_images
            return multiply_images(x1, x2)

    def __imul__(x1, x2):
        from .._tier1 import copy
        temp = copy(x1)
        if isinstance(x2, _supported_numeric_types):
            from .._tier1 import multiply_image_and_scalar
            return multiply_image_and_scalar(temp, x1, scalar=x2)
        else:
            from .._tier1 import multiply_images
            return multiply_images(temp, x2, x1)

    def __gt__(x1, x2):
        if isinstance(x2, _supported_numeric_types):
            from .._tier1 import greater_constant
            return greater_constant(x1, constant=x2)
        else:
            from .._tier1 import greater
            return greater(x1, x2)

    def __ge__(x1, x2):
        if isinstance(x2, _supported_numeric_types):
            from .._tier1 import greater_or_equal_constant
            return greater_or_equal_constant(x1, constant=x2)
        else:
            from .._tier1 import greater_or_equal
            return greater_or_equal(x1, x2)

    def __lt__(x1, x2):
        if isinstance(x2, _supported_numeric_types):
            from .._tier1 import smaller_constant
            return smaller_constant(x1, constant=x2)
        else:
            from .._tier1 import smaller
            return smaller(x1, x2)

    def __le__(x1, x2):
        if isinstance(x2, _supported_numeric_types):
            from .._tier1 import smaller_or_equal_constant
            return smaller_or_equal_constant(x1, constant=x2)
        else:
            from .._tier1 import smaller_or_equal
            return smaller_or_equal(x1, x2)

    def __eq__(x1, x2):
        if isinstance(x2, _supported_numeric_types):
            from .._tier1 import equal_constant
            return equal_constant(x1, constant=x2)
        else:
            from .._tier1 import equal
            return equal(x1, x2)

    def __ne__(x1, x2):
        if isinstance(x2, _supported_numeric_types):
            from .._tier1 import not_equal_constant
            return not_equal_constant(x1, constant=x2)
        else:
            from .._tier1 import not_equal
            return not_equal(x1, x2)

    def __pow__(x1, x2):
        if isinstance(x2, _supported_numeric_types):
            from .._tier1 import power
            return power(x1, exponent=x2)
        else:
            from .._tier1 import power_images
            return power_images(x1, x2)

    def __ipow__(x1, x2):
        from .._tier1 import copy
        temp = copy(x1)
        if isinstance(x2, _supported_numeric_types):
            from .._tier1 import power
            return power(temp, x1, exponent=x2)
        else:
            from .._tier1 import power_images
            return power_images(temp, x2, x1)

    def __setitem__(self, index, value):
        if isinstance(index, list):
            index = tuple(index)
        if isinstance(index, (tuple, np.ndarray)) and index[0] is not None and isinstance(index[0], (tuple, list, np.ndarray)):
            if len(index) == len(self.shape):
                if len(index[0]) > 0:
                    # switch xy in 2D / xz in 3D, because clesperanto expects an X-Y-Z array;
                    # see also https://github.com/clEsperanto/pyclesperanto_prototype/issues/49
                    index = list(index)
                    index[0], index[-1] = index[-1], index[0]
                    # send coordinates to GPU
                    from ._push import push
                    coordinates = push(np.asarray(index))
                    num_coordinates = coordinates.shape[-1]
                    if isinstance(value, (int, float)):
                        # make an array containing new values for every pixel
                        number = value
                        from ._create import create
                        value = create((1, 1, num_coordinates))
                        from .._tier1 import set
                        set(value, number)
                    # overwrite pixels
                    from .._tier1 import write_values_to_positions
                    from .._tier2 import combine_vertically
                    values_and_positions = combine_vertically(coordinates, value)
                    write_values_to_positions(values_and_positions, self)
                return
        return super().__setitem__(index, value)

    def __getitem__(self, index):
        result = None
        if isinstance(index, list):
            index = tuple(index)
        if isinstance(index, (tuple, np.ndarray)) and index[0] is not None and isinstance(index[0], (tuple, list, np.ndarray)):
            if len(index) == len(self.shape):
                if len(index[0]) > 0:
                    # switch xy in 2D / xz in 3D, because clesperanto expects an X-Y-Z array;
                    # see also https://github.com/clEsperanto/pyclesperanto_prototype/issues/49
                    index = list(index)
                    index[0], index[-1] = index[-1], index[0]
                    # send coordinates to GPU
                    from ._push import push
                    coordinates = push(np.asarray(index))
                    # read values from positions
                    from .._tier1 import read_intensities_from_positions
                    result = read_intensities_from_positions(coordinates, self)
                else:
                    return []

        if result is None:
            if hasattr(super(), "__getitem__"):
                result = super().__getitem__(index)
            else:
                result = self.get().__getitem__(index)

        if result.size == 1 and isinstance(result, (ArrayOperators)):
            result = result.get()
        return result
