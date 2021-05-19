from ._operations import operations

def categories():

    from inspect import getmembers, isfunction
    import pyclesperanto_prototype as cle
    ops = getmembers(cle, isfunction)

    cats = []

    for operation_name, operation in ops:
        if hasattr(operation, "categories") and operation.categories is not None:
            for cat in operation.categories:
                if cat not in cats:
                    cats = cats + [cat]

    return cats