__kernel void generate_touch_intensity_matrix (
    IMAGE_dst_neighbor_touching_count_matrix_TYPE dst_neighbor_touching_count_matrix,
    IMAGE_dst_neighbor_touching_sum_intensity_matrix_TYPE dst_neighbor_touching_sum_intensity_matrix,
    IMAGE_src_label_TYPE src_label,
    IMAGE_src_intensity_TYPE src_intensity
) {
  const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

  const int x = get_global_id(0);
  const int y = get_global_id(1);
  const int z = get_global_id(2);

  int width = GET_IMAGE_WIDTH(src_label);
  int height = GET_IMAGE_HEIGHT(src_label);
  int depth = GET_IMAGE_DEPTH(src_label);

  int matrix_width = GET_IMAGE_WIDTH(dst_neighbor_touching_count_matrix);

  int label_c = READ_IMAGE(src_label,sampler,POS_src_label_INSTANCE(x,y,z,0)).x;
  float intensity_c = READ_IMAGE(src_intensity,sampler,POS_src_intensity_INSTANCE(x,y,z,0)).x;

  if (x > 0) {
    int other_label = READ_IMAGE(src_label,sampler,POS_src_label_INSTANCE(x-1,y,z,0)).x;
    if (label_c != other_label) {
      float other_intensity = READ_IMAGE(src_intensity,sampler,POS_src_intensity_INSTANCE(x-1,y,z,0)).x;
      int pos_in_buffer = label_c + other_label * matrix_width;
      atomic_add(&dst_neighbor_touching_count_matrix[pos_in_buffer], 1);
      atomic_add(&dst_neighbor_touching_sum_intensity_matrix[pos_in_buffer], (intensity_c + other_intensity)/2);
    } 
  }
  if (y > 0) {
    int other_label = READ_IMAGE(src_label,sampler,POS_src_label_INSTANCE(x,y-1,z,0)).x;
    if (label_c != other_label) {
      float other_intensity = READ_IMAGE(src_intensity,sampler,POS_src_intensity_INSTANCE(x,y-1,z,0)).x;
      int pos_in_buffer = label_c + other_label * matrix_width;
      atomic_add(&dst_neighbor_touching_count_matrix[pos_in_buffer], 1);
      atomic_add(&dst_neighbor_touching_sum_intensity_matrix[pos_in_buffer], (intensity_c + other_intensity)/2);
    }
  }
  if (z > 0) {
    int other_label = READ_IMAGE(src_label,sampler,POS_src_label_INSTANCE(x,y,z-1,0)).x;
    if (label_c != other_label) {
      float other_intensity = READ_IMAGE(src_intensity,sampler,POS_src_intensity_INSTANCE(x,y,z-1,0)).x;
      int pos_in_buffer = label_c + other_label * matrix_width;
      atomic_add(&dst_neighbor_touching_count_matrix[pos_in_buffer], 1);
      atomic_add(&dst_neighbor_touching_sum_intensity_matrix[pos_in_buffer], (intensity_c + other_intensity)/2);
    }
  }
}