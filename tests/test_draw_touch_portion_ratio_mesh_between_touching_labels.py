import pyclesperanto_prototype as cle
import numpy as np

def test_draw_touch_portion_ratio_mesh_between_touching_labels():

    labels = cle.push(np.asarray([
        [1, 1, 3, 3, 3, 3],
        [1, 1, 3, 3, 3, 3],
        [1, 1, 3, 3, 3, 3],
        [2, 2, 2, 4, 4, 4],
        [2, 2, 2, 4, 4, 5],
        [2, 2, 2, 4, 5, 5],
    ]))

    touch_portion_ratio_mesh_between_touching_labels = cle.draw_touch_portion_ratio_mesh_between_touching_labels(labels)

    print(touch_portion_ratio_mesh_between_touching_labels)

    assert np.max(touch_portion_ratio_mesh_between_touching_labels) > 1
    assert np.min(touch_portion_ratio_mesh_between_touching_labels) == 0


