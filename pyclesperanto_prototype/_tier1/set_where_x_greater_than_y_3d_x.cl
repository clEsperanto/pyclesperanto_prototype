
__kernel void set_where_x_greater_than_y_3d(
    IMAGE_dst_TYPE dst,
    float value
)
{
  const int x = get_global_id(0);
  const int y = get_global_id(1);
  const int z = get_global_id(2);
  if (x > y) {
    WRITE_IMAGE (dst, (int4)(x,y,z,0), CONVERT_dst_PIXEL_TYPE(value));
  }
}

