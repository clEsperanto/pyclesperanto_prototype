def pull(oclarray):
    """Returns an image from GPU memory as numpy compatible array

    .. deprecated:: 0.6.0
        `pull` behaviour will be changed pyclesperanto_prototype 0.7.0 to do the same as
        `pull_zyx` because it's faster and having both doing different things is confusing.
    
    Parameters
    ----------
    image : OCLArray

    Returns
    -------
    numpy array
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.pull(image)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_pull
    """
    return oclarray.get()

def pull_zyx(oclarray):
    import warnings
    warnings.warn(
        "Deprecated: `pull_zyx()` is now deprecated as it does the same as `pull()`.",
        DeprecationWarning
    )
    return oclarray.get()
