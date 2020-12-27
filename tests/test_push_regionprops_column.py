import pyclesperanto_prototype as cle
import numpy as np

def test_statistics_of_background_and_labelled_pixels2():
    labels = cle.push_zyx(np.asarray([
        [
            [4, 4, 2],
        ], [
            [4, 1, 2],
        ], [
            [3, 3, 4]
        ]
    ]))
    reference = [1, 2, 2, 4]

    regionprops = cle.statistics_of_background_and_labelled_pixels(None, labels)
    areas = cle.push_regionprops_column(regionprops, 'area')

    print(reference)
    print(areas)

    assert np.array_equal(reference, areas)


