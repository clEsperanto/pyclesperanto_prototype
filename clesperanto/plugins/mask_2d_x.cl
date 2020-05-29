__constant sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

__kernel void mask_2d(
    IMAGE_src_TYPE  src,
    IMAGE_mask_TYPE  mask,
    IMAGE_dst_TYPE dst
)
{
  const int x = get_global_id(0);
  const int y = get_global_id(1);

  const int2 pos = (int2){x,y};

  IMAGE_src_PIXEL_TYPE value = 0;
  if (READ_mask_IMAGE(mask, sampler, pos).x != 0) {
    value = READ_src_IMAGE(src, sampler, pos).x;
  }

  WRITE_dst_IMAGE (dst, pos, CONVERT_dst_PIXEL_TYPE(value));
}
