
__kernel void maximum_x_projection (
    IMAGE_dst_max_TYPE dst_max,
    IMAGE_src_TYPE src
) {
  const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

  const int z = get_global_id(0);
  const int y = get_global_id(1);
  float max = 0;
  for(int x = 0; x < GET_IMAGE_WIDTH(src); x++)
  {
    float value = READ_src_IMAGE(src,sampler,POS_src_INSTANCE(x,y,z,0)).x;
    if (value > max || x == 0) {
      max = value;
    }
  }
  WRITE_dst_max_IMAGE(dst_max,POS_dst_max_INSTANCE(z,y,0,0), CONVERT_dst_max_PIXEL_TYPE(max));
}