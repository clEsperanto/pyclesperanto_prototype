from .._tier0 import Image

def imshow(image : Image, title : str = None, labels : bool = False, min_display_intensity : float = None, max_display_intensity : float = None, color_map = None, plot = None, colorbar:bool = False):
    from .._tier0 import pull
    from .._tier1 import maximum_z_projection

    if len(image.shape) == 3:
        image = maximum_z_projection(image)

    image = pull(image)

    cmap = color_map
    if labels:
        import matplotlib
        import numpy as np

        if not hasattr(imshow, "labels_cmap"):
            lut = np.random.rand(65537, 3)
            lut[0, :] = 0
            imshow.labels_cmap = matplotlib.colors.ListedColormap(lut)
        cmap = imshow.labels_cmap

    if plot is None:
        import matplotlib.pyplot as plt
        plt.imshow(image, cmap=cmap, vmin=min_display_intensity, vmax=max_display_intensity, interpolation='nearest')
        if colorbar:
            plt.colorbar()
        plt.show()
    else:
        plot.imshow(image, cmap=cmap, vmin=min_display_intensity, vmax=max_display_intensity, interpolation='nearest')
        if colorbar:
            plot.colorbar()

