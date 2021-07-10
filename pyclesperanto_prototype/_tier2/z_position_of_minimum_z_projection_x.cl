
__kernel void z_position_of_minimum_z_projection (
    IMAGE_dst_arg_TYPE dst_arg,
    IMAGE_src_TYPE src
) {
  const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

  const int x = get_global_id(0);
  const int y = get_global_id(1);
  float min = 0;
  int min_pos = 0;
  for(int z = 0; z < GET_IMAGE_DEPTH(src); z++)
  {
    float value = READ_src_IMAGE(src,sampler,POS_src_INSTANCE(x,y,z,0)).x;
    if (value < min || z == 0) {
      min = value;
      min_pos = z;
    }
  }
  WRITE_dst_arg_IMAGE(dst_arg,POS_dst_arg_INSTANCE(x,y,0,0), CONVERT_dst_arg_PIXEL_TYPE(min_pos));
}
