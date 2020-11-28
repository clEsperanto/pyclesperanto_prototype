__constant sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

__kernel void not_equal_3d(
    IMAGE_src1_TYPE src1,
    IMAGE_src2_TYPE src2,
    IMAGE_dst_TYPE dst
)
{
  const int x = get_global_id(0);
  const int y = get_global_id(1);
  const int z = get_global_id(2);

  const int4 pos = (int4){x,y,z,0};

  const float input1 = (float)READ_src1_IMAGE(src1, sampler, pos).x;
  const float input2 = (float)READ_src2_IMAGE(src2, sampler, pos).x;

  IMAGE_dst_PIXEL_TYPE value = 0;
  if (input1 != input2) {
    value = 1;
  }
  WRITE_dst_IMAGE (dst, pos, value);
}
