
__kernel void count_touching_neighbors (
IMAGE_src_touch_matrix_TYPE src_touch_matrix,
IMAGE_dst_count_list_TYPE dst_count_list
) {
  const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

  const int label_id = get_global_id(0);
  const int label_count = get_global_size(0);

  int count = 0;

  int y = label_id;
  int x = 0;
  for (x = 0; x < label_id; x++) {
    float value = READ_src_touch_matrix_IMAGE(src_touch_matrix, sampler, POS_src_touch_matrix_INSTANCE(x, y, 0, 0)).x;
    if (value > 0) {
      count++;
    }
  }
  x = label_id;
  for (y = label_id + 1; y < label_count; y++) {
    float value = READ_src_touch_matrix_IMAGE(src_touch_matrix, sampler, POS_src_touch_matrix_INSTANCE(x, y, 0, 0)).x;
    if (value > 0) {
      count++;
    }
  }

  WRITE_dst_count_list_IMAGE(dst_count_list, (POS_dst_count_list_INSTANCE(label_id, 0, 0, 0)), CONVERT_dst_count_list_PIXEL_TYPE(count));
}

