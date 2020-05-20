# config
filename = "data/mini-t1-head.tif"

from skimage.io import imread
import clesperanto as cle
import numpy as np
import napari


test = cle.push(np.asarray([
[1, 1, 1],
[1, 2, 1],
[1, 1, 1]
#    [1, 1, 1, 1, 1, 1, 1],
#    [1, 1, 1, 1, 1, 1, 1],
#    [1, 1, 1, 1, 1, 1, 1],
#    [1, 1, 1, 2, 1, 1, 1],
#    [1, 1, 1, 1, 1, 1, 1],
#    [1, 1, 1, 1, 1, 1, 1],
#    [1, 1, 1, 1, 1, 1, 1]
]))

test2 = cle.create(test)
# cle.set(test2, 4);

print("A test")
print(cle.pull(test))

print("A test2")
print(cle.pull(test2))


cle.maximum_sphere(test, test2, 1, 1, 1)

print("B test")
print(cle.pull(test))

print("B test2")
print(cle.pull(test2))




# test = cle.create((5,4,3))
cle.set(test, 5)
#print(test)
#print(cle.pull(test))

a = cle.pull(test)
assert (np.min(a) == 5)
assert (np.max(a) == 5)
assert (np.mean(a) == 5)

print ("ok")
# quit()

# load data and allocate memory for result
fly = imread(filename)
cle_fly = cle.push(fly);

print("pulled: ")
print(cle.pull(cle_fly))

background_subtracted_fly = cle.create(cle_fly.shape)

# subtract background
cle.top_hat_sphere(cle_fly, background_subtracted_fly, 15, 15, 0)

result = cle.pull(background_subtracted_fly);
print(result)
# show results
with napari.gui_qt():
    viewer = napari.Viewer()
    viewer.add_image(result);















# hangs on windows :-(
# result = np.copy(background_subtracted_fly)
