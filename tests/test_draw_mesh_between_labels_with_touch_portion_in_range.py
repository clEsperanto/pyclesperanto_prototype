def test_draw_mesh_between_labels_with_touch_portion_in_range():
    import numpy as np
    import pyclesperanto_prototype as cle

    labels = cle.asarray([
        [0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 2, 2, 0],
        [0, 1, 1, 1, 2, 2, 0],
        [0, 0, 3, 3, 3, 3, 0],
        [0, 0, 4, 4, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ])
    labels = cle.scale(labels, factor_x=10, factor_y=10, auto_size=True).astype(np.uint32)

    mesh1 = cle.draw_mesh_between_labels_with_touch_portion_in_range(labels, minimum_touch_portion=0.2)
    mesh2 = cle.draw_mesh_between_labels_with_touch_portion_in_range(labels, minimum_touch_portion=0.1)


    assert cle.sum_of_all_pixels(mesh1) > 30
    assert cle.sum_of_all_pixels(mesh1) < 40
    assert cle.sum_of_all_pixels(mesh1) == 38

    assert cle.sum_of_all_pixels(mesh1) < cle.sum_of_all_pixels(mesh2)

