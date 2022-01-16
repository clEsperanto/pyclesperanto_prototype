def artificial_objects_2d():
    """
    Creates an image showing artificial objects such as lines, blobs, membranes and nuclei.

    For practical application, it is recommended to blur this image, and up/downscale it.

    Returns
    -------
    image: Image

    """
    from .._tier0 import create, create_like
    from .._tier1 import set, detect_label_edges, draw_line, draw_sphere, maximum_sphere, paste, set_ramp_y
    from .._tier11 import reduce_labels_to_centroids
    from ._artificial_tissue_2d import artificial_tissue_2d

    image = create((512, 512))
    set(image, 0)

    for t in range(0, 5):
        draw_line(image, x1=10, y1=10 + t * 50, x2=40, y2=40 + t * 50, thickness=t + 1, value=255)
        draw_line(image, x1=60, y1=40 + t * 50, x2=60, y2=10 + t * 50, thickness=t + 1, value=255)
        draw_line(image, x1=80, y1=40 + t * 50, x2=110, y2=10 + t * 50, thickness=t + 1, value=255)
        draw_line(image, x1=120, y1=25 + t * 50, x2=150, y2=25 + t * 50, thickness=t + 1, value=255)

        draw_sphere(image, x=175, y=25 + t * 50, radius_x=(t + 1) * 2, radius_y=10, value=255)
        draw_sphere(image, x=200, y=25 + t * 50, radius_x=10, radius_y=(t + 1) * 2, value=255)

    # membranes
    cells = artificial_tissue_2d(width=350)
    membranes = detect_label_edges(cells)

    for x, t in zip([0, 20, 40, 50, 60, 70, 75, 80, 85, 90, 93, 96, 99,
                     100, 120, 140, 150, 160, 170, 175, 180, 185, 190, 193, 196, 199],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                     2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]):
        draw_line(membranes, x1=x, x2=x, y1=0, y2=256, thickness=t, value=0)

    nuclei = reduce_labels_to_centroids(cells)

    # remove nuclei from upper half
    binary = create_like(nuclei)
    set_ramp_y(binary)
    binary = binary > 128
    nuclei = nuclei * binary

    membranes = membranes + (maximum_sphere(nuclei, radius_x=3, radius_y=3) > 0) * 2

    paste(membranes * 256, image, destination_x=225)

    for t in range(1, 10):
        draw_sphere(image, x=20, y=255 + (t-1) * 30, radius_x=5+t, radius_y=5+t, value=255)
        draw_sphere(image, x=60, y=255 + (t-1) * 30, radius_x=5+t, radius_y=5+t, value=255)
        draw_sphere(image, x=60, y=255 + (t-1) * 30, radius_x=4+t, radius_y=4+t, value=0)
        draw_sphere(image, x=100, y=255 + (t-1) * 30, radius_x=5+t, radius_y=5+t, value=255)
        draw_sphere(image, x=100, y=255 + (t-1) * 30, radius_x=3+t, radius_y=3+t, value=0)
        draw_sphere(image, x=140, y=255 + (t-1) * 30, radius_x=5+t, radius_y=5+t, value=255)
        draw_sphere(image, x=140, y=255 + (t-1) * 30, radius_x=2+t, radius_y=2+t, value=0)

    for y in range(1, 9):
        for x in range(1, 9):
            draw_sphere(image, x=180 + (x-1) * 30, y=255 + (y-0.25) * 30, radius_x=max(x,y) * 2, radius_y=max(x,y) * 2, value=255)

    draw_line(image, x1=438, y1=438, x2=502, y2=502, thickness=3, value=255)
    draw_line(image, x1=502, y1=438, x2=438, y2=502, thickness=3, value=255)

    draw_line(image, x1=438, y1=438, x2=470, y2=396, thickness=3, value=255)
    draw_line(image, x1=502, y1=438, x2=470, y2=396, thickness=3, value=255)
    draw_line(image, x1=470, y1=364, x2=470, y2=396, thickness=3, value=255)

    draw_line(image, x1=470, y1=364, x2=470, y2=256, thickness=3, value=255)
    draw_line(image, x1=438, y1=256, x2=502, y2=256, thickness=3, value=255)

    draw_line(image, x1=438, y1=272, x2=502, y2=338, thickness=3, value=255)
    draw_line(image, x1=502, y1=272, x2=438, y2=338, thickness=3, value=255)

    draw_line(image, x1=438, y1=354, x2=502, y2=354, thickness=3, value=255)
    draw_line(image, x1=438, y1=370, x2=502, y2=370, thickness=3, value=255)

    return image