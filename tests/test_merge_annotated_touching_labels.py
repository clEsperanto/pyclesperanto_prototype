def test_merge_annotated_touching_labels():
    import pyclesperanto_prototype as cle
    from skimage.io import imread
    import numpy as np

    # load test data
    oversegmented = cle.asarray(imread('data/syntetic_cells.tif')).astype(np.uint32)
    annotation = cle.asarray(imread('data/syntetic_cells_merge_annotation.tif')).astype(np.uint32)
    reference = cle.asarray(imread('data/syntetic_cells_merged_test_result.tif')).astype(np.uint32)

    result = cle.merge_annotated_touching_labels(oversegmented, annotation == 1)

    assert cle.array_equal(reference, result)
