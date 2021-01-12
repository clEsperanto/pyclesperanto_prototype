import pyclesperanto_prototype as cle
import numpy as np

def test_push_regionprops_column():
    labels = cle.push(np.asarray([
        [
            [4, 4, 2],
        ], [
            [4, 1, 2],
        ], [
            [3, 3, 4]
        ]
    ]))
    reference = [0, 1, 2, 2, 4]

    regionprops = cle.statistics_of_background_and_labelled_pixels(None, labels)
    areas = cle.push_regionprops_column(regionprops, 'area')

    print(reference)
    print(areas)

    assert np.allclose(reference, areas, 0.001)


def test_push_regionprops_column_gpu():
    labels = cle.push(np.asarray([
        [
            [4, 4, 2],
        ], [
            [4, 1, 2],
        ], [
            [3, 3, 4]
        ]
    ]))
    reference = [0, 1, 2, 2, 4]

    regionprops = cle.statistics_of_background_and_labelled_pixels(None, labels)
    areas = cle.push_regionprops_column(regionprops, 'area')

    print(reference)
    print(areas)

    assert np.allclose(reference, areas, 0.0001)


