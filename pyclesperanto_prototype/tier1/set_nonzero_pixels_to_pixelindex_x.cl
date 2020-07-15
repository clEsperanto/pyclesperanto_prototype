__constant sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

__kernel void set_nonzero_pixels_to_pixelindex
(
  IMAGE_dst_TYPE dst,
  IMAGE_src_TYPE src
)
{
  const int i = get_global_id(0);
  const int j = get_global_id(1);
  const int k = get_global_id(2);

  const int w = GET_IMAGE_WIDTH(src);
  const int h = GET_IMAGE_HEIGHT(src);
  const int d = GET_IMAGE_DEPTH(src);

  float pixelindex = i * h * d + j * d + k;
  float value = (float)(READ_src_IMAGE(src,sampler,POS_src_INSTANCE(i,j,k,0)).x);
  if (value != 0) {
    WRITE_dst_IMAGE(dst, POS_dst_INSTANCE(i,j,k,0),pixelindex);
  } else {
    WRITE_dst_IMAGE(dst, POS_dst_INSTANCE(i,j,k,0), 0);
  }
}
