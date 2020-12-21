from .._tier0 import Image

def imshow(image : Image, title : str = None, labels : bool = False, min_display_intensity : float = None, max_display_intensity : float = None):
    from .._tier0 import pull_zyx
    image = pull_zyx(image)

    cmap = None
    if labels:
        import matplotlib
        import numpy as np
        cmap = matplotlib.colors.ListedColormap ( np.random.rand ( 256,3))

    import matplotlib.pyplot as plt
    plt.imshow(image, cmap=cmap, vmin=min_display_intensity, vmax=max_display_intensity)
    plt.show()
