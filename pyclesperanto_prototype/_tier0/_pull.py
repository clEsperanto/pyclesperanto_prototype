def pull(oclarray):
    """Pull array from GPU memory to device."""
    return oclarray.get().T


def pull_zyx(oclarray):
    return oclarray.get()
