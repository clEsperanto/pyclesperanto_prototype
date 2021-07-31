def operations(must_have_categories : list = None, must_not_have_categories : list = None) -> dict:
    """Retrieve a dictionary of operations, which can be filtered by annotated categories.

    Parameters
    ----------
    must_have_categories : list of str, optional
        if provided, the result will be filtered so that operations must contain all given categories.
    must_not_have_categories : list of str, optional
        if provided, the result will be filtered so that operations must not contain all given categories.

    Returns
    -------
    dict of str : function
    """
    if isinstance(must_have_categories, str):
        must_have_categories = [must_have_categories]
    if isinstance(must_not_have_categories, str):
        must_have_categories = [must_not_have_categories]

    result = {}

    from inspect import getmembers, isfunction
    import pyclesperanto_prototype as cle

    # retrieve all operations and cache the result for later reuse
    if not hasattr(operations, "_all") or operations._all is None:
        operations._all = getmembers(cle, isfunction)

    # filter operations according to given constraints
    for operation_name, operation in operations._all:
        keep_it = True
        if hasattr(operation, "categories") and operation.categories is not None:
            if must_have_categories is not None:
                if not all(item in operation.categories for item in must_have_categories):
                    keep_it = False

            if must_not_have_categories is not None:
                if any(item in operation.categories for item in must_not_have_categories):
                    keep_it = False
        else:
            if must_have_categories is not None:
                keep_it = False
        if (keep_it):
            result[operation_name] = operation

    return result

def operation(name : str):
    """Returns a function from the pyclesperanto package

    Parameters
    ----------
    name : str
        name of the operation

    Returns
    -------
        function
    """
    dict = operations()
    return dict[name]

def search_operation_names(name):
    return [a for a in list(operations().keys()) if name in a]
