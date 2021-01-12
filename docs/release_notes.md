# upcoming release

## New features
* `centroids_of_labels` was GPU-accelerated.
* `statistics_of_labelled_pixels` and `statistics_of_background_and_labelled_pixels` contain the parameter `standard_deviation_intensity` now.
* `statistics_of_labelled_pixels` and `statistics_of_background_and_labelled_pixels` are now GPU-accelerated. The 
results of the GPU-accelerated statistics are dictionaries which contain the same measurements as in CLIJ2.

### New operations
* `centroids_of_background_and_labels`
* `detect_minima_box`
* `euclidean_distance_from_label_centroid_map`
* `maximum_distance_of_touching_neighbors`
* `merge_touching_labels`
* `minimum_distance_of_touching_neighbors`
* `statistics_of_image`
* `label_standard_deviation_intensity_map`
* `label_mean_extension_map`
* `label_maximum_extension_map`
* `label_maximum_extension_ratio_map`
* `regionprops`
* `read_intensities_from_map`
* `read_intensities_from_positions`
* `mean_of_touching_neighbors_map`
* `standard_deviation_of_touching_neighbors_map`
* `mode_of_touching_neighbors_map`
* `minimum_of_touching_neighbors_map`
* `maximum_of_touching_neighbors_map`
* `maximum_distance_of_n_shortest_distances`
* `point_index_list_to_touch_matrix`
* `generate_n_nearest_neighbors_matrix`
* `generate_proximal_neighbors_matrix` and alias `generate_distal_neighbors_matrix`
* `maximum_of_n_nearest_neighbors_map`
* `maximum_of_proximal_neighbors_map` and alias `maximum_of_distal_neighbors_map`
* `touch_matrix_to_adjacency_matrix`
* `maximum_of_n_nearest_neighbors_map`
* `minimum_of_proximal_neighbors_map` and alias `minimum_of_distal_neighbors_map`
* `mode_of_n_nearest_neighbors_map`
* `mode_of_proximal_neighbors_map` and alias `mode_of_distal_neighbors_map`
* `standard_deviation_of_n_nearest_neighbors_map`
* `standard_deviation_of_proximal_neighbors_map` and alias `standard_deviation_of_distal_neighbors_map`
* `affine_transform` (yet without shearing)
* `translate`
* `rotate`
* `scale`
* `rigid_transform`
* `added mean_of_n_nearest_neighbors`
* `mean_of_proximal_neighbors` and alias `alias mean_of_distal_neighbors`

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
