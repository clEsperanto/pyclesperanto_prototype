import pyclesperanto_prototype as cle

# load data
from skimage.io import imread
image = imread('https://samples.fiji.sc/blobs.png')

# start up napari
import napari
with napari.gui_qt():
    viewer = napari.Viewer()
    viewer.add_image(image, name='blobs')

    # push image to GPU
    input = cle.push_zyx(image)

    # process the image
    sigma = 3
    blurred = cle.gaussian_blur(input, sigma_x=sigma, sigma_y=sigma)
    binary = cle.threshold_otsu(blurred)
    labels = cle.connected_components_labeling_box(binary)

    # pull result back
    output = cle.pull_zyx(labels)

    # add it to napari
    viewer.add_labels(output)

