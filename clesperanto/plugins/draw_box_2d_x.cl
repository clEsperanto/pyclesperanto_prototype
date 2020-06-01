
__kernel void draw_box_2d   (
    IMAGE_dst_TYPE dst,
    float x1,
    float y1,
    float x2,
    float y2,
    float value
)
{
  const int x = get_global_id(0);
  const int y = get_global_id(1);

  if (!((x >= x1 && x <= x2) || (x >= x2 && x <= x1))) {
    return;
  }
  if (!((y >= y1 && y <= y2) || (y >= y2 && y <= y1))) {
    return;
  }

  int2 ipos = (int2){x,y};
  WRITE_dst_IMAGE (dst, ipos, CONVERT_dst_PIXEL_TYPE(value));
}