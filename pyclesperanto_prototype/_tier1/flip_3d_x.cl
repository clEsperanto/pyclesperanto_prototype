
__kernel void flip_3d (    IMAGE_src_TYPE src,
                           IMAGE_dst_TYPE dst,
                           const          int        flipx,
                           const          int        flipy,
                           const          int        flipz
                     )
{
  const sampler_t intsampler  = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_NONE | CLK_FILTER_NEAREST;

  const int x = get_global_id(0);
  const int y = get_global_id(1);
  const int z = get_global_id(2);

  const int width = get_global_size(0);
  const int height = get_global_size(1);
  const int depth = get_global_size(2);

  const int4 pos = (int4)(flipx?(width-1-x):x,
                          flipy?(height-1-y):y,
                          flipz?(depth-1-z):z,0);

  const float value = READ_src_IMAGE(src, intsampler, pos).x;

  WRITE_dst_IMAGE(dst, (int4)(x,y,z,0), CONVERT_dst_PIXEL_TYPE(value));
}
