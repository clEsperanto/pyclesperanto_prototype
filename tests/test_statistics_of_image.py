import pyclesperanto_prototype as cle
import numpy as np

def test_statistics_of_labelled_pixels():
    intensity = cle.push_zyx(np.asarray([
        [0, 1, 2],
        [1, 2, 3],
        [2, 3, 4]
    ]))

    props = cle.statistics_of_image(intensity, use_gpu=False)

    assert np.equal(0, props.min_intensity)
    assert np.equal(4, props.max_intensity)
    assert np.equal(2, props.mean_intensity)
    assert np.isclose(1.15, props.standard_deviation_intensity, 0.01)
