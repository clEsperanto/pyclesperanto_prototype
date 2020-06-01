from ..core import execute


def mask_label (src, labelmap, dst, label_id):
    """
    documentation placeholder
    """


    parameters = {
        "src":src,
        "src_label_map":labelmap,
        "label_id": float(label_id),
        "dst": dst
    }

    execute(__file__, 'mask_label_' + str(len(dst.shape)) + 'd_x.cl', 'mask_label_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

