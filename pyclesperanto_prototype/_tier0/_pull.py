def pull(oclarray):
    """Copies an image specified by its name from GPU memory back to ImageJ 
    and shows it. 
    
    Parameters
    ----------
    image : String
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.pull(image)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_pull
    """
    import warnings
    warnings.warn(
            "Deprecated: The behaviour of `pull()` may change in a future release. Switch to using push_zyx now to prvent issues in the future.",
            DeprecationWarning
        )

    return oclarray.get().T


def pull_zyx(oclarray):
    return oclarray.get()
