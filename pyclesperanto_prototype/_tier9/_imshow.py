from .._tier0 import Image

def imshow(image : Image, title : str = None, labels : bool = False, min_display_intensity : float = None, max_display_intensity : float = None, color_map = None, plot = None):
    from .._tier0 import pull_zyx
    from .._tier1 import maximum_z_projection

    if len(image.shape) == 3:
        image = maximum_z_projection(image)

    image = pull_zyx(image)

    cmap = color_map
    if labels:
        import matplotlib
        import numpy as np
        cmap = matplotlib.colors.ListedColormap ( np.random.rand ( 256,3))

    if plot is None:
        import matplotlib.pyplot as plt
        plt.imshow(image, cmap=cmap, vmin=min_display_intensity, vmax=max_display_intensity)
        plt.show()
    else:
        plot.imshow(image, cmap=cmap, vmin=min_display_intensity, vmax=max_display_intensity)

