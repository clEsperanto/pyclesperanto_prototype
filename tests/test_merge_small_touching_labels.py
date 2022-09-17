def test_merge_small_touching_labels():
    import pyclesperanto_prototype as cle
    import numpy as np

    labels = cle.scale(cle.asarray([
        [1, 1, 1, 2, 2, 2],
        [1, 1, 1, 2, 2, 2],
        [1, 1, 5, 6, 2, 2],
        [4, 4, 5, 7, 3, 3],
        [4, 4, 4, 3, 3, 3],
        [4, 4, 4, 3, 3, 3],
    ]), factor_x=10, factor_y=10, auto_size=True).astype(np.uint32)

    result1 = cle.merge_small_touching_labels(labels, maximum_pixel_count=200)
    result2 = cle.merge_small_touching_labels(labels, maximum_pixel_count=400)

    assert result1.max() == 6
    assert result2.max() == 5
