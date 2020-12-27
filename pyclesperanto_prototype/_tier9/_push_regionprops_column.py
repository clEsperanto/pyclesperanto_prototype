def push_regionprops_column(regionprops : list, column : str):
    import numpy as np
    labels = [r.label for r in regionprops]
    max_label = np.max(labels)

    values = np.zeros([max_label + 1])