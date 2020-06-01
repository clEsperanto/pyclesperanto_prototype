
__kernel void set_ramp_z_2d(
    IMAGE_dst_TYPE  dst
)
{
  const int x = get_global_id(0);
  const int y = get_global_id(1);

  WRITE_dst_IMAGE (dst, (int4)(x,y,z,0), 0);
}

