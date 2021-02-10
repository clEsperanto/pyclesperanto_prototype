import pyclesperanto_prototype as cle
print("Using GPU", cle.get_device())

# load data (download it from https://git.mpi-cbg.de/rhaase/clij2_example_data/-/blob/master/lund1051_resampled.tif
from skimage.io import imread
image = imread('lund1051_resampled.tif')

import time
def stopwatch(text):
    print(text, " takes time: ", time.time() - stopwatch.start_time, " s")
    stopwatch.start_time = time.time()

stopwatch.start_time = time.time()

# start up napari
import napari
with napari.gui_qt():
    viewer = napari.Viewer(ndisplay=3)
    viewer.add_image(image, name='input')
    stopwatch("Startup")

    # push image to GPU
    input = cle.push(image)
    stopwatch("pushing")

    # process the image + kernel compilation (warmup effect)
    intermediate = cle.top_hat_box(input, radius_x=5, radius_y=5, radius_z=5)
    result = cle.voronoi_otsu_labeling(intermediate, spot_sigma=1, outline_sigma=2)
    stopwatch("warmup")

    # process the image
    intermediate = cle.top_hat_box(input, radius_x=5, radius_y=5, radius_z=5)
    result = cle.voronoi_otsu_labeling(intermediate, spot_sigma=1, outline_sigma=2)
    stopwatch("image processing")

    # add it to napari
    viewer.add_image(cle.pull(intermediate))
    stopwatch("Showing background subtracted input in napari")
    viewer.add_labels(result)
    stopwatch("Showing the result in napari")

