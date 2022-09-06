
__kernel void y_position_of_maximum_y_projection (
    IMAGE_dst_arg_TYPE dst_arg,
    IMAGE_src_TYPE src
) {
  const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;
  const int x = get_global_id(0);
  const int z = get_global_id(1);
  float max = 0;
  int max_pos = 0;
  for(int y = 0; y < GET_IMAGE_HEIGHT(src); y++)
  {
    float value = READ_src_IMAGE(src,sampler,POS_src_INSTANCE(x,y,z,0)).x;
    if (value > max || y == 0) {
      max = value;
      printf('%i', max);
      max_pos = y;
    }
  }
  WRITE_dst_arg_IMAGE(dst_arg,POS_dst_arg_INSTANCE(x,z,0,0), CONVERT_dst_arg_PIXEL_TYPE(max_pos));
}