
__kernel void mean_x_projection (
    IMAGE_dst_TYPE dst,
    IMAGE_src_TYPE src
) {
  const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

  const int z = get_global_id(0);
  const int y = get_global_id(1);
  float sum = 0;
  int count = 0;
  for(int x = 0; x < GET_IMAGE_WIDTH(src); x++)
  {
    sum = sum + READ_src_IMAGE(src,sampler,POS_src_INSTANCE(x,y,z,0)).x;
    count++;
  }
  WRITE_dst_IMAGE(dst,POS_dst_INSTANCE(z,y,0,0), CONVERT_dst_PIXEL_TYPE(sum / count));
}