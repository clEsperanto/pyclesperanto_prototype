
def artificial_tissue_2d(width: int = 256, height: int = 256, delta_x=24, delta_y=16, random_sigma_x=3, random_sigma_y=3):
    """

    Parameters
    ----------
    width
    height
    delta_x
    delta_y
    random_sigma_x
    random_sigma_y

    Returns
    -------

    """
    from .._tier0 import push_zyx
    from .._tier2 import pointlist_to_labelled_spots
    from .._tier4 import extend_labeling_via_voronoi
    import numpy as np
    from numpy.random import normal

    all_x_coords = []
    all_y_coords = []

    for i, y in enumerate(range(0, height, delta_y)):
        offset_x = 0 if i % 2 == 0 else delta_x / 2

        x_coords = np.asarray(np.arange(offset_x, width, delta_x))
        y_coords = np.zeros([len(x_coords)]) + 1 * y

        x_rand = normal(loc=0, scale=random_sigma_x, size=[len(x_coords)])
        y_rand = normal(loc=0, scale=random_sigma_y, size=[len(x_coords)])

        x_coords = x_coords + x_rand
        y_coords = y_coords + y_rand

        all_x_coords = np.append(all_x_coords, x_coords)
        all_y_coords = np.append(all_y_coords, y_coords)

    # print(all_x_coords)
    # print(all_y_coords)

    # define centroids of cells
    pointlist = push_zyx(np.asarray(
        [
            all_x_coords,
            all_y_coords
        ]))
    # print(pointlist)

    centroids = pointlist_to_labelled_spots(pointlist)

    cells = extend_labeling_via_voronoi(centroids)

    return cells