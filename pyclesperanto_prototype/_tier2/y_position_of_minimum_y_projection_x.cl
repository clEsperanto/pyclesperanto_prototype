
__kernel void y_position_of_minimum_y_projection (
    IMAGE_dst_arg_TYPE dst_arg,
    IMAGE_src_TYPE src
) {
  const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

  const int x = get_global_id(0);
  const int z = get_global_id(1);
  float min = 0;
  int min_pos = 0;
  for(int y = 0; y < GET_IMAGE_HEIGHT(src); y++)
  {
    float value = READ_src_IMAGE(src,sampler,POS_src_INSTANCE(x,y,z,0)).x;
    if (value < min || y == 0) {
      min = value;
      min_pos = y;
    }
  }
  WRITE_dst_arg_IMAGE(dst_arg,POS_dst_arg_INSTANCE(x,z,0,0), CONVERT_dst_arg_PIXEL_TYPE(min_pos));
}