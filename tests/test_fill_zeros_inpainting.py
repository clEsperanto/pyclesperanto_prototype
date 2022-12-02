def test_fill_zeros_inpainting():
    import pyclesperanto_prototype as cle

    test = cle.asarray([[
        [1,1,1,2,3,3,3],
        [1,1,1,0,3,3,3],
        [1,1,0,0,0,3,3],
        [1,0,0,0,0,0,3],
    ]])

    reference = cle.asarray([[
        [1,1,1,2,3,3,3],
        [1,1,1,3,3,3,3],
        [1,1,1,3,3,3,3],
        [1,1,1,3,3,3,3],
    ]])

    result = cle.fill_zeros_inpainting(test)

    assert cle.array_equal(result, reference)
