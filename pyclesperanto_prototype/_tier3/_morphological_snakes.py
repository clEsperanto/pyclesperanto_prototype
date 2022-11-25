from skimage import morphology
from .._tier0 import Image
from .._tier0 import plugin_function
from .._tier0 import create_like
from .._tier1 import absolute
from .._tier1 import binary_or
from .._tier1 import binary_not
from .._tier1 import gradient_x
from .._tier1 import gradient_y
from .._tier1 import gradient_z
from .._tier1 import greater_constant
from .._tier1 import mask
from .._tier2 import opening_sphere

@plugin_function
def morphological_snake(input_image: Image, contour_image: Image=None, output_image: Image=None, n_iter: int=100, smoothing: int=1, lambda1: float=1, lambda2: float=1) -> Image:
    
    if contour_image is None:
        contour_image = morphology.disk(int(input_image.shape[0] // 2))
    
    greater_constant(contour_image, constant=0, destination=output_image)
    
    for _ in range(n_iter):
        invert_curve = 1 - output_image
        outside_image = (input_image * invert_curve).sum()
        outside_curve_area = invert_curve.sum() + 1e-8
        c0 = outside_image / outside_curve_area

        inside_image = (input_image * output_image).sum()
        inside_curve_area = output_image.sum() + 1e-8
        c1 = inside_image / inside_curve_area

        absolute_gradient = create_like(output_image)

        for e in range(input_image.ndim):
            if e == 0:   
                absolute_gradient += absolute(gradient_x(output_image))
            if e == 1:
                absolute_gradient += absolute(gradient_y(output_image))
            if e == 2:
                absolute_gradient += absolute(gradient_z(output_image))


        current_curve = absolute_gradient * (lambda1 * (input_image - c1)**2 - lambda2 * (input_image - c0)**2)

        positive_curve = current_curve > 0
        negative_curve = current_curve < 0

        combined_mask = binary_or(positive_curve, negative_curve)
        inverted_mask = binary_not(combined_mask)
        masked_curve = mask(output_image, inverted_mask)
        output_image = masked_curve + negative_curve
        
        opening_sphere(output_image, destination=output_image, radius_x=smoothing, radius_y=smoothing, radius_z=smoothing)

    return output_image