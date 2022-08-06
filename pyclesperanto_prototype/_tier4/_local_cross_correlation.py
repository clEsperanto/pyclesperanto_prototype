from pyclesperanto_prototype._tier0 import Image, plugin_function, execute
from pyclesperanto_prototype._tier9 import imshow

@plugin_function(categories=['filter', 'combine', 'in assistant'])
def local_cross_correlation(source: Image, kernel: Image, destination: Image = None) -> Image:
    """Compute the cross correlation of an image to a given kernel.

    Parameters
    ----------
    source: Image
    kernel: Image
    destination: Image, optional

    Returns
    -------
    destination

    See Also
    -------
    https://anomaly.io/understand-auto-cross-correlation-normalized-shift/index.html
    """

    parameters = {
        "src1": source,
        "src2": kernel,
        "dst": destination,
    }

    execute(__file__, './local_cross_correlation.cl', 'local_cross_correlation', destination.shape, parameters)
    return destination
