import pyclesperanto_prototype as cle
import numpy as np

def test_generate_distance_matrix():

    gpu_input = cle.push(np.asarray([

            [0, 0, 0, 0, 0],
            [0, 1, 0, 3, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 2, 0, 0],
            [0, 0, 0, 0, 4]

    ]))

    gpu_reference = cle.push(np.asarray([
            [0.,        0.   ,        0.    ,     0.    ,     0.    ],
            [0.,        0.   ,     2.236068 ,     2.    , 4.2426405 ],
            [0.,    2.236068 ,         0.   , 2.236068  , 2.236068  ],
            [0.,        2.   ,     2.236068 ,     0.    , 3.1622777 ],
            [0.,    4.2426405,     2.236068 , 3.1622777 ,     0.    ]
    ]))



    gpu_pointlist = cle.labelled_spots_to_pointlist(gpu_input)
    gpu_distance_matrix = cle.generate_distance_matrix(gpu_pointlist, gpu_pointlist)

    a = cle.pull_zyx(gpu_distance_matrix)
    b = cle.pull_zyx(gpu_reference)

    print(a)
    print(b)

    assert (np.allclose(a, b, 0.001))
