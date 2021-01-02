from pyclesperanto_prototype._tier0 import Image
from pyclesperanto_prototype._tier0 import plugin_function
from pyclesperanto_prototype._tier0 import create_none

@plugin_function(output_creator=create_none)
def euclidean_distance_from_label_centroid_map(labels:Image, centroids_pointlist:Image = None, distance_map_destination:Image = None):
    """Takes a label map, determines the centroids of all labels and writes the distance of all labelled pixels to
    their centroid in the result image. Background pixels stay zero.
    """
    from ._centroids_of_background_and_labels import centroids_of_background_and_labels
    from .._tier0 import create_like
    from .._tier0 import execute

    if centroids_pointlist is None:
        centroids_pointlist = centroids_of_background_and_labels(labels)

    if distance_map_destination is None:
        distance_map_destination = create_like(labels)

    parameters = {
        "dst": distance_map_destination,
        "src": labels,
        "pointlist": centroids_pointlist
    }

    execute(__file__, '../clij-opencl-kernels/kernels/euclidean_distance_from_label_centroid_map_x.cl', 'euclidean_distance_from_label_centroid_map', distance_map_destination.shape, parameters)
    return distance_map_destination

