
__kernel void generate_touch_matrix_3d(
    IMAGE_dst_matrix_TYPE dst_matrix,
    IMAGE_src_label_map_TYPE src_label_map
) {
  const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

  const int x = get_global_id(0);
  const int y = get_global_id(1);
  const int z = get_global_id(2);

  float label = READ_src_label_map_IMAGE(src_label_map, sampler, POS_src_label_map_INSTANCE(x, y, z, 0)).x;


  if (x <= GET_IMAGE_WIDTH(src_label_map) - 1) {
    float labelx = READ_src_label_map_IMAGE(src_label_map, sampler, POS_src_label_map_INSTANCE(x + 1, y, z, 0)).x;
    if (label < labelx) {
      WRITE_dst_matrix_IMAGE(dst_matrix, (POS_dst_matrix_INSTANCE(label, labelx, 0, 0)), CONVERT_dst_matrix_PIXEL_TYPE(1));
    } else if (label > labelx) {
      WRITE_dst_matrix_IMAGE(dst_matrix, (POS_dst_matrix_INSTANCE(labelx, label, 0, 0)), CONVERT_dst_matrix_PIXEL_TYPE(1));
    }
  }
  if (y <= GET_IMAGE_HEIGHT(src_label_map) - 1) {
    float labely = READ_src_label_map_IMAGE(src_label_map, sampler, POS_src_label_map_INSTANCE(x, y + 1, z, 0)).x;
    if (label < labely) {
      WRITE_dst_matrix_IMAGE(dst_matrix, (POS_dst_matrix_INSTANCE(label, labely, 0, 0)), CONVERT_dst_matrix_PIXEL_TYPE(1));
    } else if (label > labely) {
      WRITE_dst_matrix_IMAGE(dst_matrix, (POS_dst_matrix_INSTANCE(labely, label, 0, 0)), CONVERT_dst_matrix_PIXEL_TYPE(1));
    }
  }
  if (z <= GET_IMAGE_DEPTH(src_label_map) - 1) {
    float labelz = READ_src_label_map_IMAGE(src_label_map, sampler, POS_src_label_map_INSTANCE(x, y, z + 1, 0)).x;
    if (label < labelz) {
      WRITE_dst_matrix_IMAGE(dst_matrix, (POS_dst_matrix_INSTANCE(label, labelz, 0, 0)), CONVERT_dst_matrix_PIXEL_TYPE(1));
    } else if (label > labelz) {
      WRITE_dst_matrix_IMAGE(dst_matrix, (POS_dst_matrix_INSTANCE(labelz, label, 0, 0)), CONVERT_dst_matrix_PIXEL_TYPE(1));
    }
  }
}
