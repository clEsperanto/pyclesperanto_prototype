# py-clesperanto
[![Image.sc forum](https://img.shields.io/badge/dynamic/json.svg?label=forum&url=https%3A%2F%2Fforum.image.sc%2Ftag%2Fclesperanto.json&query=%24.topic_list.tags.0.topic_count&colorB=brightgreen&suffix=%20topics&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAABPklEQVR42m3SyyqFURTA8Y2BER0TDyExZ+aSPIKUlPIITFzKeQWXwhBlQrmFgUzMMFLKZeguBu5y+//17dP3nc5vuPdee6299gohUYYaDGOyyACq4JmQVoFujOMR77hNfOAGM+hBOQqB9TjHD36xhAa04RCuuXeKOvwHVWIKL9jCK2bRiV284QgL8MwEjAneeo9VNOEaBhzALGtoRy02cIcWhE34jj5YxgW+E5Z4iTPkMYpPLCNY3hdOYEfNbKYdmNngZ1jyEzw7h7AIb3fRTQ95OAZ6yQpGYHMMtOTgouktYwxuXsHgWLLl+4x++Kx1FJrjLTagA77bTPvYgw1rRqY56e+w7GNYsqX6JfPwi7aR+Y5SA+BXtKIRfkfJAYgj14tpOF6+I46c4/cAM3UhM3JxyKsxiOIhH0IO6SH/A1Kb1WBeUjbkAAAAAElFTkSuQmCC)](https://forum.image.sc/tag/clesperanto)
[![website](https://img.shields.io/website?url=http%3A%2F%2Fclesperanto.net)](http://clesperanto.net)
[![PyPI](https://img.shields.io/pypi/v/pyclesperanto-prototype.svg?color=green)](https://pypi.org/project/pyclesperanto-prototype)
[![Contributors](https://img.shields.io/github/contributors-anon/clEsperanto/pyclesperanto_prototype)](https://github.com/clEsperanto/pyclesperanto_prototype/graphs/contributors)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/pyclesperanto_prototype)](https://pypistats.org/packages/pyclesperanto_prototype)
[![GitHub stars](https://img.shields.io/github/stars/clEsperanto/pyclesperanto_prototype?style=social)](https://github.com/clEsperanto/pyclesperanto_prototype/)
[![GitHub forks](https://img.shields.io/github/forks/clEsperanto/pyclesperanto_prototype?style=social)](https://github.com/clEsperanto/pyclesperanto_prototype/)
[![License](https://img.shields.io/pypi/l/pyclesperanto_prototype.svg?color=green)](https://github.com/haesleinhuepf/pyclesperanto_prototype/raw/master/LICENSE)
[![Python Version](https://img.shields.io/pypi/pyversions/pyclesperanto-prototype.svg?color=green)](https://python.org)
[![tests](https://github.com/clesperanto/pyclesperanto_prototype/workflows/tests/badge.svg)](https://github.com/clesperanto/pyclesperanto_prototype/actions)
[![codecov](https://codecov.io/gh/clesperanto/pyclesperanto_prototype/branch/master/graph/badge.svg)](https://codecov.io/gh/clesperanto/pyclesperanto_prototype)
[![Development Status](https://img.shields.io/pypi/status/pyclesperanto_prototype.svg)](https://en.wikipedia.org/wiki/Software_release_life_cycle#Alpha)
[![DOI](https://zenodo.org/badge/248206619.svg)](https://zenodo.org/badge/latestdoi/248206619)

py-clesperanto is a prototype for [clesperanto](http://clesperanto.net) - a multi-platform multi-language framework for GPU-accelerated image processing. 
We mostly use it in the life sciences for analysing 3/4-dimensional microsopy data, e.g. as we face it developmental biology when segmenting cells and studying
their individual properties as well as properties of compounds of cells forming tissues.

![](https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/banner.png)
<small>Image data source: Daniela Vorkel, Myers lab, MPI-CBG, rendered using [napari](https://github.com/napari/napari) </small>

clesperanto uses [OpenCL kernels](https://github.com/clEsperanto/clij-opencl-kernels/tree/development/src/main/java/net/haesleinhuepf/clij/kernels) from [CLIJ](http://clij.github.io/).
Since version 0.11.1 py-clesperanto comes with a yet experimental [cupy](https://cupy.dev)-based [CUDA](https://en.wikipedia.org/wiki/CUDA) backend.

For users convenience, there are code generators available for [napari](https://clesperanto.github.io/napari_pyclesperanto_assistant/) and [Fiji](https://clij.github.io/assistant/).
Also check out the [napari workflow optimizer](https://github.com/haesleinhuepf/napari-workflow-optimizer) for semi-automatic parameter tuning of clesperanto-functions.

## Reference
The [full reference](https://clij.github.io/clij2-docs/reference__pyclesperanto) is available as part of the CLIJ2 documentation.

## Installation
* Get a python environment, e.g. via [mini-conda](https://docs.conda.io/en/latest/miniconda.html). If you never used python/conda environments before, please follow the instructions [here](https://mpicbg-scicomp.github.io/ipf_howtoguides/guides/Python_Conda_Environments) first.
* Install [pyopencl](https://documen.tician.de/pyopencl/), e.g. via conda:

```
conda install -c conda-forge pyopencl
```

Afterwards, install py-clesperanto using pip:

```
pip install pyclesperanto-prototype
```

## Example code
A basic image procressing workflow loads blobs.gif and counts the number of gold particles:

```python
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

[Counting blobs](http://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/basics/count_blobs.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/voronoi_otsu_labeling.png" width="300"/>

</td><td>

[Voronoi-Otsu labeling](http://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/segmentation/voronoi_otsu_labeling.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/segmentation_3d.png" width="300"/>

</td><td>

[3D Image segmentation ](http://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/segmentation/Segmentation_3D.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/segmentation_2d_membranes.png" width="300"/>

</td><td>

[Cell segmentation based on membranes](http://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/segmentation/segmentation_2d_membranes.ipynb)

</td></tr>

<tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/bead_segmentation.png" width="300"/>

</td><td>

[Detecting beads and measuring their size](http://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/segmentation/bead_segmentation.ipynb)

</td></tr>

<tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/label_statistics.png" width="300"/>

</td><td>

[Label statistics](http://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/basics/label_statistics.ipynb)

</td></tr>

<tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/parametric_maps.png" width="300"/>

</td><td>

[Parametric maps](http://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/tissues/parametric_maps.ipynb)

</td></tr>


<tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/screenshot_crop_and_paste_images.png" width="300"/>

</td><td>

[Crop and paste images](http://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/basics/crop_and_paste_images.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/screenshot_inspecting_3d_images.png" width="300"/>

</td><td>

[Inspecting 3D image data](http://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/basics/inspecting_3d_images.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/screenshot_affine_transforms.png" width="300"/>

</td><td>

[Rotation, scaling, translation, affine transforms](http://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/transforms/affine_transforms.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/screenshot_multiply_vectors_and_matrices.png" width="300"/>

</td><td>

[Multiply vectors and matrices](http://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/basics/multiply_vectors_and_matrices.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/screenshot_multiply_matrices.png" width="300"/>

</td><td>

[Matrix multiplication](http://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/basics/multiply_matrices.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/screenshot_spots_pointlists_matrices_tables.png" width="300"/>

</td><td>

* [Working with spots, pointlist and matrices](http://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/basics/spots_pointlists_matrices_tables.ipynb)
* [Lists of nonzero pixel coordinates](http://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/basics/nonzero.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/mesh_between_centroids.png" width="300"/>

</td><td>

[Mesh between centroids](http://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/neighbors/mesh_between_centroids.ipynb)

</td></tr><tr><td>


<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/mesh_between_touching_neighbors.png" width="300"/>

</td><td>

[Mesh between touching neighbors](http://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/neighbors/mesh_between_touching_neighbors.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/mesh_with_distances.png" width="300"/>

</td><td>

[Mesh with distances](http://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/neighbors/mesh_with_distances.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/mesh_nearest_neighbors.png" width="300"/>

</td><td>

[Mesh nearest_neighbors](http://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/neighbors/mesh_nearest_neighbors.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/ipgraph_networkx.png" width="300"/>

</td><td>

[Export to igraph and networkx](http://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/neighbors/ipgraph_networkx.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/neighborhood_definitions.png" width="300"/>

</td><td>

[Neighborhood definitions](http://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/neighbors/neighborhood_definitions.ipynb)


</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/tissue_neighborhood_quantification.png" width="300"/>

</td><td>

[Tissue neighborhood quantification](http://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/tissues/tissue_neighborhood_quantification.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/neighbors_of_neighbors.png" width="300"/>

</td><td>

[Neighbors of neighbors](http://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/neighbors/neighbors_of_neighbors.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/screenshot_voronoi_diagrams.png" width="300"/>

</td><td>

[Voronoi diagrams](http://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/basics/voronoi_diagrams.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/shape_descriptors_based_on_neighborhood_graphs.png" width="300"/>

</td><td>

[Shape descriptors based on neighborhood graphs](http://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/neighbors/shape_descriptors_based_on_neighborhood_graphs.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/distance_to_other_labels.png" width="300"/>

</td><td>

[Measuring distances between labels in two label images](http://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/neighbors/distance_to_other_labels.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/screenshot_tribolium_napari.png" width="300"/>

</td><td>

[Tribolium morphometry + Napari](https://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/tribolium_morphometry/tribolium.py)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/screenshot_tribolium_morphometry.png" width="300"/>

</td><td>

[Tribolium morphometry](http://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/tribolium_morphometry/tribolium_morphometry.ipynb)

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/screenshot_napari_dask.png" width="300"/>

</td><td>

[napari+dask timelapse processing](http://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/napari_gui/napari_dask.ipynb)

</td></tr>
</table>

## Technical insights

<table border="0"><tr><td>
<tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/browse_operations.png" width="300"/>

</td><td>

[Browsing operations](http://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/basics/browse_operations.ipynb)

</td></tr>
<tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/interactive_widgets.gif" width="300"/>

</td><td>

[Interactive widgets](https://colab.research.google.com/github/clEsperanto/pyclesperanto_prototype/tree/master/demo/basics/browse_operations.ipynb)

</td></tr>
<tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/optimize_blobs_segmentation.png" width="300"/>

</td><td>

[Automatic workflow optimization](https://colab.research.google.com/github/clEsperanto/pyclesperanto_prototype/tree/master/demo/optimization/optimize_blobs_segmentation.ipynb)

</td></tr>

<tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/switching_gpus.png" width="300"/>

</td><td>

[Exploring and switching between GPUs](http://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/basics/switching_gpus.ipynb)

</td></tr>
<tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/cupy_compatibility.png" width="300"/>

</td><td>

[Interoperability with cupy](http://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/basics/interoperability_cupy.ipynb)

[Using the cupy backend](http://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/basics/select_backend.ipynb)

</td></tr>
</table>

## Related projects

<table border="0"><tr><td>

<img src="https://github.com/clesperanto/napari_pyclesperanto_assistant/raw/master/docs/images/screenshot.png" width="300"/>

</td><td>

[napari-pyclesperanto-assistant](https://github.com/clesperanto/napari_pyclesperanto_assistant):
A graphical user interface for general purpose GPU-accelerated image processing and analysis in napari.

</td></tr><tr><td>

<img src="https://github.com/haesleinhuepf/napari-accelerated-pixel-and-object-classification/raw/main/images/screenshot.png" width="300"/>

</td><td>

[napari-accelerated-pixel-and-object-classification](https://github.com/haesleinhuepf/napari-accelerated-pixel-and-object-classification):
GPU-accelerated Random Forest Classifiers for pixel and labeled object classification

</td></tr><tr><td>

<img src="https://github.com/clEsperanto/pyclesperanto_prototype/raw/master/docs/images/napari-clusters-plotter.png" width="300"/>

</td><td>

[napari-clusters-plotter](https://github.com/BiAPoL/napari-clusters-plotter):
Clustering of objects according to their quantitative properties

</td></tr></table>

## Benchmarking
We implemented some basic benchmarking notebooks allowing to see performance differences between pyclesperanto and 
some other image processing libraries, typically using the CPU. Such benchmarking results vary heavily depending on 
image size, kernel size, used operations, parameters and used hardware. Feel free to use those notebooks, adapt them to 
your use-case scenario and benchmark on your target hardware. If you have different scenarios or use-cases, you are very 
welcome to submit your notebook as pull-request!

* [Affine transforms](http://github.com/clEsperanto/pyclesperanto_prototype/blob/master/benchmarks/affine_transforms.ipynb)
* [Background subtraction](http://github.com/clEsperanto/pyclesperanto_prototype/blob/master/benchmarks/top_hat.ipynb)
* [Gaussian blur](http://github.com/clEsperanto/pyclesperanto_prototype/blob/master/benchmarks/gaussian_blur.ipynb)
* [Convolution](http://github.com/clEsperanto/pyclesperanto_prototype/blob/master/benchmarks/convolution.ipynb)
* [Otsu's thresholding](http://github.com/clEsperanto/pyclesperanto_prototype/blob/master/benchmarks/threshold_otsu.ipynb)
* [Connected component labeling](http://github.com/clEsperanto/pyclesperanto_prototype/blob/master/benchmarks/connected_component_labeling.ipynb)  
* [Extend labels](http://github.com/clEsperanto/pyclesperanto_prototype/blob/master/benchmarks/extend_labels.ipynb)
* [Statistics of labeled pixels / regionprops](http://github.com/clEsperanto/pyclesperanto_prototype/blob/master/benchmarks/statistics_of_labeled_pixels.ipynb)
* [Histograms](http://github.com/clEsperanto/pyclesperanto_prototype/blob/master/benchmarks/histograms.ipynb)
* [Matrix multiplication](http://github.com/clEsperanto/pyclesperanto_prototype/blob/master/benchmarks/matrix_multiplication.ipynb)
* [Pixel-wise comparison](http://github.com/clEsperanto/pyclesperanto_prototype/blob/master/benchmarks/pixelwise_comparison.ipynb)
* [Intensity projections](http://github.com/clEsperanto/pyclesperanto_prototype/blob/master/benchmarks/intensity_projections.ipynb)
* [Axis transposition](http://github.com/clEsperanto/pyclesperanto_prototype/blob/master/benchmarks/transpose.ipynb)
* [Nonzero](http://github.com/clEsperanto/pyclesperanto_prototype/blob/master/benchmarks/nonzero.ipynb)

## See also
There are other libraries for code acceleration and GPU-acceleration for image processing.
* [numba](https://numba.pydata.org/)
* [cupy](https://cupy.dev)
* [cucim](https://github.com/rapidsai/cucim)
* [clij](https://clij.github.io)

## Feedback welcome!
clesperanto is developed in the open because we believe in the open source community. See our [community guidelines](https://clij.github.io/clij2-docs/community_guidelines). Feel free to drop feedback as [github issue](https://github.com/clEsperanto/pyclesperanto_prototype/issues) or via [image.sc](https://image.sc)
