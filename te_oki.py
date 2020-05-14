# config
filename = "C:/structure/data/2018-05-23-16-18-13-89-Florence_multisample/processed/tif/000300.raw.tif"

from skimage.io import imread
import clesperanto as cle
import napari

# load data and allocate memory for result
fly = imread(filename)
cle_fly = cle.push(fly);

print(cle_fly.shape)
background_subtracted_fly = cle.create(cle_fly.shape)

# subtract background
cle.top_hat_sphere(cle_fly, background_subtracted_fly, 0, 15, 15)

result = cle.pull(background_subtracted_fly);
print(result)
# show results
# with napari.gui_qt():
#    viewer = napari.Viewer()
#    viewer.add_image(, contrast_limits=(0,500));















# hangs on windows :-(
# result = np.copy(background_subtracted_fly)
