# Tribolium castaneum morphometry workflow
# See also: https://clij.github.io/clij2-docs/md/tribolium_morphometry/
# Thanks to Pradeep Rajasekhar (Monash University) and Daniela Vorkel (MPI CBG Dresden)
# for code snippets and data :-)

import pyclesperanto_prototype as cle

# we need to select a powerful GPU for this
cle.select_device("RTX")

# check which GPU we use
print(cle.get_device().name)


# load data
from skimage.io import imread
image = imread('C:/structure/data/lund1051_resampled.tif')
# The dataset is available online:
# https://git.mpi-cbg.de/rhaase/clij2_example_data/blob/master/lund1051_resampled.tif

print(image.shape)

# The dataset shows a Tribolium castaneum embryo, imaged by a custom light sheet microscope,
# at a wavelength of 488nm (Imaging credits: Daniela Vorkel, Myers lab, MPI CBG).
# The data set has be resample to a voxel size of
voxel_size = [1, 1, 1] # microns
# The embryo expresses nuclei-GFP. We will use the dataset to detect nuclei and to generate
# an estimated cell-segmentation.

# Define an interactive user interface using magicgui
from magicgui import magicgui
from napari.layers import Image, Labels

# use auto_call=True for instantaneous execution
@magicgui(auto_call=True)
def workflow(input: Image, sigma=3, threshold : float = 30) -> Labels:
    if input:
        # push image to GPU memory and show it
        gpu_input = cle.push(input.data)

        # Spot detection
        # After some noise removal/smoothing, we perform a local maximum detection

        # gaussian blur
        gpu_blurred = cle.gaussian_blur(gpu_input, sigma_x=sigma, sigma_y=sigma, sigma_z=0)

        # detect maxima
        gpu_detected_maxima = cle.detect_maxima_box(gpu_blurred)

        # Spot curation
        # Now, we remove spots with values below a certain intensity and label the remaining spots

        # threshold
        gpu_thresholded = cle.greater_constant(gpu_blurred, constant= threshold * 10)

        # mask
        gpu_masked_spots = cle.mask(gpu_detected_maxima, gpu_thresholded)

        # label spots
        gpu_labelled_spots = cle.connected_components_labeling_box(gpu_masked_spots)

        number_of_spots = cle.maximum_of_all_pixels(gpu_labelled_spots)
        print("Number of detected spots: " + str(number_of_spots))

        # Expanding labelled spots
        # Next, we spatially extend the labelled spots by applying a maximum filter.

        # label map closing
        number_of_dilations = 10
        number_of_erosions = 4

        flip = cle.create_like(gpu_labelled_spots)
        flop = cle.create_like(gpu_labelled_spots)
        flag = cle.create([1,1,1])
        cle.copy(gpu_labelled_spots, flip)

        for i in range (0, number_of_dilations) :
            cle.onlyzero_overwrite_maximum_box(flip, flag, flop)
            cle.onlyzero_overwrite_maximum_diamond(flop, flag, flip)

        flap = cle.greater_constant(flip, constant= 1)

        for i in range(0, number_of_erosions):
            cle.erode_box(flap, flop)
            cle.erode_sphere(flop, flap)

        gpu_labels = cle.mask(flip, flap)

        output = cle.pull(gpu_labels)
        return output

# Start up napari
import napari

with napari.gui_qt():
    viewer = napari.Viewer()
    viewer.add_image(image, name='Tribolium')

    gui = workflow.Gui()
    viewer.window.add_dock_widget(gui)
