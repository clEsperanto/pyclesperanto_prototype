__constant sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

__kernel void maximum_separable_2d
(
  IMAGE_dst_TYPE dst,
  IMAGE_src_TYPE src,
  const int dim,
  const int N,
  const float s
)
{
  const int i = get_global_id(0), j = get_global_id(1);
  const int2 coord = (int2)(i,j);
  const int2 dir   = (int2)(dim==0,dim==1);

  // center
  const int   c = (N-1)/2;

  float res = (float)READ_src_IMAGE(src,sampler,coord).x;
  for (int v = -c; v <= c; v++) {
    if (v != 0) {
      res = max(res, (float)(READ_src_IMAGE(src,sampler,coord+v*dir).x));
    }
  }
  WRITE_dst_IMAGE(dst,coord, CONVERT_dst_PIXEL_TYPE(res));
}
