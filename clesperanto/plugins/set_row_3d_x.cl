
__kernel void set_row_3d(
    IMAGE_dst_TYPE  dst,
    int row,
    float value
)
{
  const int x = get_global_id(0);
  const int y = row;
  const int z = get_global_id(2);

  WRITE_dst_IMAGE (dst, (int4)(x,y,z,0), CONVERT_dst_PIXEL_TYPE(value));
}

