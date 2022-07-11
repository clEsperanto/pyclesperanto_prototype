import pyclesperanto_prototype as cle

from skimage.io import imread, imsave

# initialize GPU
device = cle.select_device("GTX")
print("Used GPU: ", device)

# load data
image = imread('https://imagej.nih.gov/ij/images/blobs.gif')

# process the image
inverted = cle.subtract_image_from_scalar(image, scalar=255)
blurred = cle.gaussian_blur(inverted, sigma_x=1, sigma_y=1)
binary = cle.threshold_otsu(blurred)
labeled = cle.connected_components_labeling_box(binary)

# The maxmium intensity in a label image corresponds to the number of objects
num_labels = cle.maximum_of_all_pixels(labeled)

# print out result
print("Num objects in the image: " + str(num_labels))

# save image to disc
imsave("result.tif", cle.pull(labeled))