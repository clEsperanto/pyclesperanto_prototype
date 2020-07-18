import pyclesperanto_prototype as cle
print(cle.get_gpu_name())

# load data
from skimage.io import imread
image = imread('C:/structure/teaching/clij2_example_data/lund1051_resampled.tif')
print(image.shape)




## Load a data set
# The dataset is available online:
# https://git.mpi-cbg.de/rhaase/clij2_example_data/blob/master/lund1051_resampled.tif
# It shows a Tribolium castaneum embryo, imaged by a custom light sheet microscope,
# at a wavelength of 488nm (Imaging credits: Daniela Vorkel, Myers lab, MPI CBG).
# The data set has been resampled to a voxel size of 1x1x1 microns. The embryo
# expresses nuclei-GFP. We will use the dataset to detect nuclei and to generate
# an estimated cell-segmentation.

def mesh_data(gpu_input, sigma : float = 2.0, threshold : float = 300):

    # Spot detection
    # After some noise removal/smoothing, we perform a local maximum detection

    # gaussian blur
    gpu_blurred = cle.gaussian_blur(gpu_input, sigma_x=sigma, sigma_y=sigma, sigma_z=sigma)

    # detect maxima
    gpu_detected_maxima = cle.detect_maxima_box(gpu_blurred)

    # Spot curation
    # Now, we remove spots with values below a certain intensity and label the remaining spots

    # threshold
    gpu_thresholded = cle.greater_constant(gpu_blurred, scalar = threshold)

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

    flap = cle.greater_constant(flip, scalar = 1)

    for i in range(0, number_of_erosions):
        cle.erode_box(flap, flop)
        cle.erode_sphere(flop, flap)

    gpu_labels = cle.mask(flip, flap)

    # Draw connectivity of the cells as a mesh¶
    # We then read out all current positions of detected nuclei as a pointlist to
    # generate a distance matrix of all nuclei towards each other:

    gpu_pointlist = cle.labelled_spots_to_pointlist(gpu_labelled_spots);
    gpu_distance_matrix = cle.generate_distance_matrix(gpu_pointlist, gpu_pointlist);
    gpu_touch_matrix = cle.generate_touch_matrix(gpu_labels)

    # touch matrix:
    # set the first column to zero to ignore all spots touching the background
    # (background label 0, first column)
    cle.set_column(gpu_touch_matrix, 0, 0)

    # create memory for the pixelated mesh
    gpu_mesh = cle.create_like(gpu_input)

    cle.touch_matrix_to_mesh(gpu_pointlist, gpu_touch_matrix, gpu_mesh)

    return gpu_mesh



def napari():

    import napari
    from magicgui import magicgui
    from napari.layers import Image



    with napari.gui_qt():
        viewer = napari.Viewer()
        viewer.add_image(image, name='Tribolium')


        # use auto_call=True for instantaneous execution
        # can add sliders using QSlider, but need to show values
        @magicgui(call_button='Compute')
        def clij_filter(input: Image, sigma=2, threshold : float = 300) -> Image:
            if input:
                # push image to GPU memory and show it
                gpu_input = cle.push_zyx(input.data)

                gpu_output = mesh_data(gpu_input, sigma, threshold)

                output = cle.pull_zyx(gpu_output)
                return output


        # use of magic_gui also passes an attribute to clij_operation  "called"
        # def print_shape(image):
        # print('Output image shape ', image.shape)

        gui = clij_filter.Gui()
        viewer.window.add_dock_widget(gui)
        # if a layer gets added or removed, refresh the dropdown choices
        viewer.layers.events.changed.connect(lambda x: gui.refresh_choices("input"))

        # clij_operation.called.connect(print_shape)


gpu_input = cle.push_zyx(image)

import cProfile

#cProfile.run('mesh_data(gpu_input, 2, 300)')

import time
time_stamp = time.time()
gpu_output = mesh_data(gpu_input, 2, 300)
print("First round took " + str((time.time() - time_stamp) * 1000) + " ms")

time_stamp = time.time()
gpu_output = mesh_data(gpu_input, 2, 300)
print("Second round took " + str((time.time() - time_stamp) * 1000) + " ms")
