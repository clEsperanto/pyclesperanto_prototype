from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import create_vector_from_labelmap

@plugin_function(output_creator=create_vector_from_labelmap)
def flag_existing_labels(label_src : Image, flag_vector_destination : Image = None):
    """
    Given a label map this function will generate a binary vector where all pixels are set to 1 if label with given
    x-coordinate in the vector exists. For example a label image such as
    ```
    0 1
    3 5
    ```

    will produce a flag_vector like this:
    ```
    1 1 0 1 0 1
    ```

    Parameters
    ----------
    label_src : Image
        a label image
    flag_vector_destination, : Image optional
        binary vector, if given should have size 1*n with n = maximum label + 1

    Returns
    -------

    """
    from .._tier0 import execute
    from .._tier1 import set

    parameters = {
        "dst": flag_vector_destination,
        "src": label_src
    }

    set(flag_vector_destination, 0)

    execute(__file__, '../clij-opencl-kernels/kernels/flag_existing_labels_x.cl', 'flag_existing_labels', label_src.shape, parameters)
    return flag_vector_destination

