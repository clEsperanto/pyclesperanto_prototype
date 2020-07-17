from pyclesperanto_prototype import create
from pyclesperanto_prototype import create_like

def test_create_3d():
    size = [2, 3, 4]

    image = create(size)

    assert (image.shape[0] == 2)
    assert (image.shape[1] == 3)
    assert (image.shape[2] == 4)

    image2 = create_like(image)
    assert (image2.shape[0] == 2)
    assert (image2.shape[1] == 3)
    assert (image2.shape[2] == 4)

def test_create_2d():
    size = [2, 3]

    image = create(size)

    assert (image.shape[0] == 2)
    assert (image.shape[1] == 3)

    image2 = create_like(image)
    assert (image2.shape[0] == 2)
    assert (image2.shape[1] == 3)





