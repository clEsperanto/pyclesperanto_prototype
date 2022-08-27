import pyclesperanto_prototype as cle
import numpy as np

def test_draw_touch_portion_mesh_between_touching_labels():

    labels = cle.push(np.asarray([
        [1, 1, 3, 3, 3, 3],
        [1, 1, 3, 3, 3, 3],
        [1, 1, 3, 3, 3, 3],
        [2, 2, 2, 4, 4, 4],
        [2, 2, 2, 4, 4, 5],
        [2, 2, 2, 4, 5, 5],
    ]))

    reference = cle.push(np.asarray([
        [0.        , 0.        , 0.        , 0.        , 0.        , 0.        ],
        [0.6       , 0.6       , 0.6       , 0.6       , 0.        , 0.        ],
        [0.4       , 0.        , 0.16666667, 0.4285714 , 0.        , 0.        ],
        [0.4       , 0.5       , 0.5       , 0.5       , 0.        , 0.        ],
        [0.        , 0.5       , 0.        , 0.        , 0.4       , 0.        ],
        [0.        , 0.        , 0.        , 0.        , 0.        , 0.        ]
    ]))


    touch_portion_mesh_between_touching_labels = cle.draw_touch_portion_mesh_between_touching_labels(labels)

    print(reference)
    print(touch_portion_mesh_between_touching_labels)

    assert np.allclose(touch_portion_mesh_between_touching_labels, reference, 0.001)
