__kernel void paste_3d(
    IMAGE_dst_TYPE dst,
    IMAGE_src_TYPE src,
    int destination_x,
    int destination_y,
    int destination_z
) {
  const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

  const int dx = get_global_id(0) + destination_x;
  const int dy = get_global_id(1) + destination_y;
  const int dz = get_global_id(2) + destination_z;


  const int sx = get_global_id(0);
  const int sy = get_global_id(1);
  const int sz = get_global_id(2);


  const POS_dst_TYPE dpos = POS_dst_INSTANCE(dx, dy, dz, 0);
  const POS_src_TYPE spos = POS_src_INSTANCE(sx, sy, sz, 0);

  const float out = READ_src_IMAGE(src, sampler, spos).x;
  WRITE_dst_IMAGE(dst, dpos, CONVERT_dst_PIXEL_TYPE(out));
}

