
__kernel void set_plane_3d(
    IMAGE_dst_TYPE  dst,
    int plane,
    float value
)
{
  const int x = get_global_id(0);
  const int y = get_global_id(1);
  const int z = plane;

  WRITE_dst_IMAGE (dst, (int4)(x,y,z,0), CONVERT_dst_PIXEL_TYPE(value));
}

