import numpy as np
import transforms3d

class AffineTransform3D:
    """

    Inspired by: https://github.com/imglib/imglib2-realtransform/blob/master/src/main/java/net/imglib2/realtransform/AffineTransform3D.java

    """

    def __init__(self, transform_as_string : str = None):
        self._matrix = transforms3d.zooms.zfdir2aff(1)


    def scale(self, scale_x: float = None, scale_y: float = None, scale_z: float = None):
        """
        Scaling the current affine transform matrix.
        """
        if scale_x is not None:
            self._concatenate(transforms3d.zooms.zfdir2aff(scale_x, direction=(1, 0, 0), origin=(0, 0, 0)))
        if scale_y is not None:
            self._concatenate(transforms3d.zooms.zfdir2aff(scale_y, direction=(0, 1, 0), origin=(0, 0, 0)))
        if scale_z is not None:
            self._concatenate(transforms3d.zooms.zfdir2aff(scale_z, direction=(0, 0, 1), origin=(0, 0, 0)))

        return self

    def rotate(self, axis : int = 2, angle_in_rad : float = 0):
        """
        Rotation around a given axis (default: z-axis, meaning rotation in x-y-plane)

        Parameters
        ----------
        axis
        angle_in_rad

        Returns
        -------

        """
        if axis == 0:
            self._concatenate(self._3x3_to_4x4(transforms3d.euler.euler2axangle(angle_in_rad, 0, 0)))
        if axis == 1:
            self._concatenate(self._3x3_to_4x4(transforms3d.euler.euler2axangle(0, angle_in_rad, 0)))
        if axis == 2:
            self._concatenate(self._3x3_to_4x4(transforms3d.euler.euler2mat(0, 0, angle_in_rad)))

        return self

    def translate(self, translate_x: float = 0, translate_y: float = 0, translate_z : float = 0):
        self._concatenate(np.asarray([
            [1, 0, 0, translate_x],
            [0, 1, 0, translate_y],
            [0, 0, 1, translate_z],
            [0, 0, 0, 1],
        ]))
        return self

    def shear(self):
        raise NotImplementedError("Shearing has not been implemented yet. \n"
                                  "See https://github.com/clEsperanto/pyclesperanto_prototype/issues/90")

    def _3x3_to_4x4(self, matrix):
        # I bet there is an easier way to do this.
        # But I don't know what to google for :D
        #                            haesleinhuepf
        return np.asarray([
            [matrix[0,0], matrix[0,1], matrix[0,2], 0],
            [matrix[1,0], matrix[1,1], matrix[1,2], 0],
            [matrix[2,0], matrix[2,1], matrix[2,2], 0],
            [0, 0, 0, 1]
        ])

    def _concatenate(self, matrix):
        self._matrix = np.matmul(matrix, self._matrix)

    def inverse(self):
        self._matrix = np.linalg.inv(self._matrix)
        return self

    def copy(self):
        a_copy = AffineTransform3D()
        a_copy._matrix = np.copy(self._matrix)
        return a_copy

    def __array__(self):
        return self._matrix
