
__kernel void set_column_2d(
    IMAGE_dst_TYPE dst,
    int column,
    float value
)
{
  const int x = column;
  const int y = get_global_id(1);

  WRITE_dst_IMAGE (dst, (int2)(x,y), CONVERT_dst_PIXEL_TYPE(value));
}
