def test_draw_mesh_between_n_most_touching_labels():
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

    mesh1 = cle.draw_mesh_between_n_most_touching_labels(labels, n=1)
    mesh2 = cle.draw_mesh_between_n_most_touching_labels(labels, n=2)

    assert cle.sum_of_all_pixels(mesh1) > 60
    assert cle.sum_of_all_pixels(mesh1) < 70
    assert cle.sum_of_all_pixels(mesh1) == 64

    assert cle.sum_of_all_pixels(mesh1) < cle.sum_of_all_pixels(mesh2)

