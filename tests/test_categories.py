def test_categories():
    import pyclesperanto_prototype as cle
    names = cle.categories()

    assert len(names) > 0