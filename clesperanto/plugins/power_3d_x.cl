__constant sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

__kernel void power_3d(
    IMAGE_src_TYPE  src,
    IMAGE_dst_TYPE  dst,
    float exponent
)
{
  const int x = get_global_id(0);
  const int y = get_global_id(1);
  const int z = get_global_id(2);

  const int4 pos = (int4){x,y,z,0};

  const IMAGE_src_PIXEL_TYPE input = READ_src_IMAGE(src, sampler, pos).x;

  const IMAGE_dst_PIXEL_TYPE value = CONVERT_dst_PIXEL_TYPE(pow(input, exponent));

  WRITE_dst_IMAGE (dst, pos, value);
}
