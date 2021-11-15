# 0.11.0

## New features
* This version introduces an experimental `cupy` backend. Install [cupy](https://cupy.dev/) and run `cle.select_device('cupy')` to test it. 
  This feature is experimental yet, please use it with care. These functions are known to cause issues with the cupy backend: 
  * affine_transform (linear interpolation not supported), 
  * apply_vector_field (linear interpolation not supported), 
  * create(uint64), create(int32), create(int64), 
  * label_spots, 
  * labelled_spots_to_pointlist, 
  * resample (linear interpolation not supported),  
  * scale (linear interpolation not supported), 
  * spots_to_pointlist

## API deprecations
* The following parameters of `execute()` are deprecated:
  * `image_size_independent_kernel_compilation` (will always be True in the future), 
  * `prog` (will no longer be supported, use [pyopencl](https://documen.tician.de/pyopencl/) for those kinds of features) and 
  * `device` (will no longer be supported, use pyopencl instead)

# 0.10.9 - November 11th 2021

## New features
* deployment switched from setup.py to setup.cfg

# 0.10.8 - November 6th 2021

## New features
* `standard_deviation_box` / `standard_deviation_sphere` filters (Thanks to Lucrezia Ferme @lcferme and Allyson Ryan @allysonryan for suggesting)

## Bugfixes
* Kernels were crashing when calling `y = x * x.max()` in case `x` was a GPU-backed image of type uint16 (and others).

# 0.10.7 - October 30th 2021
## New features
* `imshow` has a new optional parameter: `colorbar`
* added `label_nonzero_pixel_count_map`
* added `label_nonzero_pixel_count_ratio_map`
* added `label_overlap_count_map`

## Bug fixes
* `imshow` uses the same colormap when visualizing label images

# 0.10.5 - October 29th 2021
## Bug fixes
* imshow(numpy array) crashed

# 0.10.4 - October 26th 2021
## Bug fixes
* scikit-image regionprops crashed when passing a pyclesperanto labels image

# 0.10.0 - August 15th 2021
## New features
* It is now possible to read and write pixels in images using the syntax `image[([z1,z2], [y1,y2], [x1,x2])] = new_value`

## Bug fixes
* When importing `pyclesperanto_prototype`, some functions in `pyopencl` stopped working (see [#130](https://github.com/clEsperanto/pyclesperanto_prototype/issues/130)) (Thanks to Peter Sobolewski for reporting and Talley Lambert for support while fixing)
* Operations crashed when a [dask](https://dask.org/) array was handed over as image parameter. That can happen in napari for example when opening CZI files.
* z-position projections automatically created output images had a wrong size (x and y switched).

## Backwards compatiblity breaking changes
* Instead of manipulating internal sturctures of pyopencl (in particular `cl.array.Array`), we now ship an own image class, `OCLArray`. 
  Thus, it is possible that operators directly applied to images produced by pyclesperanto don't work anymore. 
  If you experience any issues, [please report them](https://github.com/clEsperanto/pyclesperanto_prototype/issues).

# 0.9.9 - August 1st 2021
## New features
* `relabel_sequential`, similar to scikit-image (formely known as `close_index_gaps_in_label_maps`)
* `erode_labels`
* `extend_labels_with_maximum_radius` has been renamed to `dilate_labels`, an alias to the old method is kept as well
* `exclude_small_labels` as shortcut / convenience function to `exclude_labels_out_of_size_range`
* `exclude_large_labels` as shortcut / convenience function to `exclude_labels_out_of_size_range`
* `search_operation_names` for searching in the clesperanto API

## Bug fixes
* Switching GPUs using `select_device` made operations fail that were executed before switching ([#110](https://github.com/clEsperanto/pyclesperanto_prototype/issues/110))

# 0.9.7 - July 15th 2021
## Bug fixes
* `multiply_matrix` wasn't capable of creating / allocating memory for an output image 

# 0.9.5 - July 11th 2021
## Bug fixes
* `skimage.io.imsave` caused errors with oclarrays, also in napari
* `standard_deviation_z_projection` had wrong output size per default

## New features
* `median_box`
* `median_sphere`
* `extended_depth_of_focus_variance_projection`  
* `variance_box` filter
* `variance_sphere` filter
* `z_position_of_maximum_z_projection` and alias `arg_maximum_z_projection`
* `z_position_of_minimum_z_projection` and alias `arg_minimum_z_projection`
* `z_position_projection`
* `z_position_range_projection`

## Miscellaneous
* `invert` was removed from the assistant user interface. It does not do the same as in ImageJ and/or scikit-image. Thus, it might change in the future. See also https://github.com/clEsperanto/pyclesperanto_prototype/issues/123
* better documentation for `threshold_otsu`, `voronoi_otsu_labeling` and minor others

# 0.9.4 - July 3rd 2021
## Bug fixes
* Relax dependencies: pyopencl-version is no longer pinned. This should simplify installation.

## New features
* Improved interoperability with [cupy](https://cupy.dev/). You can now process images from clesperanto and cupy using syntax like `result = cle_image + cupy_image`. Note: This will pull/push the image from cupy to clesperanto. Thus, it might not be very performant.
* More operations have been marked as compatible with the [assistant](https://www.napari-hub.org/plugins/napari-pyclesperanto-assistant).

# 0.9.2 - June 26th 2021
## New features
Added aliases for compatibility with [clij 2.5](https://clij.github.io/clij2-docs/clij25_transition_notes)
* added alias `dilate_labels` for `extend_labels_with_maximum_radius`
* added alias `mean_intensity_map` for `label_mean_intensity_map`
* added alias `mean_extension_map` for `label_mean_extension_map`
* added alias `maximum_extension_map` for `label_maximum_extension_map`
* added alias `extension_ratio_map` for `label_maximum_extension_ratio_map`
* added alias `maximum_intensity_map` for `label_maximum_intensity_map`
* added alias `minimum_intensity_map` for `label_minimum_intensity_map`
* added alias `pixel_count_map` for `label_pixel_count_map`
* added alias `standard_deviation_intensity_map` for `label_standard_deviation_intensity_map`

## Bug fixes
* The `touching_neighbor_count_map` does not count background as neighbor anymore.
* Removed debug traces in `exclude_labels_with_values_within_range`
* `mean_sphere` returned always `None`

## Miscellaneous 
* Standard-deviation-Z-projection is now shown in the assistant user interface


# 0.9.1 - May 19th 2021
## New features
* `cle.operations` now supports strings as parameters and lists of strings (as before)
* `cle.categories` returns all available categories which can be used in `cle.operations`

# 0.9.0 - May 16th 2021

## New features
* the `execute` function allows providing `None` as anchor. With this, you can execute custom open.cl files located anywhere.

## Backwards compatibility breaking changes / bug fixes
* `statistics_of_labelled_pixels` had some entries in the returned dictionary which contained misleading content. Those were removed: `bbox`, `centroid`, `weighted_centroid`
* `crop` returned a 3D image with one slice when asked to crop a 2D image.

# 0.8.0 - Apr 22nd 2021
## New features
* OpenCL-buffers support now operators such as `+`,`-`,`*`,`/`,`**`,`+=`,`-=`,`*=`,`/=`,`**=`,`<`,`>`,`<=`,`>=`,`==`,`!=` with second operand also OpenCL-buffer, numpy-array or scalar (int/float).
* OpenCL-buffers now also support min, max and sum with axes 0, 1 and 2.  
* Added aliases `asarray` for `push` and `nparray` for `pull`
* New operation `proximal_neighbor_count_map`

## Backwards compatibility breaking changes
* Operations producing label images now automatically generate outout-images of type uint16. Operations producing binary images now automatically produce output images of type uint8. In case this breaks pre-existing workflows, consider using `cle.create_like` to create output-images of type float, which was default before this version.

# 0.7.6 - Apr 11th 2021
## Bug fixes
* `sub_stack` threw an error when processing 2D images. It now warns and returns a copy.

<a name="#075"></a>
# 0.7.5 - Apr 4th 2021
## New Features
* `sub_stack`
* activated transforms and projections in the assistant GUI
* added warnings in case operations get parameters which can cause errors, e.g. scale factor = 0

## Bug fixes
* `merge_touching_labels` didn't work properly in case labels were circular connected.

<a name="#074"></a>
# 0.7.4 - Mar 27th 2021
## New Features
* `apply_vector_field` for warping images

## Bug fixes
* `mean_(x/y/z)_projection` parameter `destination` is now optional

<a name="#073"></a>
# 0.7.3 - Mar 26th 2021

## New features
* The `linear_interpolation` parameter in `affine_transform`, `rigid_transform`, `scale`, `translate` and `rotate` is now functional.

## Bug fixes
* Turned off interpolation in `imshow`
* `linear_interpolation=True` caused crashes on NVidida GPUs (#99).
* If `scale` was scaling to the image center (as per default) and the output image was not the same size as the input image, parts of the image might have been removed.

<a name="#070"></a>
# 0.7.0 - Jan 14th 2021

## New features
This update brings many new functions, highlighing affine-transforms (rotation, translation, scaling) and filters based 
on neighborhood relationships between labels. With those you can convolve measurements of cells in tissues based on their adjacency graph.
Furthermore, `centroids_of_labels`, `statistics_of_labelled_pixels` and `statistics_of_background_and_labelled_pixels` were GPU-accelerated.
The `statistics_of_*` functions, measure standard deviation of the intensity` now and results of these functions are 
dictionaries which contain the same measurements as in CLIJ2.

### New operations
* `affine_transform` (yet without shearing and with nearest-neighbor interpolation only for now)
* `centroids_of_background_and_labels`
* `detect_minima_box`
* `euclidean_distance_from_label_centroid_map`
* `generate_n_nearest_neighbors_matrix`
* `generate_proximal_neighbors_matrix` and alias `generate_distal_neighbors_matrix`
* `label_standard_deviation_intensity_map`
* `label_mean_extension_map`
* `label_maximum_extension_map`
* `label_maximum_extension_ratio_map`
* `masked_voronoi_labeling`
* `maximum_distance_of_n_shortest_distances`
* `maximum_distance_of_touching_neighbors`
* `maximum_of_n_nearest_neighbors_map`
* `maximum_of_proximal_neighbors_map` and alias `maximum_of_distal_neighbors_map`
* `maximum_of_touching_neighbors_map`
* `mean_of_n_nearest_neighbors_map`
* `mean_of_proximal_neighbors_map` and alias `alias mean_of_distal_neighbors_map`
* `mean_of_touching_neighbors_map`
* `merge_touching_labels`
* `minimum_distance_of_touching_neighbors`
* `minimum_of_n_nearest_neighbors_map`
* `minimum_of_proximal_neighbors_map` and alias `minimum_of_distal_neighbors_map`
* `minimum_of_touching_neighbors_map`
* `mode_of_n_nearest_neighbors_map`
* `mode_of_proximal_neighbors_map` and alias `mode_of_distal_neighbors_map`
* `mode_of_touching_neighbors_map`
* `point_index_list_to_touch_matrix`
* `read_intensities_from_map`
* `read_intensities_from_positions`
* `regionprops` (based on scikit-image)
* `rigid_transform`
* `rotate`
* `scale`
* `standard_deviation_of_n_nearest_neighbors_map`
* `standard_deviation_of_proximal_neighbors_map` and alias `standard_deviation_of_distal_neighbors_map`
* `standard_deviation_of_touching_neighbors_map`
* `statistics_of_image`
* `touch_matrix_to_adjacency_matrix`
* `translate`
* `voronoi_otsu_labeling`

### Backwards compatibility breaking changes
* `statistics_of_labelled_pixels` and `statistics_of_background_and_labelled_pixels` produce different output now. 
Instead of a scikit-image RegionProps objects, the produce a dictionary which contains lists of measurements. 
`push_regionprops_column` also works with the new output format. Consider updating your code to work with the 
dictionaries,e.g. `stats['area']` instead of `[s.area for s in stats]`. If not possible, use the new function 
`regionprops` retrieve results in the old format
* `n_closest_points` ignores the background position and the distance to labels themselves per default now. 
  Consider passing `ignore_background=False` and `ignore_self=False` to go back to former functionality.

### Deprecation warnings
* `resample` has been deprecated. Use `scale` instead.

### Bug fixes
* `imshow` in 3D caused an error
* `push_regionprops_column` didn't actually push

### Miscellaneous
* `flag_existing_intensities` has been renamed to `flag_existing_labels`. An alias to the old method was created to keep backwards-compatibility

<a name="#060"></a>
# 0.6.0 - Christmas 2020

## New features
* Operations can be categorized now. That allows generating handy user interfaces (74c82f0, d03fc2d). For example, you can retrieve a dictionary with all `background removal` operations indiced with their names by calling:
```
import pyclesperanto_prototype as cle
dict = cle.operations(must_have_categories=['background removal'])
```
* Internal support for clImages. This allows acceleated interpolation, which is necessary, e.g. for the new `resample` operation. (075250c)
* Implemented image-size independent kernel compilation. This should improve performance of operations significantly, where typically images of various sizes are processed.
For example operations working with distance matrices and point lists. (d897863)
* `cle.functions` now have a parameter fullargspec to enable better automatic GUI generation for them (119cee3)
* We're working with a version controlled `release_notes` file now. Let's see how this evolves.

### New operations
* `artificial_tissue_2d` (08b154a)
* `add_images` (30fd15b)
* `average_distance_of_n_closest_neighbors` (e90773b)
* `average_distance_of_n_closest_neighbors_map` (4032fa7)
* `average_distance_of_n_far_off_distances` (f72e5ba)
* `average_distance_of_n_shortest_distances` (392f010)
* `average_neighbor_distance_map` (c8e939a)
* `combine_horizontally` (a527be7)
* `combine_vertically` (f8e4d70)
* `concatenate stacks` (b1b6fb0)
* `count_touching_neighbors and create_vector_from_square_matrix` (63d7865)
* `create_from_pointlist` (07cbcd2)
* `downsample_slice_by_slice_half_median` (61d6526)
* `draw_angle_mesh_between_touching_labels` (d1c5330)
* `draw_distance_mesh_between_touch_labels` (b09d717)
* `draw_mesh_between_n_closest_neighbors` (bab895f)
* `degrees_to_radians` (e73b5cb)
* `distance_matrix_to_mesh` (2f1d60e)
* `divide_by_gaussian_background` (e8f461c)
* `exclude_labels` (08e2556)
* `exclude_labels_out_of_size_range` (1fdb2f5)
* `exclude_labels_with_values_out_of_range` (62ade23)
* `exclude_labels_with_values_within_range` (2e35a4b)
* `extend_labels_with_maximum_radius` (55cf151)
* `gamma_correction` (a4f64da)
* `generate_angle_matrix` (e73b5cb)
* `generate_binary_overlap_matrix` (552369a)
* `imread` (711ebc9)
* `imshow` (711ebc9)
* `label_centroids_to_pointlist` (50ee757, 9731e3f)
* `label_maximum_intensity_map` (4bed040)
* `label_mean_intensity_map` (1de25e4)
* `label_pixel_count_map` (a8c3da1)
* `label_spots` (e7b31ef)
* `local_minimum_touching_neighbor_count_map` (9b735c1)
* `local_maximum_touching_neighbor_count_map` (9b735c1)
* `local_mean_touching_neighbor_count_map` (9b735c1)
* `local_median/_touching_neighbor_count_map` (9b735c1)
* `local_standard_deviation_touching_neighbor_count_map` (9b735c1)
* `maximum_of_touching_neighbors` (6339684)
* `mean_of_touching_neighbors` (4eae7bb)
* `median_of_touching_neighbors` (59c255a)
* `minimum_of_touching_neighbors` (86abebf)
* `mode_of_touching_neighbors` (c782f20)
* `n_closest_points` (b7fb4d7)
* `neighbors_of_neighbors` (f4ca339)
* `pointindexlist_to_mesh` (bab895f)
* `pointlist_to_labelled_spots` (7df49ee)
* `push_regionprops` (7d9b57d)
* `radians_to_degrees` (e73b5cb)
* `resample without interpolation` (4076ddd)
* `reduce_stack` (d5f32bd)
* `spots_to_pointlist` (fab24e2)
* `standard_deviation_of_touching_neighbors` (734c1b9)
* `statistics_of_labelled_pixels` (7d9b57d)
* `statistics_of_background_and_labelled_pixels` (7d9b57d)
* `subtract_gaussian_background` (cedb8e3)
* `touching_neighbor_count_map` (d92d7c4, 49fa5c9)
* `write_values_to_positions` (829bd72)

## Backwards compatibility breaking changes
* the behaviour of `exclude_labels` is inverted now 
* The implementation of `label_spots` changed. It's now comparable with CLIJ2.
* `set_nonzero_pixels_to_pixelindex` was renamed to `set_non_zero_pixels_to_pixel_index`

## Deprecations
* As an answer to [Issue #49](https://github.com/clEsperanto/pyclesperanto_prototype/issues/49), 
the `push` and `pull` commands warn now about deprecation. In a future release, we may remove the transposition so that
`push` does the same as `push_zyx`, and `pull` does the same as `pull_zyx`.

## Bugfixes
* automatic `create*` functions failed when only `kwargs` were passed to any operation (d033fed, 4fd6099)
* `divide_by_gaussian_background` didn't divide, it was in fact the implementation of `subtract_gaussian_background` (a6b0dd0)
* before drawing a mesh, all pixels are set to 0 (9433a2f, 52572a6)
* the behaviour of `exclude_labels` was inverse (3c9f5b1, fd5d98b)
* in `exclude_labels` background was added to label 1 in case it was kept (439dba5)
* `detect_maxima_box` had missing parameters compared to the CLIJ2 API
