
__kernel void minimum_y_projection (
    IMAGE_dst_min_TYPE dst_min,
    IMAGE_src_TYPE src
) {
  const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

  const int x = get_global_id(0);
  const int z = get_global_id(1);
  float min = 0;
  for(int y = 0; y < GET_IMAGE_HEIGHT(src); y++)
  {
    float value = READ_src_IMAGE(src,sampler,POS_src_INSTANCE(x,y,z,0)).x;
    if (value < min || y == 0) {
      min = value;
    }
  }
  WRITE_dst_min_IMAGE(dst_min,POS_dst_min_INSTANCE(x,z,0,0), CONVERT_dst_min_PIXEL_TYPE(min));
}