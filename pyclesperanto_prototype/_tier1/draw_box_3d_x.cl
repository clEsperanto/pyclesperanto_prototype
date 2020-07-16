__kernel void draw_box_3d   (
    IMAGE_dst_TYPE dst,
    float x1,
    float y1,
    float z1,
    float x2,
    float y2,
    float z2,
    float value
)
{
  const int x = get_global_id(0);
  const int y = get_global_id(1);
  const int z = get_global_id(2);

  if (!((x >= x1 && x <= x2) || (x >= x2 && x <= x1))) {
    return;
  }
  if (!((y >= y1 && y <= y2) || (y >= y2 && y <= y1))) {
    return;
  }
  if (!((z >= z1 && z <= z2) || (z >= z2 && z <= z1))) {
    return;
  }

  int4 ipos = (int4){x,y,z,0};
  WRITE_dst_IMAGE (dst, ipos, CONVERT_dst_PIXEL_TYPE(value));
}
