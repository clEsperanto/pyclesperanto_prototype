def operations(must_have_categories : list = None, must_not_have_categories : list = None) -> dict:
    result = {}

    from inspect import getmembers, isfunction
    import pyclesperanto_prototype as cle

    if not hasattr(operations, "_all") or operations._all is None:
        operations._all = getmembers(cle, isfunction)

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
    dict = operations()
    return dict[name]


