# pyclesperanto
pyclesperanto is a prototype for [clEsperanto](http://clesperanto.net) - a multi-platform multi-language framework for GPU-accelerated image processing. 
It uses [OpenCL kernels](https://github.com/clEsperanto/clij-opencl-kernels/tree/development/src/main/java/net/haesleinhuepf/clij/kernels) from [CLIJ](http://clij.github.io/).

For users convenience, there are code generators available for [napari](https://clesperanto.github.io/napari_pyclesperanto_assistant/) and [Fiji](https://clij.github.io/assistant/).

![](https://clesperanto.github.io/napari_pyclesperanto_assistant/docs/images/screenshot_5.png)

## Reference
The [full reference](https://clij.github.io/clij2-docs/reference__pyclesperanto) is available as part of the CLIJ2 documentation.

## Installation
* Get a python environment, e.g. via [mini-conda](https://docs.conda.io/en/latest/miniconda.html). If you never used python/conda environments before, please follow the instructions [here](https://mpicbg-scicomp.github.io/ipf_howtoguides/guides/Python_Conda_Environments) first.
* Install [pyopencl](https://documen.tician.de/pyopencl/). 

If installation of pyopencl for Windows fails, consider downloading a precompiled wheel (e.g. from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyopencl) ) and installing it manually. Note that "cl12" and "cp38" in the filename matter: They allow you using OpenCL 1.2 compatible GPU devices from Python 3.8.

```
pip install pyopencl-2019.1.1+cl12-cp37-cp37m-win_amd64.whl
```
Alternatively, installing via conda also works:
```
conda install -c conda-forge pyopencl=2020.3.1
```

Afterwards, install pyclesperanto:

```
pip install pyclesperanto-prototype
```

### Troubleshooting installation
If you receive an error like 
```
DLL load failed: The specified procedure could not be found.
```
Try downloading and installing a pyopencl with a lower cl version, e.g. cl12 : pyopencl-2020.1+cl12-cp37-cp37m-win_amd64

## Example code
A basic image procressing workflow loads blobs.gif and counts the number of gold particles:

```python
import pyclesperanto_prototype as cle

from skimage.io import imread, imsave

# initialize GPU
cle.select_device("GTX")
print("Used GPU: " + cle.get_device().name)

# load data
image = imread('https://imagej.nih.gov/ij/images/blobs.gif')
print("Loaded image size: " + str(image.shape))

# push image to GPU memory
input = cle.push(image)
print("Image size in GPU: " + str(input.shape))

# process the image
inverted = cle.subtract_image_from_scalar(image, scalar=255)
blurred = cle.gaussian_blur(inverted, sigma_x=1, sigma_y=1)
binary = cle.threshold_otsu(blurred)
labeled = cle.connected_components_labeling_box(binary)

# The maxmium intensity in a label image corresponds to the number of objects
num_labels = cle.maximum_of_all_pixels(labeled)

# print out result
print("Num objects in the image: " + str(num_labels))

# for debugging: print out image
print(labeled)

# for debugging: save image to disc
imsave("result.tif", cle.pull(labeled))
```

## Example gallery 

<table border="0">
<tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/screenshot_select_GPU.png" width="300"/>

</td><td>

[Select GPU](https://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/basics/select_GPU.py)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/screenshot_count_blobs.png" width="300"/>

</td><td>

[Counting blobs](https://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/basics/count_blobs.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/screenshot_crop_and_paste_images.png" width="300"/>


</td><td>

[Crop and paste images](https://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/basics/crop_and_paste_images.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/screenshot_inspecting_3d_images.png" width="300"/>

</td><td>

[Inspecting 3D image data](https://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/basics/inspecting_3d_images.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/screenshot_affine_transforms.png" width="300"/>

</td><td>

[Rotation, scaling, translation, affine transforms](https://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/transforms/affine_transforms.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/screenshot_multiply_vectors_and_matrices.png" width="300"/>

</td><td>

[Multiply vectors and matrices](https://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/basics/multiply_vectors_and_matrices.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/screenshot_multiply_matrices.png" width="300"/>

</td><td>

[Matrix multiplication](https://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/basics/multiply_matrices.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/screenshot_spots_pointlists_matrices_tables.png" width="300"/>

</td><td>

[Working with spots, pointlist and matrices](https://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/basics/spots_pointlists_matrices_tables.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/mesh_between_centroids.png" width="300"/>

</td><td>

[Mesh between centroids](https://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/neighbors/mesh_between_centroids.ipynb)

</td></tr><tr><td>


<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/mesh_between_touching_neighbors.png" width="300"/>

</td><td>

[Mesh between touching neighbors](https://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/neighbors/mesh_between_touching_neighbors.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/mesh_with_distances.png" width="300"/>

</td><td>

[Mesh with distances](https://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/neighbors/mesh_with_distances.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/mesh_nearest_neighbors.png" width="300"/>

</td><td>

[Mesh nearest_neighbors](https://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/neighbors/mesh_nearest_neighbors.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/neighborhood_definitions.png" width="300"/>

</td><td>

[Neighborhood definitions](https://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/neighbors/neighborhood_definitions.ipynb)


</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/tissue_neighborhood_quantification.png" width="300"/>

</td><td>

[Tissue neighborhood quantification](https://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/tissues/tissue_neighborhood_quantification.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/neighbors_of_neighbors.png" width="300"/>

</td><td>

[Neighbors of neighbors](https://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/neighbors/neighbors_of_neighbors.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/screenshot_voronoi_diagrams.png" width="300"/>

</td><td>

[Voronoi diagrams](https://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/basics/voronoi_diagrams.ipynb)

</td></tr><tr><td>

</td><td>

[Shape descriptors based on neighborhood graphs](https://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/neighbors/shape_descriptors_based_on_neighborhood_graphs.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/screenshot_tribolium_napari.png" width="300"/>

</td><td>

[Tribolium morphometry + Napari](https://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/tribolium_morphometry/tribolium.py)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/screenshot_tribolium_morphometry.png" width="300"/>

</td><td>

[Tribolium morphometry](https://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/tribolium_morphometry/tribolium_morphometry.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/screenshot_napari_dask.png" width="300"/>

</td><td>

[napari+dask timelapse processing](https://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/napari_gui/napari_dask.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clesperanto/napari_pyclesperanto_assistant/raw/master/docs/images/screenshot.png" width="300"/>

</td><td>

[pyclesperanto assistant](https://github.com/clesperanto/napari_pyclesperanto_assistant)

</td></tr></table>





## Feedback welcome!
clEsperanto is developed in the open because we believe in the [open source community](https://clij.github.io/clij2-docs/community_guidelines). Feel free to drop feedback as [github issue](https://github.com/clEsperanto/pyclesperanto_prototype/issues) or via [image.sc](https://image.sc)
