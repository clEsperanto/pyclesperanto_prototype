
def list_bia_bob_plugins():
    """List of function hints for bia_bob"""
    return """    * Computes the absolute value of every individual pixel in a given image.
    cle.absolute(source: ndarray, destination: ndarray = None) -> ndarray
    
    * Determines the absolute difference pixel by pixel between two images.
    cle.absolute_difference(source1: ndarray, source2: ndarray, destination: ndarray = None) -> ndarray
    
    * Replace label map with the average distance to the n closest neighboring labels, given a label map, distance map, and n.
    cle.average_distance_of_n_nearest_neighbors_map(labels: ndarray, distance_map: ndarray = None, n: int = 1) -> ndarray
    
    * Replaces every label in the label map with the average distance to the n closest neighboring labels
    cle.average_distance_of_n_nearest_neighbors_map(labels: ndarray, distance_map: ndarray = None, n: int = 1) -> ndarray
    
    * Replaces labels in a label map with the average distance to neighboring labels.
    cle.average_neighbor_distance_map(labels: ndarray, distance_map: ndarray = None) -> ndarray
    
    * Compute a binary image from two input images by connecting pairs of pixels with the binary AND operator &.
    cle.binary_and(operand1: ndarray, operand2: ndarray, destination: ndarray = None) -> ndarray
    
    * Identify and set the surface pixels of binary objects to 1 in the destination image, while setting all other pixels to 0.
    cle.binary_edge_detection(source: ndarray, destination: ndarray = None) -> ndarray
    
    * Compute a binary image by connecting corresponding pixels from two input images using the binary AND operator.
    cle.binary_and(operand1: ndarray, operand2: ndarray, destination: ndarray = None) -> ndarray
    
    * Compute a binary image by negating the pixel values of an input image, interpreting all non-zero values as 1.
    cle.binary_not(source: ndarray, destination: ndarray = None) -> ndarray
    
    * Compute a binary image from two input images by connecting pairs of pixels with the binary OR operator.
    cle.binary_or(operand1: ndarray, operand2: ndarray, destination: ndarray = None) -> ndarray
    
    * Subtract one binary image from another.
    cle.binary_subtract(minuend: ndarray, subtrahend: ndarray, destination: ndarray = None) -> ndarray
    
    * Computes a binary image from two input images by connecting pairs of pixels with the binary OR operator.
    cle.binary_or(operand1: ndarray, operand2: ndarray, destination: ndarray = None) -> ndarray
    
    * Connects pairs of pixels from two input images X and Y using binary operators (AND, OR, NOT, XOR) to compute a binary image
    cle.binary_xor(operand1: ndarray, operand2: ndarray, destination: ndarray = None) -> ndarray
    
    * Applies a bottom-hat filter for background subtraction to the input image.
    cle.bottom_hat_sphere(source: ndarray, destination: ndarray = None, radius_x: float = 1, radius_y: float = 1, radius_z: float = 1) -> ndarray
    
    * Determines the centroids of all labels in a label image or image stack and writes the resulting coordinates in a pointlist image
    cle.centroids_of_labels(labels: ndarray, pointlist_destination: ndarray = None, include_background: bool = False) -> ndarray
    
    * This function analyzes a label map and relabels subsequent labels if there are gaps in the indexing.
    cle.relabel_sequential(source: ndarray, output: ndarray = None, blocksize: int = 4096) -> ndarray
    
    * Apply a morphological closing operation to a label image.
    cle.closing_labels(labels_input: ndarray, labels_destination: ndarray = None, radius: int = 0) -> ndarray
    
    * Applies morphological closing to intensity or binary images using a sphere-shaped footprint.
    cle.closing_sphere(input_image: ndarray, destination: ndarray = None, radius_x: int = 1, radius_y: int = 1, radius_z: int = 0) -> ndarray
    
    * combine two images or stacks in X where the output is a destination image.
    cle.combine_horizontally(stack1: ndarray, stack2: ndarray, destination: ndarray = None) -> ndarray
    
    * Combine two label images by adding labels of one image to another
    - Overwrite labels in the first image with labels from the second image
    - Relabel the combined image sequentially
    cle.combine_labels(labels_input1: ndarray, labels_input2: ndarray, labels_destination: ndarray = None) -> ndarray
    
    * Combine two images or stacks in the Y direction.
    cle.combine_vertically(stack1: ndarray, stack2: ndarray, destination: ndarray = None) -> ndarray
    
    * concatenate two stacks in Z
    cle.concatenate_stacks(stack1: ndarray, stack2: ndarray, destination: ndarray = None) -> ndarray
    
    * Performs connected components analysis on a binary image, generating a label map.
    cle.connected_components_labeling_box(binary_input: ndarray, labeling_destination: ndarray = None, flagged_nonzero_minimum_filter: <built-in function callable> = <function nonzero_minimum_box at 0x0000018A95BE9EA0>) -> ndarray
    
    * Computes the number of touching neighbors per label in a touch matrix
    cle.count_touching_neighbors(touch_matrix: ndarray, touching_neighbors_count_destination: ndarray = None, ignore_background: bool = True) -> ndarray
    
    * Create an image where the pixels on label edges are set to 1 and all other pixels are set to 0, given a labelmap image
    cle.detect_label_edges(label_source: ndarray, binary_destination: ndarray = None) -> ndarray
    
    * Apply Gaussian blur to an input image twice with different sigma values and subtract the resulting images from each other
    cle.difference_of_gaussian(source: ndarray, destination: ndarray = None, sigma1_x: float = 2, sigma1_y: float = 2, sigma1_z: float = 2, sigma2_x: float = 2, sigma2_y: float = 2, sigma2_z: float = 2) -> ndarray
    
    * Dilates labels to a larger size without overwriting another label, assuming input images are isotropic.
    cle.dilate_labels(labeling_source: ndarray, labeling_destination: ndarray = None, radius: int = 2) -> ndarray
    
    * Computes the binary dilation of a given input image using the von-Neumann-neighborhood.
    cle.dilate_sphere(source: ndarray, destination: ndarray = None) -> ndarray
    
    * Applies Gaussian blur to an image and divides the original by the result
    cle.divide_by_gaussian_background(source: ndarray, destination: ndarray = None, sigma_x: float = 2, sigma_y: float = 2, sigma_z: float = 2) -> ndarray
    
    * Draws a box on an image at a specified position and size, leaving all other pixels untouched
    cle.draw_box(destination: ndarray, x: int = 0, y: int = 0, z: int = 0, width: int = 1, height: int = 1, depth: int = 1, value: float = 1) -> ndarray
    
    * Draw a line between two points with a given thickness
    cle.draw_line(destination: ndarray, x1: float = 0, y1: float = 0, z1: float = 0, x2: float = 1, y2: float = 1, z2: float = 1, thickness: float = 1, value: float = 1) -> ndarray
    
    * Draws a sphere around a given point with given radii in x, y, and z, if 3D, leaving all other pixels untouched.
    cle.draw_sphere(destination: ndarray, x: float = 0, y: float = 0, z: float = 0, radius_x: float = 1, radius_y: float = 1, radius_z: float = 1, value: float = 1) -> ndarray
    
    * Erodes labels to a smaller size
    cle.erode_connected_labels(labels_input: ndarray, labels_destination: ndarray = None, radius: int = 1) -> ndarray
    
    * Compute a binary image representing the binary erosion of an input image
    cle.erode_sphere(source: ndarray, destination: ndarray = None) -> ndarray
    
    * Segments and labels an image using blurring, Otsu-thresholding, binary erosion, and masked Voronoi-labeling
    cle.eroded_otsu_labeling(image: ndarray, labels_destination: ndarray = None, number_of_erosions: int = 5, outline_sigma: float = 2) -> ndarray
    
    * Remove labels from a label map that touch the edges of the image, and renumber the remaining labels.
    cle.exclude_labels_on_edges(label_map_input: ndarray, label_map_destination: ndarray = None, exclude_in_x: bool = True, exclude_in_y: bool = True, exclude_in_z: bool = True, exlude_in_x: bool = None, exlude_in_y: bool = None, exlude_in_z: bool = None) -> ndarray
    
    * Removes labels from a label map based on their size, specified by a minimum and maximum number of pixels or voxels per label.
    cle.exclude_labels_outside_size_range(source: ndarray, destination: ndarray = None, minimum_size: float = 0, maximum_size: float = 100) -> ndarray
    
    * Removes labels from a label map based on their size in terms of pixel or voxel count.
    cle.exclude_labels_outside_size_range(source: ndarray, destination: ndarray = None, minimum_size: float = 0, maximum_size: float = 100) -> ndarray
    
    * Remove labels from a labelmap and renumber the remaining labels
    cle.exclude_labels_with_values_out_of_range(values_vector: ndarray, label_map_input: ndarray, label_map_destination: ndarray = None, minimum_value_range: float = 0, maximum_value_range: float = 100) -> ndarray
    
    * Remove labels from a labelmap and renumber the remaining labels
    cle.exclude_labels_with_values_within_range(values_vector: ndarray, label_map_input: ndarray, label_map_destination: ndarray = None, minimum_value_range: float = 0, maximum_value_range: float = 100) -> ndarray
    
    * Removes labels from a label map based on their size
    cle.exclude_large_labels(source: ndarray, destination: ndarray = None, minimum_size: float = 100) -> ndarray
    
    * Removes labels from a label map below a specified maximum size
    cle.exclude_small_labels(source: ndarray, destination: ndarray = None, maximum_size: float = 100) -> ndarray
    
    * Takes a label map image and dilates the regions until they touch, and then writes the resulting label map to the output.
    cle.extend_labeling_via_voronoi(labeling_source: ndarray, labeling_destination: ndarray = None) -> ndarray
    
    * Dilates labels to a larger size without label overwrite, assuming input images are isotropic.
    cle.dilate_labels(labeling_source: ndarray, labeling_destination: ndarray = None, radius: int = 2) -> ndarray
    
    * Maximizes the local pixel intensity variance by projecting an extended depth of focus
    cle.extended_depth_of_focus_variance_projection(source: ndarray, destination: ndarray = None, radius_x: int = 10, radius_y: int = 10, sigma: float = 5) -> ndarray
    
    * compute the absolute value of every individual pixel in a given image
    cle.absolute(source: ndarray, destination: ndarray = None) -> ndarray
    
    * Segment objects in grey-value images by applying a Gaussian blur, Otsu-thresholding, and connected component labeling.
    cle.gauss_otsu_labeling(source: ndarray, label_image_destination: ndarray = None, outline_sigma: float = 2) -> ndarray
    
    * Compute the Gaussian blurred image of an image given sigma values in X, Y, and Z.
    cle.gaussian_blur(source: ndarray, destination: ndarray = None, sigma_x: float = 0, sigma_y: float = 0, sigma_z: float = 0) -> ndarray
    
    * Compute the distance between all point coordinates given in two point lists.
    cle.generate_distance_matrix(coordinate_list1: ndarray, coordinate_list2: ndarray, distance_matrix_destination: ndarray = None) -> ndarray
    
    * Generate a touch matrix that represents a region adjacency graph for a labelmap
    cle.generate_touch_matrix(label_map: ndarray, touch_matrix_destination: ndarray = None) -> ndarray
    
    * Performs connected components analysis on a binary image, generating a label map
    cle.connected_components_labeling_box(binary_input: ndarray, labeling_destination: ndarray = None, flagged_nonzero_minimum_filter: <built-in function callable> = <function nonzero_minimum_box at 0x0000018A95BE9EA0>) -> ndarray
    
    * Determines the centroids of all labels in a label image or image stack and writes the resulting coordinates in a pointlist image.
    cle.centroids_of_labels(labels: ndarray, pointlist_destination: ndarray = None, include_background: bool = False) -> ndarray
    
    * Transforms a binary image with single pixels set to 1 to a labeled spots image, or transforms a spots image into an image with numbered spots.
    cle.label_spots(input_spots: ndarray, labelled_spots_destination: ndarray = None) -> ndarray
    
    * Generates a coordinate list of points in a labelled spot image.
    cle.labelled_spots_to_pointlist(input_labelled_spots: ndarray, destination_pointlist: ndarray = None) -> ndarray
    
    * Apply the Laplace operator (Box neighborhood) to an image.
    cle.laplace_box(source: ndarray, destination: ndarray = None) -> ndarray
    
    * Applies the Laplace operator (Diamond neighborhood) to an image.
    cle.laplace_diamond(source: ndarray, destination: ndarray = None) -> ndarray
    
    * Compute a binary image by connecting pairs of pixels from two input images using the binary AND operator.
    cle.binary_and(operand1: ndarray, operand2: ndarray, destination: ndarray = None) -> ndarray
    
    * Compute a binary image by inverting the pixel values of an input image, interpreting all non-zero values as 1.
    cle.binary_not(source: ndarray, destination: ndarray = None) -> ndarray
    
    * Compute a binary image by connecting pairs of pixels from two input images using the binary OR operator |.
    cle.binary_or(operand1: ndarray, operand2: ndarray, destination: ndarray = None) -> ndarray
    
    * Create a binary image by connecting pairs of pixels from two input images using binary operators AND, OR, NOT, and XOR.
    cle.binary_xor(operand1: ndarray, operand2: ndarray, destination: ndarray = None) -> ndarray
    
    * Replaces integer intensities specified in a vector image by mapping them to new values.
    cle.replace_intensities(source: ndarray, new_values_vector: ndarray, destination: ndarray = None) -> ndarray
    
    * Computes a masked image by applying a binary mask to an image.
    cle.mask(source: ndarray, mask: ndarray, destination: ndarray = None) -> ndarray
    
    * Copy pixel values from one image to another based on a label mask.
    cle.mask_label(source: ndarray, label_map: ndarray, destination: ndarray = None, label_index: int = 1) -> ndarray
    
    * Performs label map generation and dilation on a binary image using an octagon shape, within a specified masked area, resulting in a labeled output image.
    cle.masked_voronoi_labeling(binary_source: ndarray, mask_image: ndarray, labeling_destination: ndarray = None) -> ndarray
    
    * Compute the maximum pixel value between two images and store the result in a destination image
    cle.maximum_images(source1: ndarray, source2: ndarray, destination: ndarray = None) -> ndarray
    
    * Compute the maximum of a constant scalar and each pixel value in an image.
    cle.maximum_image_and_scalar(source: ndarray, destination: ndarray = None, scalar: float = 0) -> ndarray
    
    * Compute the maximum pixel value between two given images and store the result in a destination image.
    cle.maximum_images(source1: ndarray, source2: ndarray, destination: ndarray = None) -> ndarray
    
    * Computes the local maximum of a pixel's spherical neighborhood.
    cle.maximum_sphere(source: ndarray, destination: ndarray = None, radius_x: float = 1, radius_y: float = 1, radius_z: float = 0) -> ndarray
    
    * Determines the maximum intensity projection of an image along the Z-axis.
    cle.maximum_z_projection(source: ndarray, destination_max: ndarray = None) -> ndarray
    
    * Computes the local mean average of a pixel's spherical neighborhood
    cle.mean_sphere(source: ndarray, destination: ndarray = None, radius_x: float = 1, radius_y: float = 1, radius_z: float = 1) -> ndarray
    
    * Determines the mean squared error between two images and stores the result in a new row of ImageJs Results table
    cle.mean_squared_error(source1: ndarray, source2: ndarray) -> float
    
    * Determines the mean average intensity projection of an image along the Z-axis.
    cle.mean_z_projection(source: ndarray, destination: ndarray = None) -> ndarray
    
    * Compute the mean intensity along borders between labels in an image, then merge labels within a specified intensity range.
    cle.merge_labels_with_border_intensity_within_range(image: ndarray, labels: ndarray, labels_destination: ndarray = None, minimum_intensity: float = 0, maximum_intensity: float = 3.4028235e+38)
    
    * Merge and renumber labels in a label image, producing a new label image.
    cle.merge_touching_labels(labels_input: ndarray, labels_destination: ndarray = None) -> ndarray
    
    * Computes the local minimum of a pixels spherical neighborhood specified by its half-width, half-height, and half-depth.
    cle.minimum_sphere(source: ndarray, destination: ndarray = None, radius_x: float = 1, radius_y: float = 1, radius_z: float = 1) -> ndarray
    
    * Determine the minimum intensity projection of an image along the Z-axis.
    cle.minimum_z_projection(source: ndarray, destination_min: ndarray = None) -> ndarray
    
    * Computes the remainder of a division of pairwise pixel values in two images.
    cle.modulo_images(image1: ndarray, image2: ndarray, destination: ndarray = None) -> ndarray
    
    * Compute the local mode of a pixels sphere shaped neighborhood
    cle.mode_sphere(source: ndarray, destination: ndarray = None, radius_x: int = 1, radius_y: int = 1, radius_z: int = 1) -> ndarray
    
    * Compute the remainder of a division of pairwise pixel values in two images
    cle.modulo_images(image1: ndarray, image2: ndarray, destination: ndarray = None) -> ndarray
    
    * Apply a morphological opening operation to a label image with an octagon as the structuring element, using iterative erosion and dilation.
    cle.opening_labels(labels_input: ndarray, labels_destination: ndarray = None, radius: int = 0) -> ndarray
    
    * Apply morphological opening to intensity or binary images using a sphere-shaped footprint.
    cle.opening_sphere(input_image: ndarray, destination: ndarray = None, radius_x: int = 1, radius_y: int = 1, radius_z: int = 0) -> ndarray
    
    * Takes a pointlist with coordinates and labels corresponding pixels
    cle.pointlist_to_labelled_spots(pointlist: ndarray, spots_destination: ndarray = None) -> ndarray
    
    * Takes a label map and replaces each label with the number of neighboring labels within a given distance range
    cle.proximal_neighbor_count_map(source: ndarray, destination: ndarray = None, min_distance: float = 0, max_distance: float = 3.4028235e+38) -> ndarray
    
    * Read parametric values from label positions in a label image and a parametric image and store the intensity values in a vector
    cle.read_intensities_from_map(labels: ndarray, map_image: ndarray, values_destination: ndarray = None) -> ndarray
    
    * Go to positions in an image specified by a pointlist, read intensities of those pixels, and store them in a new vector.
    cle.read_intensities_from_positions(pointlist: ndarray, intensity_image: ndarray, values_destination: ndarray = None) -> ndarray
    
    * Reduces label map by taking only the center spots and setting background to zero.
    cle.reduce_labels_to_centroids(source: ndarray, destination: ndarray = None) -> ndarray
    
    * Reduces labels to their edges in a label map
    cle.reduce_labels_to_label_edges(source: ndarray, destination: ndarray = None) -> ndarray
    
    * Reduce the number of slices in a stack by a factor and control which slices stay by specifying an offset.
    cle.reduce_stack(source: ndarray, destination: ndarray = None, reduction_factor: int = 2, offset: int = 0) -> ndarray
    
    * This function analyzes a label map and relabels subsequent labels if there are any gaps in the indexing, resulting in the number of labels and the maximum label index being equal.
    cle.relabel_sequential(source: ndarray, output: ndarray = None, blocksize: int = 4096) -> ndarray
    
    * Computes the remainder of a division of pairwise pixel values in two images
    cle.modulo_images(image1: ndarray, image2: ndarray, destination: ndarray = None) -> ndarray
    
    * Replaces integer intensities specified in a vector image.
    cle.replace_intensities(source: ndarray, new_values_vector: ndarray, destination: ndarray = None) -> ndarray
    
    * Transform an image by translating and rotating it, with optional parameters for interpolation, auto-sizing, and specifying the center of rotation.
    cle.rigid_transform(source: ndarray, destination: ndarray = None, translate_x: float = 0, translate_y: float = 0, translate_z: float = 0, angle_around_x_in_degrees: float = 0, angle_around_y_in_degrees: float = 0, angle_around_z_in_degrees: float = 0, rotate_around_center: bool = True, linear_interpolation: bool = False, auto_size: bool = False) -> ndarray
    
    * Apply morphological opening operation and voronoi-labeling to a label image, then mask the result label image
    cle.smooth_labels(labels_input: ndarray, labels_destination: ndarray = None, radius: int = 0) -> ndarray
    
    * Convolve an image with the Sobel kernel.
    cle.sobel(source: ndarray, destination: ndarray = None) -> ndarray
    
    * Compute the squared difference pixel by pixel between two images
    cle.squared_difference(source1: ndarray, source2: ndarray, destination: ndarray = None) -> ndarray
    
    * Computes the local standard deviation of a pixel's neighborhood given a specified box size. The box size is specified by its half-width, half-height, and half-depth (radius).
    cle.standard_deviation_sphere(source: ndarray, destination: ndarray = None, radius_x: int = 1, radius_y: int = 1, radius_z: int = 1) -> ndarray
    
    * Determines the standard deviation intensity projection of an image stack along Z.
    cle.standard_deviation_z_projection(source: ndarray, destination: ndarray = None) -> ndarray
    
    * Determines various properties of labelled objects in an image, including bounding box, area, intensity statistics, and shape descriptors.
    cle.statistics_of_labelled_pixels(intensity_image: ndarray = None, label_image: ndarray = None)
    
    * Crop multiple Z-slices of a 3D stack into a new 3D stack.
    cle.sub_stack(source: ndarray, destination: ndarray = None, start_z: int = 0, end_z: int = 0) -> ndarray
    
    * Apply Gaussian blur to an input image and subtract the result from the original image
    cle.subtract_gaussian_background(source: ndarray, destination: ndarray = None, sigma_x: float = 2, sigma_y: float = 2, sigma_z: float = 2) -> ndarray
    
    * Combine two label images by removing labels from one image that also exist in the other image
    cle.subtract_labels(labels_input1: ndarray, labels_input2: ndarray, labels_destination: ndarray = None) -> ndarray
    
    * Determines the sum intensity projection of an image along Z.
    cle.sum_z_projection(source: ndarray, destination: ndarray = None) -> ndarray
    
    * Binarizes an image using Otsu's threshold method and creates binary images.
    cle.threshold_otsu(source: ndarray, destination: ndarray = None) -> ndarray
    
    * Applies a top-hat filter for background subtraction to the input image
    cle.top_hat_sphere(source: ndarray, destination: ndarray = None, radius_x: float = 1, radius_y: float = 1, radius_z: float = 1) -> ndarray
    
    * Takes a label map and replaces each label with the number of neighboring labels it touches.
    cle.touching_neighbor_count_map(source: ndarray, destination: ndarray = None) -> ndarray
    
    * Computes the local variance of a pixel's sphere neighborhood, specified by its half-width, half-height, and half-depth (radius), ignoring radius_z if 2D images are given.
    cle.variance_sphere(source: ndarray, destination: ndarray = None, radius_x: int = 1, radius_y: int = 1, radius_z: int = 1) -> ndarray
    
    * Label connected components in a binary image and dilate the regions until they touch
    cle.voronoi_labeling(binary_source: ndarray, labeling_destination: ndarray = None) -> ndarray
    
    * Labels objects in grey-value images by applying two Gaussian blurs, spot detection, Otsu-thresholding, and Voronoi-labeling
    cle.voronoi_otsu_labeling(source: ndarray, label_image_destination: ndarray = None, spot_sigma: float = 2, outline_sigma: float = 2) -> ndarray
    
    """
