
const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

__kernel void flag_existing_intensities
(
  IMAGE_dst_TYPE dst,
  IMAGE_src_TYPE src
)
{
  const int i = get_global_id(0);
  const int j = get_global_id(1);
  const int k = get_global_id(2);

  int index = (int)(READ_IMAGE(src,sampler,POS_src_INSTANCE(i,j,k,0)).x);
  WRITE_IMAGE(dst, POS_dst_INSTANCE(index,0,0,0), 1);
}

