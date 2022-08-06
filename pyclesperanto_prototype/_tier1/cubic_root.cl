
__kernel void cubic_root(
    IMAGE_dst_TYPE dst,
    IMAGE_src_TYPE src
) {
  const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

  const int x = get_global_id(0);
  const int y = get_global_id(1);
  const int z = get_global_id(2);

  float value = (float)(READ_IMAGE(src,sampler, POS_src_INSTANCE(x, y, z,0)).x);
  value = cbrt(value);

  WRITE_IMAGE(dst, POS_dst_INSTANCE(x, y, z,0), CONVERT_dst_PIXEL_TYPE(value));
}