__constant sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;


__kernel void gradient_x_2d
(
  IMAGE_dst_TYPE dst, 
  IMAGE_src_TYPE src
)
{
  const int i = get_global_id(0), j = get_global_id(1);
  const int2 coord = (int2){i,j};
  const int2 coordA = (int2){i-1,j};
  const int2 coordB = (int2){i+1,j};

  float valueA = READ_src_IMAGE(src, sampler, coordA).x;
  float valueB = READ_src_IMAGE(src, sampler, coordB).x;
  IMAGE_dst_PIXEL_TYPE res = CONVERT_dst_PIXEL_TYPE(valueB - valueA);

  WRITE_dst_IMAGE(dst, coord, res);
}
