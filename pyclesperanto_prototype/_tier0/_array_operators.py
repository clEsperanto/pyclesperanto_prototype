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
            if isinstance(index, tuple):
                if any(x is Ellipsis for x in index):
                    # handle img[1, ..., 1] or img[1, ...]
                    new_index = []
                    for x in index:
                        if x is Ellipsis:
                            print(len(self.shape), len(index), "lens")
                            for i in range(len(self.shape) - len(index) + 1):
                                new_index.append(slice(None, None, None))
                        else:
                            new_index.append(x)
                    index = tuple(new_index)

                if any(isinstance(x, slice) for x in index):
                    if len(self.shape) > 2:  # 3D image
                        if len(index) > 2:
                            x_range = index[2]
                        else:
                            x_range = slice(None, None, None)

                        if len(index) > 1:
                            y_range = index[1]
                        else:
                            y_range = slice(None, None, None)

                        if len(index) > 0:
                            z_range = index[0]
                        else:
                            z_range = slice(None, None, None)
                    else:
                        if len(index) > 1:
                            x_range = index[1]
                        else:
                            x_range = slice(None, None, None)

                        if len(index) > 0:
                            y_range = index[0]
                        else:
                            y_range = slice(None, None, None)

                        z_range = slice(None, None, None)

                    if x_range is None:
                        x_range = slice(None, None, None)
                    if y_range is None:
                        y_range = slice(None, None, None)
                    if z_range is None:
                        z_range = slice(None, None, None)

                    eliminate_x = False
                    eliminate_y = False
                    eliminate_z = False
                    if not isinstance(x_range, slice) and np.issubdtype(type(x_range), np.integer):
                        x_range = slice(x_range, x_range + 1, 1)
                        eliminate_x = True
                    if not isinstance(y_range, slice) and np.issubdtype(type(y_range), np.integer):
                        y_range = slice(y_range, y_range + 1, 1)
                        eliminate_y = True
                    if not isinstance(z_range, slice) and np.issubdtype(type(z_range), np.integer):
                        z_range = slice(z_range, z_range + 1, 1)
                        eliminate_z = True

                    from .._tier1 import range as arange
                    result = arange(self, start_x=x_range.start, stop_x=x_range.stop, step_x=x_range.step,
                                   start_y=y_range.start, stop_y=y_range.stop, step_y=y_range.step,
                                   start_z=z_range.start, stop_z=z_range.stop, step_z=z_range.step)

                    if (eliminate_x * 1) + (eliminate_y * 1) + (eliminate_z * 1) <= 1:
                        from .._tier0 import create
                        from .._tier1 import copy_slice, copy_vertical_slice, copy_horizontal_slice, copy
                        if eliminate_x:
                            output = create(result.shape[:2], self.dtype)
                            result = copy_vertical_slice(result, output)
                        if eliminate_y:
                            output = create((result.shape[0],result.shape[2]), self.dtype)
                            result = copy_horizontal_slice(result, output)
                        if eliminate_z:
                            output = create(result.shape[1:], self.dtype)
                            result = copy_slice(result, output)
                    else:
                        from .._tier0 import push, pull
                        # todo: this is a necessary workaround because we can't handle 1d-arrays in pyclesperanto yet
                        result = push(pull(self).__getitem__(index))

        if result is None:

            if hasattr(super(), "__getitem__"):
                result = super().__getitem__(index)
            else:
                result = self.get().__getitem__(index)

        if result.size == 1 and isinstance(result, (ArrayOperators)):
            result = result.get()
        return result

    # adapted from https://github.com/napari/napari/blob/d6bc683b019c4a3a3c6e936526e29bbd59cca2f4/napari/utils/notebook_display.py#L54-L73
    def _plt_to_png(self):
        """PNG representation of the image object for IPython.
        Returns
        -------
        In memory binary stream containing a PNG matplotlib image.
        """
        import matplotlib.pyplot as plt
        from io import BytesIO

        with BytesIO() as file_obj:
            plt.savefig(file_obj, format='png')
            plt.close() # supress plot output
            file_obj.seek(0)
            png = file_obj.read()
        return png


    def _png_to_html(self, png):
        import base64
        url = 'data:image/png;base64,' + base64.b64encode(png).decode('utf-8')
        return f'<img src="{url}"></img>'


    def _repr_html_(self):
        """HTML representation of the image object for IPython.
        Returns
        -------
        HTML text with the image and some properties.
        """

        import numpy as np
        import matplotlib.pyplot as plt
        from .._tier9 import imshow

        labels = (self.dtype == np.uint32)

        if len(self.shape) in (2, 3):
            import matplotlib.pyplot as plt
            imshow(self,
                   labels=labels,
                   continue_drawing=True,
                   colorbar=not labels)
            image = self._png_to_html(self._plt_to_png())
        else:
            image = "<pre>" + str(self) + "</pre>"

        size_in_pixels = np.prod(self.shape)
        size_in_bytes = size_in_pixels * self.dtype.itemsize

        if size_in_bytes > 1024:
            size_in_bytes = size_in_bytes / 1024
            if size_in_bytes > 1024:
                size_in_bytes = size_in_bytes / 1024
                if size_in_bytes > 1024:
                    size_in_bytes = size_in_bytes / 1024
                    size = "{:.1f}".format(size_in_bytes) + " GB"
                else:
                    size = "{:.1f}".format(size_in_bytes) + " MB"
            else:
                size = "{:.1f}".format(size_in_bytes) + " kB"
        else:
            size = "{:.1f}".format(size_in_bytes) + " B"

        if size_in_bytes < 100 * 1024 * 1024 and not labels:

            import numpy as np
            from .._tier2 import minimum_of_all_pixels, maximum_of_all_pixels
            from .._tier3 import histogram

            num_bins = 32

            h = np.asarray(histogram(self, num_bins=num_bins))

            plt.figure(figsize=(1.8, 1.2))
            plt.bar(range(0, len(h)), h)

            # hide axis text
            # https://stackoverflow.com/questions/2176424/hiding-axis-text-in-matplotlib-plots
            frame1 = plt.gca()
            frame1.axes.xaxis.set_ticklabels([])
            frame1.axes.yaxis.set_ticklabels([])

            histogram = self._png_to_html(self._plt_to_png())

        else:
            histogram = ""

        if size_in_pixels < 100:
            data = "<pre>" + str(self) + "</pre>"
        else:
            data = ""

        all = [
            "<table>",
            "<tr>",
            "<td>",
            image,
            "</td>",
            "<td style=\"text-align: left; vertical-align: top;\">",
            "<b><a href=\"https://github.com/clEsperanto/pyclesperanto_prototype\" target=\"_blank\">cle._</a> image</b><br/>",
            "<table>",
            "<tr><td>shape</td><td>" + str(self.shape).replace(" ", "&nbsp;") + "</td></tr>",
            "<tr><td>dtype</td><td>" + str(self.dtype) + "</td></tr>",
            "<tr><td>size</td><td>" + size + "</td></tr>",
            "</table>",
            histogram,
            "</td>",
            "</tr>",
            "</table>",
            data,
        ]

        return "\n".join(all)
