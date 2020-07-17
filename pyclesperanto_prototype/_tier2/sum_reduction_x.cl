

__kernel void sum_reduction_x(
    IMAGE_dst_TYPE dst,
    IMAGE_src_TYPE src,
    int blocksize
) {
  const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

  const int x = get_global_id(0);
  const int z = get_global_id(1);
  const int y = get_global_id(2);
  float sum = 0;
  for(int dx = 0; dx < blocksize; dx++)
  {
    sum = sum + READ_src_IMAGE(src,sampler,POS_src_INSTANCE(x * blocksize + dx,y,z,0)).x;
  }
  WRITE_dst_IMAGE(dst,POS_dst_INSTANCE(x,y,z,0), CONVERT_dst_PIXEL_TYPE(sum));
}
