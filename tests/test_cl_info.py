def test_cl_info():
    import pyclesperanto_prototype as cle
    info = cle.cl_info()

    assert len(info) > 0