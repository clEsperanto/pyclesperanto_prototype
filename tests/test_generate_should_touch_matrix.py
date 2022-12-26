def test_generate_should_touch_matrix():
    import pyclesperanto_prototype as cle
    from skimage.io import imread
    import numpy as np

    # load test data
    oversegmented = cle.asarray(imread('data/syntetic_cells.tif')).astype(np.uint32)
    annotation = cle.asarray(imread('data/syntetic_cells_merge_annotation.tif')).astype(np.uint32)
    reference = cle.asarray(imread('data/syntetic_cells_merged_test_result.tif')).astype(np.uint32)

    should_touch_matrix = cle.generate_should_touch_matrix(oversegmented, annotation == 1)

    result = cle.merge_labels_according_to_touch_matrix(oversegmented, should_touch_matrix)

    assert cle.array_equal(reference, result)
