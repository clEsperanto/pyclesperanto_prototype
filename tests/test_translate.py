import pyclesperanto_prototype as cle
import numpy as np

def test_translate():
    source = cle.push_zyx(np.asarray([[
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 1, 1, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
    ]]))

    reference = cle.push_zyx(np.asarray([[
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]]))

    result = cle.translate(source, translate_x=-1, translate_y=-1)

    a = cle.pull_zyx(result)
    b = cle.pull_zyx(reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))

