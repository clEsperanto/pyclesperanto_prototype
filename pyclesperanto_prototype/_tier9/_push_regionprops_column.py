def push_regionprops_column(regionprops : list, column : str):
    import numpy as np
    if hasattr(regionprops[0], 'original_label'):
        labels = [r.original_label for r in regionprops]
    else:
        labels = [r.label for r in regionprops]
    max_label = np.max(labels)

    values = np.zeros([max_label + 1])
    for r in regionprops:
        if hasattr(r, 'original_label'):
            label = r.original_label
        else:
            label = r.label
        values[label] = r[column]

    from .._tier0 import push_zyx
    return push_zyx(np.asarray([values]))
