def operations(category : str = None) -> dict:
    result = {}

    from inspect import getmembers, isfunction
    import pyclesperanto_prototype as cle

    if not hasattr(operations, "_all") or operations._all is None:
        operations._all = getmembers(cle, isfunction)

    if category is None:
        return dict(operations._all) # make a copy to keep it safe

    for operation_name, operation in operations._all:
        if hasattr(operation, "categories") and operation.categories is not None:
            if category in operation.categories and operation not in result:

                result[operation_name] = operation

    return result

def operation(name : str):
    dict = operations()
    return dict[name]


