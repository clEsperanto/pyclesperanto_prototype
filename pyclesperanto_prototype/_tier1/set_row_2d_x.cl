
__kernel void set_row_2d(
    IMAGE_dst_TYPE dst,
    int row,
    float value
)
{
  const int x = get_global_id(0);
  const int y = row;

  WRITE_dst_IMAGE (dst, (int2)(x,y), CONVERT_dst_PIXEL_TYPE(value));
}
