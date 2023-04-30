import pyclesperanto_prototype as cle

from skimage.io import imread, imsave

# initialize GPU
cle.select_device("GTX")
print("Used GPU: " + cle.get_device().name)

# load data
image = imread('https://imagej.nih.gov/ij/images/blobs.gif')
print("Loaded image size: " + str(image.shape))

# process the image
inverted = cle.subtract_image_from_scalar(image, scalar=255)
blurred = cle.gaussian_blur(inverted, sigma_x=1, sigma_y=1)
binary = cle.threshold_otsu(blurred)
labeled = cle.connected_components_labeling_box(binary)

# The maximium intensity in a label image corresponds to the number of objects
num_labels = labeled.max()
print("Num objects in the image: " + str(num_labels))

# for debugging: print out image
print(labeled)

# for debugging: save image to disc
imsave("result.tif", labeled)
