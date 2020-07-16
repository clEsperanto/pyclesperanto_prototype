__kernel void draw_line_2D   (IMAGE_dst_TYPE dst,
                                   float x1,
                                   float y1,
                                   float x2,
                                   float y2,
                                   float radius,
                                   float value
                     )
{
  const float x = min(x1, x2) - radius + get_global_id(0);
  const float y = min(y1, y2) - radius + get_global_id(1);

  if (!((x >= x1 - radius && x <= x2 + radius) || (x >= x2 - radius && x <= x1 + radius))) {
    return;
  }
  if (!((y >= y1 - radius && y <= y2 + radius) || (y >= y2 - radius && y <= y1 + radius))) {
    return;
  }


  float4 r = (float4){x-x2, y-y2, 0, 0};
  float4 r1 = (float4){x1-x2, y1-y2, 0, 0};
  float4 v = cross(r1, r);
  float distance = length(v) / length(r1);

  if (distance < radius) {
    int2 ipos = (int2){x,y};
    WRITE_dst_IMAGE (dst, ipos, CONVERT_dst_PIXEL_TYPE(value));
  }
}