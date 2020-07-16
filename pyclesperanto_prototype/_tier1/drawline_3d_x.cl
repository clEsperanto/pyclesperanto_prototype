__kernel void draw_line_3D   (IMAGE_dst_TYPE dst,
                                   float x1,
                                   float y1,
                                   float z1,
                                   float x2,
                                   float y2,
                                   float z2,
                                   float radius,
                                   float value
                     )
{
  const float x = min(x1, x2) - radius + get_global_id(0);
  const float y = min(y1, y2) - radius + get_global_id(1);
  const float z = min(z1, z2) - radius + get_global_id(2);

  if (!((x >= x1 - radius && x <= x2 + radius) || (x >= x2 - radius && x <= x1 + radius))) {
    return;
  }
  if (!((y >= y1 - radius && y <= y2 + radius) || (y >= y2 - radius && y <= y1 + radius))) {
    return;
  }
  if (!((z >= z1 - radius && z <= z2 + radius) || (z >= z2 - radius && z <= z1 + radius))) {
    return;
  }


  float4 r = (float4){x-x2, y-y2, z-z2, 0};
  float4 r1 = (float4){x1-x2, y1-y2, z1-z2, 0};
  float4 v = cross(r1, r);
  float distance = length(v) / length(r1);

  if (distance < radius) {
    int4 ipos = (int4){x,y,z,0};
    WRITE_dst_IMAGE (dst, ipos, CONVERT_dst_PIXEL_TYPE(value));
  }
}
