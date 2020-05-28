__kernel void draw_sphere_3d   (
    IMAGE_dst_TYPE dst,
    float cx,
    float cy,
    float cz,
    float rx,
    float ry,
    float rz,
    float rxsq,
    float rysq,
    float rzsq,
    float value
)
{
  const float x = get_global_id(0);
  const float y = get_global_id(1);
  const float z = get_global_id(2);

  if ((x < cx - rx) || (x > cx + rx)) {
    return;
  }
  if ((y < cy - ry) || (y > cy + ry)) {
    return;
  }
  if ((z < cz - rz) || (z > cz + rz)) {
    return;
  }

  float xSquared = pow(x - cx, 2);
  float ySquared = pow(y - cy, 2);
  float zSquared = pow(z - cz, 2);

  if ((xSquared / rxsq + ySquared / rysq + zSquared / rzsq) <= 1.0) {
      int4 ipos = (int4){x,y,z,0};
      WRITE_dst_IMAGE (dst, ipos, CONVERT_dst_PIXEL_TYPE(value));
  }
}
