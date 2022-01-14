import pyclesperanto_prototype as cle
import numpy as np

def test_shear_x():
    arr = np.zeros((5,5,5),dtype = float)
    arr[2][2][2] =1

    source = cle.push(arr)

    arr = np.zeros((5,5,5),dtype = float)
    arr[4][4][2] =1
    
    reference = cle.push(arr)

    transform = cle.AffineTransform3D()
    transform.shear_x(angle_z_in_degrees=45,angle_y_in_degrees=45)
    
    result = cle.affine_transform(source, transform=transform)
    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))

def test_shear_y():
    arr = np.zeros((5,5,5),dtype = float)
    arr[2][2][2] =1

    source = cle.push(arr)

    arr = np.zeros((5,5,5),dtype = float)
    arr[4][2][4] =1
    
    reference = cle.push(arr)

    transform = cle.AffineTransform3D()
    transform.shear_y(angle_z_in_degrees=45,angle_x_in_degrees=45)
    
    result = cle.affine_transform(source, transform=transform)
    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))

def test_shear_z():
    arr = np.zeros((5,5,5),dtype = float)
    arr[2][2][2] =1

    source = cle.push(arr)

    arr = np.zeros((5,5,5),dtype = float)
    arr[2][4][4] =1
    
    reference = cle.push(arr)

    transform = cle.AffineTransform3D()
    transform.shear_z(angle_y_in_degrees=45,angle_x_in_degrees=45)
    
    result = cle.affine_transform(source, transform=transform)
    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))
