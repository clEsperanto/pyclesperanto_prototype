
__kernel void minimum_z_projection(
    IMAGE_dst_min_TYPE dst_min,
    IMAGE_src_TYPE src
) {
  const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

  const int x = get_global_id(0);
  const int y = get_global_id(1);
  float min = 0;
  for(int z = 0; z < GET_IMAGE_DEPTH(src); z++)
  {
    float value = READ_src_IMAGE(src,sampler,POS_src_INSTANCE(x,y,z,0)).x;
    if (value < min || z == 0) {
      min = value;
    }
  }
  WRITE_dst_min_IMAGE(dst_min,POS_dst_min_INSTANCE(x,y,0,0), CONVERT_dst_min_PIXEL_TYPE(min));
}
