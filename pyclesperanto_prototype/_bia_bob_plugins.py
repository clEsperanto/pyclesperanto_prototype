
def list_bia_bob_plugins():
    """List of function hints for bia_bob"""

    # do not recommend anything if pyclesperanto (non-prototype) is installed
    try:
        import pyclesperanto
        return ""
    except:
        pass


    return """
    * Set only surface pixels to 1 in destination binary image
    cle.binary_edge_detection(source: ndarray, destination: ndarray = None) -> ndarray
    
    * Create a binary image by inverting pixel values in an input image, where all non-zero pixels become 0 and zeros become 1
    cle.binary_not(source: ndarray, destination: ndarray = None) -> ndarray
    
    * Determines centroids of all labels in an image and writes coordinates in a pointlist image
    cle.centroids_of_labels(labels: ndarray, pointlist_destination: ndarray = None, include_background: bool = False) -> ndarray
    
    * Analyses a label map to ensure that all labels are indexed without gaps before returning the relabeled map.
    cle.relabel_sequential(source: ndarray, output: ndarray = None, blocksize: int = 4096) -> ndarray
    
    * Apply morphological closing with a sphere-shaped footprint to intensity or binary images.
    cle.closing_sphere(input_image: ndarray, destination: ndarray = None, radius_x: int = 1, radius_y: int = 1, radius_z: int = 0) -> ndarray
    
    * Combines two label images by adding labels from one image to another and sequentially relabeling the result
    cle.combine_labels(labels_input1: ndarray, labels_input2: ndarray, labels_destination: ndarray = None) -> ndarray
    
    * Performs connected components analysis inspecting the box neighborhood of every pixel in a binary image, generating a label map
    cle.connected_components_labeling_box(binary_input: ndarray, labeling_destination: ndarray = None, flagged_nonzero_minimum_filter: <built-in function callable> = <function nonzero_minimum_box at 0x000001ECA0BEDC10>) -> ndarray
    
    * Takes a labelmap and sets edge pixels to 1 and others to 0
    cle.detect_label_edges(label_source: ndarray, binary_destination: ndarray = None) -> ndarray
    
    * Apply Gaussian blur to an input image twice with different sigma values, resulting in two images that are subtracted from each other. It is recommended to apply this operation to images of type Float (32 bit).
    cle.difference_of_gaussian(source: ndarray, destination: ndarray = None, sigma1_x: float = 2, sigma1_y: float = 2, sigma1_z: float = 2, sigma2_x: float = 2, sigma2_y: float = 2, sigma2_z: float = 2) -> ndarray
    
    * Dilates label images to a larger size without overwriting other labels, assuming input images are isotropic.
    cle.dilate_labels(labeling_source: ndarray, labeling_destination: ndarray = None, radius: int = 2) -> ndarray
    
    * Removes labels touching edges of the image in X, Y, and Z; renumbers remaining labels; allows exclusion along min and max X, Y, and Z axes
    cle.exclude_labels_on_edges(label_map_input: ndarray, label_map_destination: ndarray = None, exclude_in_x: bool = True, exclude_in_y: bool = True, exclude_in_z: bool = True, exlude_in_x: bool = None, exlude_in_y: bool = None, exlude_in_z: bool = None) -> ndarray
    
    * Removes labels from a label map above a given maximum size 
    cle.exclude_large_labels(source: ndarray, destination: ndarray = None, minimum_size: float = 100) -> ndarray
    
    * Removes labels from a label map below a specified maximum size by number of pixels or voxels.
    cle.exclude_small_labels(source: ndarray, destination: ndarray = None, maximum_size: float = 100) -> ndarray
    
    * Dilates labels in an isotropic label image without overwriting other labels.
    cle.dilate_labels(labeling_source: ndarray, labeling_destination: ndarray = None, radius: int = 2) -> ndarray
    
    * Compute the Gaussian blurred image of an image given sigma values in X, Y, and Z with optional destination and sigma parameters.
    cle.gaussian_blur(source: ndarray, destination: ndarray = None, sigma_x: float = 0, sigma_y: float = 0, sigma_z: float = 0) -> ndarray
    
    * Performs connected components analysis on a binary image by inspecting each pixel's neighbors to generate a label map.
    cle.connected_components_labeling_box(binary_input: ndarray, labeling_destination: ndarray = None, flagged_nonzero_minimum_filter: <built-in function callable> = <function nonzero_minimum_box at 0x000001ECA0BEDC10>) -> ndarray
    
    * Determines centroids of labels in a label image or image stack, writing resulting coordinates in a pointlist image: label image input, destination image of d*n size for d-dimensional label image with n labels, optional background centroid measurement
    cle.centroids_of_labels(labels: ndarray, pointlist_destination: ndarray = None, include_background: bool = False) -> ndarray
    
    * Computes a binary image by inverting pixel values with the binary NOT operator, treating non-zero values as 1.
    cle.binary_not(source: ndarray, destination: ndarray = None) -> ndarray
    
    * Replace integer intensities in a 3D vector image with specified values
    cle.replace_intensities(source: ndarray, new_values_vector: ndarray, destination: ndarray = None) -> ndarray
    
    * Computes the local maximum of a pixel's spherical neighborhood specified by radius in three dimensions.
    cle.maximum_sphere(source: ndarray, destination: ndarray = None, radius_x: float = 1, radius_y: float = 1, radius_z: float = 0) -> ndarray
    
    * Maximum intensity projection of an image along Z
    cle.maximum_z_projection(source: ndarray, destination_max: ndarray = None) -> ndarray
    
    * Compute the local mean average of a pixel's spherical neighborhood using specified radii dimensions in 3D space.
    cle.mean_sphere(source: ndarray, destination: ndarray = None, radius_x: float = 1, radius_y: float = 1, radius_z: float = 1) -> ndarray
    
    * Calculates the mean average intensity projection of an image along Z.
    cle.mean_z_projection(source: ndarray, destination: ndarray = None) -> ndarray
    
    * takes a label image, merges touching labels, renumbers them, and produces a new label image
    cle.merge_touching_labels(labels_input: ndarray, labels_destination: ndarray = None) -> ndarray
    
    * Computes the local minimum of a pixels spherical neighborhood with specified radius dimensions
    cle.minimum_sphere(source: ndarray, destination: ndarray = None, radius_x: float = 1, radius_y: float = 1, radius_z: float = 1) -> ndarray
    
    * Calculates the minimum intensity projection of an image along the Z-axis
    cle.minimum_z_projection(source: ndarray, destination_min: ndarray = None) -> ndarray
    
    * Compute the local mode of a pixels sphere shaped neighborhood to locally correct semantic segmentation results of an image, with specified half-width and half-height (radius) of the sphere, and intensities ranging from 0 to 255, returning the smallest value in case of multiple maximum frequency values.
    cle.mode_sphere(source: ndarray, destination: ndarray = None, radius_x: int = 1, radius_y: int = 1, radius_z: int = 1) -> ndarray
    
    * Reads intensity values from labeled image positions and stores them in a new vector, taking into consideration certain constraints on label structure.
    cle.read_intensities_from_map(labels: ndarray, map_image: ndarray, values_destination: ndarray = None) -> ndarray
    
    * Reduce all labels in a label map to their center spots, keeping label IDs intact and setting background to zero.
    cle.reduce_labels_to_centroids(source: ndarray, destination: ndarray = None) -> ndarray
    
    * reduce all labels in a label map to their edges, maintaining label IDs and setting background to zero
    cle.reduce_labels_to_label_edges(source: ndarray, destination: ndarray = None) -> ndarray
    
    * Analyses and renumbers a label map to fill in any gaps in indexing, ensuring that the number of labels matches the maximum label index
    cle.relabel_sequential(source: ndarray, output: ndarray = None, blocksize: int = 4096) -> ndarray
    
    * Replaces integer intensities specified in a vector image with new values
    cle.replace_intensities(source: ndarray, new_values_vector: ndarray, destination: ndarray = None) -> ndarray
    
    * Apply morphological opening operation, fill label gaps with voronoi-labeling, and mask background pixels in label image.
    cle.smooth_labels(labels_input: ndarray, labels_destination: ndarray = None, radius: int = 0) -> ndarray
    
    * Convolve image with Sobel kernel to detect edges in image
    cle.sobel(source: ndarray, destination: ndarray = None) -> ndarray
    
    * Determines bounding box, area, min, max, mean, standard deviation of intensity and shape descriptors of labelled objects in a label map and corresponding pixels in the original image.
    cle.statistics_of_labelled_pixels(intensity_image: ndarray = None, label_image: ndarray = None)
    
    * Apply Gaussian blur to input image and subtract from original to create destination image.
    cle.subtract_gaussian_background(source: ndarray, destination: ndarray = None, sigma_x: float = 2, sigma_y: float = 2, sigma_z: float = 2) -> ndarray
    
    * Combine two label images by removing overlapping labels from one image that also exist in the other image.
    cle.subtract_labels(labels_input1: ndarray, labels_input2: ndarray, labels_destination: ndarray = None) -> ndarray
    
    * Determine the sum intensity projection of an image along Z
    cle.sum_z_projection(source: ndarray, destination: ndarray = None) -> ndarray
    
    * Binarize an image using Otsu's threshold method implemented in scikit-image, utilizing a GPU-based histogram for binary image creation.
    cle.threshold_otsu(source: ndarray, destination: ndarray = None) -> ndarray
    
    * Apply a top-hat filter for background subtraction to an input image.
    cle.top_hat_sphere(source: ndarray, destination: ndarray = None, radius_x: float = 1, radius_y: float = 1, radius_z: float = 1) -> ndarray
    
    * Takes a binary image, labels connected components, dilates regions until they touch, and outputs a label map.
    cle.voronoi_labeling(binary_source: ndarray, labeling_destination: ndarray = None) -> ndarray
    
    * Labels objects in grey-value images using Gaussian blurs, spot detection, Otsu-thresholding, and Voronoi-labeling from isotropic input images.
    cle.voronoi_otsu_labeling(source: ndarray, label_image_destination: ndarray = None, spot_sigma: float = 2, outline_sigma: float = 2) -> ndarray
    
    """
