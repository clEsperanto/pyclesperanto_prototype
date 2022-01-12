from warnings import warn

import numpy as np
import transforms3d

class AffineTransform3D:
    """This class is a convenience class to setup affine transform matrices.
    When initialized, this object corresponds to a null transform. Afterwards,
    you can append transforms, e.g. by calling `transform.translate(10, 20)`.

    The API aims to be compatible to Imglib2 AffineTransform3D.

    Inspired by: https://github.com/imglib/imglib2-realtransform/blob/master/src/main/java/net/imglib2/realtransform/AffineTransform3D.java

    """

    def __init__(self):
        self._matrix = transforms3d.zooms.zfdir2aff(1)


    def scale(self, scale_x: float = None, scale_y: float = None, scale_z: float = None):
        """
        Scaling the current affine transform matrix.

        Parameters
        ----------
        scale_x : float
            scaling along x axis
        scale_y : float
            scaling along y axis
        scale_z : float
            scaling along z axis

        Returns
        -------
        self

        """
        if scale_x == 0:
            warn('scale_x must not be 0')
            scale_x = 1
        if scale_y == 0:
            warn('scale_y must not be 0')
            scale_y = 1
        if scale_z == 0:
            warn('scale_z must not be 0')
            scale_z = 1
        if scale_x is not None:
            self._concatenate(transforms3d.zooms.zfdir2aff(scale_x, direction=(1, 0, 0), origin=(0, 0, 0)))
        if scale_y is not None:
            self._concatenate(transforms3d.zooms.zfdir2aff(scale_y, direction=(0, 1, 0), origin=(0, 0, 0)))
        if scale_z is not None:
            self._concatenate(transforms3d.zooms.zfdir2aff(scale_z, direction=(0, 0, 1), origin=(0, 0, 0)))

        return self

    def rotate(self, axis : int = 2, angle_in_degrees : float = 0):
        """
        Rotation around a given axis (default: z-axis, meaning rotation in x-y-plane)

        Parameters
        ----------
        axis : int
            axis to rotate around (0=x, 1=y, 2=z)
        angle_in_degrees : int
            angle in degrees. To convert radians to degrees use this formula:
            angle_in_deg = angle_in_rad / numpy.pi * 180.0

        Returns
        -------
        self
        """
        angle_in_rad = angle_in_degrees * np.pi / 180.0

        if axis == 0:
            self._concatenate(self._3x3_to_4x4(transforms3d.euler.euler2mat(angle_in_rad, 0, 0)))
        if axis == 1:
            self._concatenate(self._3x3_to_4x4(transforms3d.euler.euler2mat(0, angle_in_rad, 0)))
        if axis == 2:
            self._concatenate(self._3x3_to_4x4(transforms3d.euler.euler2mat(0, 0, angle_in_rad)))

        return self

    def translate(self, translate_x: float = 0, translate_y: float = 0, translate_z : float = 0):
        """Translation along axes.

        Parameters
        ----------
        translate_x : float
            translation along x-axis
        translate_y : float
            translation along y-axis
        translate_z : float
            translation along z-axis

        Returns
        -------
        self

        """
        self._concatenate(np.asarray([
            [1, 0, 0, translate_x],
            [0, 1, 0, translate_y],
            [0, 0, 1, translate_z],
            [0, 0, 0, 1],
        ]))
        return self

    def center(self, shape, undo : bool = False):
        """Change the center of the image to the root of the coordinate system

        Parameters
        ----------
        shape : iterable
            shape of the image which should be centered
        undo : bool, optional
            if False (default), the image is moved so that the center of the image is in the root of the coordinate system
            if True, it is translated in the opposite direction

        Returns
        -------
        self

        """

        presign = 1
        if not undo:
            presign = -1

        if len(shape) == 2:
            self.translate(
                translate_x = presign * shape[1] / 2,
                translate_y = presign * shape[0] / 2
            )
        else: # 3 dimensional image
            self.translate(
                translate_x = presign * shape[2] / 2,
                translate_y = presign * shape[1] / 2,
                translate_z = presign * shape[0] / 2
            )

        return self

    def shear_z(self,angle_x_in_degrees: float = 0, angle_y_in_degrees: float = 0 ):
        """Shear image in Z along X and/or Y direction
           Uses angle in degrees to calculate the shear
           Tip: Used for lattice lightsheet deskewing. For Janelia lattice, use angle_x_in_degrees and for Zeiss lattice, use angle_y_in_degrees

        Args:
            angle_x_in_degrees (float, optional): shear angle in X in degrees. Defaults to 0.
            angle_y_in_degrees (float, optional): shear angle in Y in degrees. Defaults to 0.

        Returns:
            self
        """          
        import math
        try:
            shear_factor_xz = 1.0 / math.tan(angle_x_in_degrees * math.pi / 180)
        except ZeroDivisionError:
            shear_factor_xz = 0
        
        try:
            shear_factor_yz = 1.0 / math.tan(angle_y_in_degrees * math.pi / 180)
        except ZeroDivisionError:
            shear_factor_yz = 0

        # shearing
        self._concatenate(np.asarray([
            [1, 0, shear_factor_xz, 0],
            [0, 1, shear_factor_yz, 0],
            [0, 0 , 1, 0],
            [0, 0, 0, 1],
        ]))
        return self

    def shear_x(self,angle_y_in_degrees: float = 0, angle_z_in_degrees: float = 0 ):
        """Shear image in x along Y and/or Z direction
           Uses angle in degrees to calculate the shear

        Args:
            angle_y_in_degrees (float, optional): shear angle in X in degrees. Defaults to 0.
            angle_z_in_degrees (float, optional): shear angle in Z in degrees. Defaults to 0.

        Returns:
            self
        """        
        
        import math
        try:
            shear_factor_yx = 1.0 / math.tan(angle_y_in_degrees * math.pi / 180)
        except ZeroDivisionError:
            shear_factor_yx = 0
        
        try:
            shear_factor_zx = 1.0 / math.tan(angle_z_in_degrees * math.pi / 180)
        except ZeroDivisionError:
            shear_factor_zx = 0

        # shearing
        self._concatenate(np.asarray([
            [1, 0, 0, 0],
            [shear_factor_yx, 1, 0, 0],
            [shear_factor_zx, 0 , 1, 0],
            [0, 0, 0, 1],
        ]))
        return self

    def shear_y(self,angle_x_in_degrees: float = 0, angle_z_in_degrees: float = 0 ):
        """Shear image in Y along X and/or Z direction
           Uses angle in degrees to calculate the shear

        Args:
            angle_x_in_degrees (float, optional): shear angle in X in degrees. Defaults to 0.
            angle_z_in_degrees (float, optional): shear angle in Z in degrees. Defaults to 0.

        Returns:
            self
        """        
        
        import math
        try:
            shear_factor_xy = 1.0 / math.tan(angle_x_in_degrees * math.pi / 180)
        except ZeroDivisionError:
            shear_factor_xy = 0
        
        try:
            shear_factor_zy = 1.0 / math.tan(angle_z_in_degrees * math.pi / 180)
        except ZeroDivisionError:
            shear_factor_zy = 0

        # shearing
        self._concatenate(np.asarray([
            [1, shear_factor_xy, 0, 0],
            [0, 1, 0, 0],
            [0, shear_factor_zy , 1, 0],
            [0, 0, 0, 1],
        ]))
        return self

    def _3x3_to_4x4(self, matrix):
        """Pads 3x3 affine transformation matrix to convert it to 4x4
        """        
        mat = np.pad(matrix,(0,1),'constant', constant_values = (0,0))
        mat[3,3] = 1
        return mat

    def _concatenate(self, matrix):
        self._matrix = np.matmul(matrix, self._matrix)

    def inverse(self):
        """Computes the inverse of the transformation.

        This can be useful, e.g. when you want to know the transformation
        from image B to image A but you only know the transformation from
        A to B.

        Returns
        -------
        self

        """
        self._matrix = np.linalg.inv(self._matrix)
        return self

    def copy(self):
        """Makes a copy of the current transform which can then be
        manipulated without changing the source.

        Returns
        -------
        copy of the current transform
        """
        a_copy = AffineTransform3D()
        a_copy._matrix = np.copy(self._matrix)
        return a_copy

    def __array__(self):
        return self._matrix
