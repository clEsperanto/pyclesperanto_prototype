__constant sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

__kernel void mean_separable_3d
(
  IMAGE_dst_TYPE dst,
  IMAGE_src_TYPE src,
  const int dim,
  const int N,
  const float s
)
{
  const int i = get_global_id(0);
  const int j = get_global_id(1);
  const int k = get_global_id(2);

  const int4 coord = (int4)(i,j,k,0);
  const int4 dir   = (int4)(dim==0, dim==1, dim==2, 0);

  // center
  const int   c = (N-1)/2;

  float res = 0;
  float count = 0;
  for (int v = -c; v <= c; v++) {
    res = res + (float)READ_src_IMAGE(src,sampler,coord + v * dir).x;
    count = count + 1;
  }
  res /= count;
  WRITE_dst_IMAGE(dst,coord, CONVERT_dst_PIXEL_TYPE(res));
}
