
from ..core import execute

def add_images_weighted(input1, input2, output, weight1, weight2):
    """Calculates the sum of pairs of pixels x and y from images X and Y weighted with factors a and b.
    
    <pre>f(x, y, a, b) = x * a + y * b</pre>

    Available for: 2D, 3D

    Parameters
    ----------
    (Image summand1, Image summand2, ByRef Image destination, Number factor1, Number factor2)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_addImagesWeighted


    Returns
    -------

    """


    parameters = {
        "src":input1,
        "src1":input2,
        "dst":output,
        "factor":float(weight1),
        "factor1":float(weight2)
    };

    execute(__file__, 'add_images_weighted_' + str(len(output.shape)) + 'd_x.cl', 'add_images_weighted_' + str(len(output.shape)) + 'd', output.shape, parameters);
