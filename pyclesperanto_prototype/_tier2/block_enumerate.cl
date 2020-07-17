

__kernel void block_enumerate(
    IMAGE_dst_TYPE dst,
    IMAGE_src_TYPE src,
    IMAGE_src_sums_TYPE src_sums,
    int blocksize
) {
  const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

  const int x = get_global_id(0);
  const int z = get_global_id(1);
  const int y = get_global_id(2);
  float sum = 0;
  for(int sx = 0; sx < x - 1; sx++)
  {
    sum = sum + READ_src_sums_IMAGE(src_sums,sampler,POS_src_sums_INSTANCE(sx,y,z,0)).x;
  }

  for(int dx = 0; dx < blocksize; dx++)
  {
    float value = READ_src_IMAGE(src,sampler,POS_src_INSTANCE(x * blocksize + dx,y,z,0)).x;
    if (value != 0) {
      sum = sum + value;
      WRITE_dst_IMAGE(dst,POS_dst_INSTANCE(x * blocksize + dx,y,z,0), CONVERT_dst_PIXEL_TYPE(sum));
    } else {
      WRITE_dst_IMAGE(dst,POS_dst_INSTANCE(x * blocksize + dx,y,z,0), 0);
    }
  }
}
