from .._tier0 import plugin_function
from .._tier0 import create_from_pointlist
from .._tier0 import Image
from .._tier0 import execute

@plugin_function(output_creator=create_from_pointlist)
def pointindexlist_to_mesh(pointlist: Image, indexlist : Image, mesh_target : Image = None):
    """

    Parameters
    ----------
    pointlist
    indexlist
    mesh_target

    Returns
    -------

    """
    parameters = {
        "src_pointlist": pointlist,
        "src_indexlist": indexlist,
        "dst_mesh": mesh_target,
    }

    dimensions = [1, 1, indexlist.shape[-1]]

    execute(__file__, "pointindexlist_to_mesh_3d_x.cl", "pointindexlist_to_mesh_3d", dimensions, parameters)

    return mesh_target
