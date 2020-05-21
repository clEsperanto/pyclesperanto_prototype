from ..core import execute

def binary_edge_detection (src, dst):

    parameters = {
        "dst": dst,
        "src":src
    }

    # TODO: Rename cl file and kernel function to fit to naming conventions. This needs to be done in clij2 as well.
    execute(__file__, 'binaryEdgeDetection' + str(len(dst.shape)) + 'd_x.cl', 'binary_edge_detection_diamond_image' + str(len(dst.shape)) + 'd', dst.shape, parameters)
