__constant sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

__kernel void greater_or_equal_constant_2d(
    IMAGE_src1_TYPE src1,
    float scalar,
    IMAGE_dst_TYPE  dst
)
{
  const int x = get_global_id(0);
  const int y = get_global_id(1);

  const int2 pos = (int2){x,y};

  const float input1 = (float)READ_src1_IMAGE(src1, sampler, pos).x;

  IMAGE_dst_PIXEL_TYPE value = 0;
  if (input1 >= scalar) {
    value = 1;
  }
  WRITE_dst_IMAGE (dst, pos, value);
}