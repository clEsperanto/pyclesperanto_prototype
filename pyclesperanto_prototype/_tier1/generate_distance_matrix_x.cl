
__kernel void generate_distance_matrix(
    IMAGE_dst_matrix_TYPE dst_matrix,
    IMAGE_src_point_list1_TYPE src_point_list1,
    IMAGE_src_point_list2_TYPE src_point_list2
) {
  const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

  const int x = get_global_id(0);

  int n_dimensions = GET_IMAGE_HEIGHT(src_point_list1);
  int n_points = GET_IMAGE_WIDTH(src_point_list2);

  float positions[10];
  for (int i = 0; i < n_dimensions; i ++) {
      positions[i] = READ_src_point_list1_IMAGE(src_point_list1, sampler, POS_src_point_list1_INSTANCE(x, i, 0, 0)).x;
  }

  for (int j = 0; j < GET_IMAGE_WIDTH(src_point_list2); j ++) {
      float sum = 0;
      for (int i = 0; i < n_dimensions; i ++) {
          sum = sum + pow(positions[i] - (float)READ_src_point_list2_IMAGE(src_point_list2, sampler, POS_src_point_list2_INSTANCE(j, i, 0, 0)).x, (float)2);
      }
      float out = sqrt(sum);
      WRITE_dst_matrix_IMAGE(dst_matrix, POS_dst_matrix_INSTANCE(get_global_id(0)+1, j+1, 0, 0), CONVERT_dst_matrix_PIXEL_TYPE(out));
  }
}
