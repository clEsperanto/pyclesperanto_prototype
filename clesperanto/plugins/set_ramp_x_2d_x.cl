
__kernel void set_ramp_x_2d(
    IMAGE_dst_TYPE  dst
)
{
  const int x = get_global_id(0);
  const int y = get_global_id(1);

  WRITE_dst_IMAGE (dst, (int2)(x,y), CONVERT_dst_PIXEL_TYPE(x));
}

