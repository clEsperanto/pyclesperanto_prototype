from .._tier0 import Image, plugin_function

@plugin_function
def imshow(image : Image, title : str = None, labels : bool = False, min_display_intensity : float = None, max_display_intensity : float = None, color_map = None, plot = None, colorbar:bool = False, colormap = None, alpha:float = None, continue_drawing:bool = False, mute_warning:bool=False):
    """Visualize an image, e.g. in Jupyter notebooks.

    Parameters
    ----------
    image: np.ndarray
        numpy or OpenCL-backed image to visualize
    title: str
        Obsolete (kept for ImageJ-compatibility)
    labels: bool
        True: integer labels will be visualized with colors
        False: Specified or default colormap will be used to display intensities.
    min_display_intensity: float
        lower limit for display range
    max_display_intensity: float
        upper limit for display range
    color_map: str
        deprecated, use colormap instead
    plot: matplotlib axis
        Plot object where the image should be shown. Useful for putting multiple images in subfigures.
    colorbar: bool
        True puts a colorbar next to the image. Will not work with label images and when visualizing multiple
        images (continue_drawing=True).
    colormap: str or matplotlib colormap
    alpha: float
        alpha blending value
    continue_drawing: float
        True: the next shown image can be visualized on top of the current one, e.g. with alpha = 0.5
    """
    if not mute_warning:
        import warnings
        warnings.warn("cle.imshow is deprecated, use stackview.imshow instead.")
    import numpy as np
    from .._tier0 import pull
    from .._tier1 import maximum_z_projection

    if len(image.shape) == 3:
        image = maximum_z_projection(image)

    image = pull(image)
    if len(image.shape) == 1:
        image = image[np.newaxis]

    if color_map is not None:
        import warnings
        warnings.warn("The imshow parameter color_map is deprecated. Use colormap instead.")
        if colormap is None:
            colormap = color_map

    if colormap is None:
        colormap = "Greys_r"

    cmap = colormap
    if labels:
        import matplotlib
        import numpy as np

        if not hasattr(imshow, "labels_cmap"):
            from numpy.random import MT19937
            from numpy.random import RandomState, SeedSequence
            rs = RandomState(MT19937(SeedSequence(3)))
            lut = rs.rand(65537, 3)
            lut[0, :] = 0
            # these are the first four colours from matplotlib's default
            lut[1] = [0.12156862745098039, 0.4666666666666667, 0.7058823529411765]
            lut[2] = [1.0, 0.4980392156862745, 0.054901960784313725]
            lut[3] = [0.17254901960784313, 0.6274509803921569, 0.17254901960784313]
            lut[4] = [0.8392156862745098, 0.15294117647058825, 0.1568627450980392]
            
            imshow.labels_cmap = matplotlib.colors.ListedColormap(lut)
        cmap = imshow.labels_cmap

        if min_display_intensity is None:
            min_display_intensity = 0
        if max_display_intensity is None:
            max_display_intensity = 65536

    if plot is None:
        import matplotlib.pyplot as plt
        plt.imshow(image, cmap=cmap, vmin=min_display_intensity, vmax=max_display_intensity, interpolation='nearest', alpha=alpha)
        if colorbar:
            plt.colorbar()
        if not continue_drawing:
            plt.show()
    else:
        ims = plot.imshow(image, cmap=cmap, vmin=min_display_intensity, vmax=max_display_intensity, interpolation='nearest', alpha=alpha)
        if colorbar:
            fig = plot.get_figure()
            cax = fig.add_axes([plot.get_position().x1 + 0.01, plot.get_position().y0, 0.005,
                                 plot.get_position().height])
            fig.colorbar(ims, cax=cax)

