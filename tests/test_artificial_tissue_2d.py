def test_artificial_tissue_2d():
    import pyclesperanto_prototype as cle
    image = cle.artificial_tissue_2d(width=500, height=250)

    assert image.shape[0] == 250
    assert image.shape[1] == 500
