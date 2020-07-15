# config
filename = "data/mini-t1-head.tif"

from skimage.io import imread
import pyclesperanto_prototype as cle
import numpy as np

# load data and allocate memory for result
fly = imread(filename)
cle_fly = cle.push(fly);

#print("pulled: ")
#print(cle.pull(cle_fly))

background_subtracted_fly = cle.create(cle_fly.shape)

# subtract background
cle.top_hat_sphere(cle_fly, background_subtracted_fly, 15, 15, 0)

result = cle.pull(background_subtracted_fly);

assert (np.min(result) == 0)
assert (np.max(result) != 0)
assert (np.mean(result) != 0)
print("ok top_hat_sphere")

#print(result)
# show results
#with napari.gui_qt():
#    viewer = napari.Viewer()
#    viewer.add_image(result);


