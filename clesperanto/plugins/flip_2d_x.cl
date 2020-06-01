
__kernel void flip_2d (    IMAGE_src_TYPE src,
                           IMAGE_dst_TYPE dst,
                           const          int        flipx,
                           const          int        flipy
                       )
{
  const sampler_t intsampler  = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_NONE | CLK_FILTER_NEAREST;

  const int x = get_global_id(0);
  const int y = get_global_id(1);

  const int width = get_global_size(0);
  const int height = get_global_size(1);

  const int2 pos = (int2)(flipx?(width-1-x):x,
                          flipy?(height-1-y):y);

  const float value = READ_src_IMAGE(src, intsampler, pos).x;

  WRITE_dst_IMAGE (dst, (int2)(x,y), CONVERT_dst_PIXEL_TYPE(value));
}
