__constant sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

__kernel void add_images_weighted_3d(
IMAGE_src_TYPE  src,
IMAGE_src1_TYPE  src1,
IMAGE_dst_TYPE   dst,
float factor,
float factor1
)
{
  const int x = get_global_id(0);
  const int y = get_global_id(1);
  const int z = get_global_id(2);

  const int4 pos = (int4)(x,y,z,0);

  const float value1 = factor * ((float)(READ_IMAGE(src, sampler, pos).x));
  const float value2 = factor1 * ((float)(READ_IMAGE(src1, sampler, pos).x));

  float value = value1 + value2;

  WRITE_IMAGE (dst, pos, CONVERT_dst_PIXEL_TYPE( value));
}