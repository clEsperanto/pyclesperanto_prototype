filename = "data/mini-t1-head.tif"


import clesperanto as cle
from skimage import io
import napari

#2d image
blobs=io.imread('https://imagej.nih.gov/ij/images/blobs.gif')
cle_blobs = cle.push(blobs)
thresholded=cle.create(cle_blobs.shape)
cle.apply_threshold(cle_blobs,thresholded,threshold=125)
blobs_result = cle.pull(thresholded)

print("processing 2d image")
fly_3d=io.imread(filename)
cle_fly_3d = cle.push(fly_3d)
thresholded=cle.create(cle_fly_3d.shape)
cle.apply_threshold(cle_fly_3d,thresholded,threshold=200)
fly3d_result = cle.pull(thresholded)

with napari.gui_qt():
    viewer = napari.Viewer()
    viewer.add_image(blobs,name='blobs')
    viewer.add_image(blobs_result,name='blobs_binary')
    viewer.add_image(fly_3d,name='Fly_3d')
    viewer.add_image(fly3d_result,name='fly3d_binary')
