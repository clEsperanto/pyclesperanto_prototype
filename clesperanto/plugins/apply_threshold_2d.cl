__constant sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

__kernel void apply_threshold_2d
(
IMAGE_src_TYPE src,
IMAGE_dst_TYPE dst,
float threshold
)
{
  const int x = get_global_id(0);
  const int y = get_global_id(1);

  const int2 pos = (int2){x,y};

  const IMAGE_src_PIXEL_TYPE inputValue = READ_src_IMAGE(src, sampler, pos).x;
  IMAGE_dst_PIXEL_TYPE value = 1.0;

  if (inputValue < threshold)
  {
    value = 0.0;
  }

  WRITE_dst_IMAGE(dst, pos, value);
}