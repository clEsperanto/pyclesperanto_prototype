# Inspired by
# https://github.com/pr4deepr/pyclesperanto_prototype/blob/master/napari_clij_widget.py
import napari
import pyclesperanto_prototype as cle
from magicgui import magicgui
from napari.layers import Image, Labels

@magicgui(auto_call=True)
def process_image(input: Image, sigma: float = 5) -> Labels:
    if input:
        # push image to GPU
        input = cle.push_zyx(input.data)

        # process the mage
        blurred = cle.gaussian_blur(input, sigma_x=sigma, sigma_y=sigma)
        binary = cle.threshold_otsu(blurred)
        labels = cle.connected_components_labeling_box(binary)

        # pull result back
        output = cle.pull_zyx(labels)
        return output

# load data
from skimage.io import imread
image = imread('https://samples.fiji.sc/blobs.png')

# start up napari
with napari.gui_qt():
    viewer = napari.Viewer()
    viewer.add_image(image, name='blobs')

    # generate a Graphical User Interface from the function above magically
    gui = process_image.Gui()
    viewer.window.add_dock_widget(gui)


