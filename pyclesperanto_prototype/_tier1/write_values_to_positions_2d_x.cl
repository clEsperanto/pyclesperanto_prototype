__constant sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

__kernel void write_values_to_positions_2d
(
  IMAGE_dst_TYPE dst,
  IMAGE_src_TYPE src
)
{
  const int i = get_global_id(0);
  const POS_src_TYPE sourcePos = POS_src_INSTANCE(i, 0, 0, 0);

  const int x = READ_src_IMAGE(src,sampler, (sourcePos + POS_src_INSTANCE(0, 0, 0, 0))).x;
  const int y = READ_src_IMAGE(src,sampler, (sourcePos + POS_src_INSTANCE(0, 1, 0, 0))).x;
  const float v = READ_src_IMAGE(src,sampler, (sourcePos + POS_src_INSTANCE(0, 2, 0, 0))).x;

  const POS_dst_TYPE coord = POS_dst_INSTANCE(x, y, z, 0);
  WRITE_dst_IMAGE(dst,coord, CONVERT_dst_PIXEL_TYPE(v));
}
