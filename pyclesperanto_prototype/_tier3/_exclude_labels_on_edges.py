import warnings

from pyclesperanto_prototype._tier0 import execute
from pyclesperanto_prototype._tier0 import plugin_function
from pyclesperanto_prototype._tier0 import Image
from .._tier0 import pull
from .._tier0 import push
from .._tier2 import maximum_of_all_pixels
from .._tier1 import replace_intensities
from .._tier0 import create_like, create_labels_like
import numpy as np

@plugin_function(categories=['label processing', 'in assistant', 'bia-bob-suggestion'], priority=1, output_creator=create_labels_like)
def exclude_labels_on_edges(label_map_input : Image, label_map_destination : Image = None, exclude_in_x:bool = True, exclude_in_y:bool = True, exclude_in_z:bool = True, exlude_in_x:bool = None, exlude_in_y:bool = None, exlude_in_z:bool = None) -> Image:
    """Removes all labels from a label map which touch the edges of the image 
    (in X, Y and Z if the image is 3D). 
    
    Remaining label elements are renumbered afterwards. 
    
    Parameters
    ----------
    label_map_input : Image
    label_map_destination : Image, optional
    exclude_in_x : bool, optional
        Exclude labels along min and max x (default is True)
    exclude_in_y : bool, optional
        Exclude labels along min and max y (default is True)
    exclude_in_z : bool, optional
        Exclude labels along min and max z (default is True)

    Returns
    -------
    label_map_destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.exclude_labels_on_edges(label_map_input, label_map_destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_excludeLabelsOnEdges
    """
    if exlude_in_x is not None:
        warnings.warn("exlude_in_x parameter of cle.exclude_labels_on_edges() is deprecated. Use exclude_in_x instead.")
        exclude_in_x = exlude_in_x
    if exlude_in_y is not None:
        warnings.warn("exlude_in_y parameter of cle.exclude_labels_on_edges() is deprecated. Use exclude_in_y instead.")
        exclude_in_y = exlude_in_y
    if exlude_in_z is not None:
        warnings.warn("exlude_in_z parameter of cle.exclude_labels_on_edges() is deprecated. Use exclude_in_z instead.")
        exclude_in_z = exlude_in_z

    num_labels = int(maximum_of_all_pixels(label_map_input))

    label_indices = range(0, num_labels + 1)

    label_index_map = push(np.asarray(label_indices))

    parameters = {
        "src":label_map_input,
        "label_index_dst":label_index_map
    }
    if (len(label_map_input.shape) == 3):
        dimensions = [
            label_map_input.shape[0],
            label_map_input.shape[1],
            label_map_input.shape[2]
        ]
    else:
        dimensions = [
            1,
            label_map_input.shape[0],
            label_map_input.shape[1]
        ]

    if (len(label_map_input.shape) == 3 and exclude_in_z):
        global_sizes = [1, dimensions[1], dimensions[2]]
        execute(__file__, "../clij-opencl-kernels/kernels/exclude_labels_on_edges_3d_x.cl", "exclude_on_edges_z_3d", global_sizes, parameters)

    if exclude_in_y:
        global_sizes = [dimensions[0], 1 ,dimensions[2]]
        execute(__file__, "../clij-opencl-kernels/kernels/exclude_labels_on_edges_3d_x.cl", "exclude_on_edges_y_3d", global_sizes, parameters)

    if exclude_in_x:
        global_sizes = [dimensions[0], dimensions[1], 1]
        execute(__file__, "../clij-opencl-kernels/kernels/exclude_labels_on_edges_3d_x.cl", "exclude_on_edges_x_3d", global_sizes, parameters)


    label_indices = pull(label_index_map)
    count = 1
    for i in range(1, num_labels + 1):
        if (label_indices[i] > 0):
            label_indices[i] = count
            count = count + 1

    label_index_map = push(np.asarray(label_indices))

    replace_intensities(label_map_input, label_index_map, label_map_destination)

    return label_map_destination