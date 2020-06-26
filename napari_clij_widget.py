two_dim = "data/blobs.tif"
three_dim = "data/t1-head.tif"

from skimage import io
import numpy as np
import napari
import clesperanto as cle
from magicgui import magicgui #https://magicgui.readthedocs.io/en/latest/
from napari.layers import Image
from enum import Enum

image_2d = io.imread(two_dim)
image_3d = io.imread(three_dim)


# Using Enums for getting a dropdown menu
# clesperanto functions are not being passed as enum values for some reason, so they are defined as strings
class gpu_filter(Enum):
    # using pyclesperanto filtering images with a gpu
    mean = 'cle.mean_sphere'
    maximum = 'cle.maximum_sphere'
    minimum = 'cle.minimum_sphere'
    top_hat = 'cle.top_hat_sphere'
    gaussian_blur = 'cle.gaussian_blur'
    crop = 'cle.crop'


with napari.gui_qt():
    viewer = napari.Viewer()
    viewer.add_image(image_2d, name='2D_image_orig')
    viewer.add_image(image_3d, name='3D_image_orig')


    # use auto_call=True for instantaneous execution
    #can add sliders using QSlider, but need to show values
    @magicgui(call_button='Compute')
    def clij_filter(input: Image, operation: gpu_filter, x: float = 0, y: float = 0,
                    z: float = 0) -> Image:
        if input:
            cle_input = cle.push(input.data)
            output = cle.create_like(input.data)
            # concatenate the vale from gpu_operation  as a string
            command = operation.value + "(cle_input, output, x, y, z)"
            # use evaluate to execute the command
            eval(command)
            output = cle.pull(output)
            print("output shape", output.shape)
            # reshape image from z,x,y to x,y,z; image is returned as z,x,y from cle push and pull operations
            output = np.swapaxes(output, 0, -1)
            print("output shape after reshape ", output.shape)
            return output


    # use of magic_gui also passes an attribute to clij_operation  "called"
    # def print_shape(image):
    # print('Output image shape ', image.shape)

    gui = clij_filter.Gui()
    viewer.window.add_dock_widget(gui)
    # if a layer gets added or removed, refresh the dropdown choices
    viewer.layers.events.changed.connect(lambda x: gui.refresh_choices("input"))

    # clij_operation.called.connect(print_shape)
