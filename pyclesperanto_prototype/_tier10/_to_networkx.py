from .._tier0 import plugin_function
from .._tier0 import Image
import numpy as np

def to_networkx(adjacency_matrix:Image, centroids:Image=None):
    """
    Converts a given adjacency matrix to a networkx [1] graph data structure.

    Note: the given centroids typically have one entry less than the adjacency matrix is wide, because
    those matrices contain a first row and column representing background. When exporting the igraph graph,
    that first column will be ignored.

    Parameters
    ----------
    adjacency_matrix : Image
        m*m touch-matrix, proximal-neighbor-matrix or n-nearest-neighbor-matrix
    centroids : Image, optional
        d*(m-1) matrix, position list of centroids

    Returns
    -------
    networkx graph

    See Also
    --------
    ..[1] https://networkx.org/documentation/stable/reference/generated/networkx.convert_matrix.from_numpy_matrix.html
    """
    try:
        import networkx
    except ImportError:
        raise ImportError("networkx is not installed. Please refer to the documentation https://networkx.org/documentation/stable/install.html")


    networkx_graph = networkx.from_numpy_matrix(np.asarray(adjacency_matrix)[1:,1:])

    if centroids is not None:
        from .._tier1 import transpose_xy
        centroid_positions = transpose_xy(centroids)

        for n in range(len(networkx_graph.nodes)):
            networkx_graph.nodes[n]['pos'] = np.asarray(centroid_positions[n])

    return networkx_graph
