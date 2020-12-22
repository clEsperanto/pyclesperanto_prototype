
__kernel void generate_binary_overlap_matrix_2d(
    IMAGE_dst_matrix_TYPE dst_matrix,
    IMAGE_src_label_map1_TYPE src_label_map1,
    IMAGE_src_label_map2_TYPE src_label_map2
) {
  const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

  const int x = get_global_id(0);
  const int y = get_global_id(1);

  float label1 = READ_IMAGE(src_label_map1, sampler, POS_src_label_map1_INSTANCE(x, y, 0, 0)).x;
  float label2 = READ_IMAGE(src_label_map2, sampler, POS_src_label_map2_INSTANCE(x, y, 0, 0)).x;

  WRITE_dst_matrix_IMAGE(dst_matrix, (POS_dst_matrix_INSTANCE(label1, label2, 0, 0)), CONVERT_dst_matrix_PIXEL_TYPE(1));
}
