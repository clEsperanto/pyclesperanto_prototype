
__kernel void set_2d(
    IMAGE_dst_TYPE dst,
    float value
)
{
  const int x = get_global_id(0);
  const int y = get_global_id(1);

  WRITE_dst_IMAGE (dst, (int2)(x,y), CONVERT_dst_PIXEL_TYPE(value));
}
