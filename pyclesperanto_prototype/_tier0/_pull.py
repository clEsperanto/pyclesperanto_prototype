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
    >>> cle.pull_zyx(image)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_pull
    """
    import warnings
    warnings.warn(
            "Deprecated: The behaviour of `pull()` will change in a future release. Switch to using push_zyx now to prvent issues in the future.",
            DeprecationWarning
        )

    return oclarray.get().T


def pull_zyx(oclarray):
    return oclarray.get()
