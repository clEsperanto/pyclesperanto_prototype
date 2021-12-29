def test_available_device_names():
    import pyclesperanto_prototype as cle
    names = cle.available_device_names()

    assert len(names) > 0