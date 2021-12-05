import numpy as np
from .._tier0 import Image

def to_igraph(adjacency_matrix:Image, centroids:Image=None):
    """
    Converts a given adjacency matrix to a iGraph [1] graph data structure.

    Note: the given centroids typically have one entry less than the adjacency matrix is wide, because
    those matrices contain a first row and column representing background. When exporting the networkx graph,
    that first column will be ignored.

    Parameters
    ----------
    adjacency_matrix : Image
        m*m touch-matrix, proximal-neighbor-matrix or n-nearest-neighbor-matrix
    centroids : Image, optional
        d*(m-1) matrix, position list of centroids

    Returns
    -------
    iGraph graph

    See Also
    --------
    ..[1] https://igraph.org/
    """
    try:
        import igraph
    except ImportError:
        raise ImportError("igraph is not installed. Please refer to the documentation https://igraph.org/python/")

    igraph_graph = igraph.Graph(adjacency_matrix.shape[0] - 1)
    edge_list = np.nonzero(np.asarray(adjacency_matrix)[1:,1:])
    igraph_graph.add_edges(np.asarray(edge_list).T)

    if centroids is not None:
        igraph_graph.vs['x'] = centroids[0]
        igraph_graph.vs['y'] = centroids[1]
        if centroids.shape[0] > 2: # 3D data
            igraph_graph.vs['z'] = centroids[2]

    return igraph_graph
