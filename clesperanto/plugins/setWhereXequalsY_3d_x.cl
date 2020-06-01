
__kernel void set_where_x_equals_y_3d(DTYPE_IMAGE_OUT_3D  dst,
                  float value
                     )
{
  const int x = get_global_id(0);
  const int y = get_global_id(1);
  const int z = get_global_id(2);
  if (x == y) {
    WRITE_IMAGE_3D (dst, (int4)(x,y,z,0), (DTYPE_OUT)value);
  }
}

