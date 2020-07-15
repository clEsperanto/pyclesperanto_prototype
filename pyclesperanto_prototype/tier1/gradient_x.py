from ..tier0 import execute

def gradient_x (src, dst):
    """Computes the gradient of gray values along X. 
    
    Assuming a, b and c are three adjacent
     pixels in X direction. In the target image will be saved as: <pre>b' = c - a;</pre>

    Available for: 2D, 3D

    Parameters
    ----------
    (Image source, ByRef Image destination)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_gradientX


    Returns
    -------

    """


    parameters = {
        "dst":dst,
        "src":src
    }

    execute(__file__, 'gradient_x_' + str(len(dst.shape)) + 'd_x.cl', 'gradient_x_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
