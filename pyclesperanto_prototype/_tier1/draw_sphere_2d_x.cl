
__kernel void draw_sphere_2d(
    IMAGE_dst_TYPE dst,
    float cx,
    float cy,
    float rx,
    float ry,
    float rxsq,
    float rysq,
    float value
)
{
  const float x = get_global_id(0);
  const float y = get_global_id(1);
/*
  if ((x < cx - rx) || (x > cx + rx)) {
    return;
  }
  if ((y < cy - ry) || (y > cy + ry)) {
    return;
  }*/

  float xSquared = pow(x - cx, 2);
  float ySquared = pow(y - cy, 2);

  if ((xSquared / rxsq + ySquared / rysq) <= 1.0) {
      int2 ipos = (int2){x,y};
      WRITE_dst_IMAGE(dst, ipos, CONVERT_dst_PIXEL_TYPE(value));
  }
}