def test_operations():
    import pyclesperanto_prototype as cle
    names = cle.operations()

    assert len(names) > 0

def test_operations_search():
    import pyclesperanto_prototype as cle
    names = cle.operations("map")

    assert len(names) > 0

def test_operations_search_not():
    import pyclesperanto_prototype as cle
    names = cle.operations(must_not_have_categories="map")

    assert len(names) > 0

def test_operation():
    import pyclesperanto_prototype as cle
    op = cle.operation("gaussian_blur")

    assert op is not None
