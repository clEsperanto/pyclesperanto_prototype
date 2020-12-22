
__kernel void generate_angle_matrix(
    IMAGE_dst_matrix_TYPE dst_matrix,
    IMAGE_src_point_list1_TYPE src_point_list1,
    IMAGE_src_point_list2_TYPE src_point_list2
) {
  const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

  const int p = get_global_id(0);

  int n_dimensions = GET_IMAGE_HEIGHT(src_point_list1);
  int n_points = GET_IMAGE_WIDTH(src_point_list2);


  const float pos_x = READ_src_point_list1_IMAGE(src_point_list1, sampler, POS_src_point_list1_INSTANCE(p, 0, 0, 0)).x;
  const float pos_y = READ_src_point_list1_IMAGE(src_point_list1, sampler, POS_src_point_list1_INSTANCE(p, 1, 0, 0)).x;

  for (int j = 0; j < GET_IMAGE_WIDTH(src_point_list2); j ++) {
      const float pos_d_x = READ_src_point_list2_IMAGE(src_point_list2, sampler, POS_src_point_list2_INSTANCE(j, 0, 0, 0)).x;
      const float pos_d_y = READ_src_point_list2_IMAGE(src_point_list2, sampler, POS_src_point_list2_INSTANCE(j, 1, 0, 0)).x;

      const double adjacent = pos_d_x - pos_x;
      const double opposite = pos_d_y - pos_y;

      const float out = atan(opposite / adjacent);

      WRITE_dst_matrix_IMAGE(dst_matrix, POS_dst_matrix_INSTANCE(p+1, j+1, 0, 0), CONVERT_dst_matrix_PIXEL_TYPE(out));
  }
}
