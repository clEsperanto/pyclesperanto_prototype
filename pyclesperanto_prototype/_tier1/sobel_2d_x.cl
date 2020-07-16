__constant sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

__kernel void sobel_2d
(
  IMAGE_dst_TYPE dst,
  IMAGE_src_TYPE src
)
{
  const int x = get_global_id(0);
  const int y = get_global_id(1);

  const int2 pos = (int2){x,y};

  float valueCenter = READ_src_IMAGE(src, sampler, pos).x;

  float valueRight = READ_src_IMAGE(src, sampler, (pos + (int2){1, 0})).x;
  float valueLeft = READ_src_IMAGE(src, sampler, (pos + (int2){-1, 0})).x;
  float valueBottom = READ_src_IMAGE(src, sampler, (pos + (int2){0, 1})).x;
  float valueTop = READ_src_IMAGE(src, sampler, (pos + (int2){0, -1})).x;

  float valueTopLeft = READ_src_IMAGE(src, sampler, (pos + (int2){-1, -1})).x;
  float valueTopRight = READ_src_IMAGE(src, sampler, (pos + (int2){1, -1})).x;
  float valueBottomLeft = READ_src_IMAGE(src, sampler, (pos + (int2){-1, 1})).x;
  float valueBottomRight = READ_src_IMAGE(src, sampler, (pos + (int2){1, 1})).x;

  float result_x = valueTopLeft * -1.0 +
                 valueLeft * -2.0 +
                 valueBottomLeft * -1.0 +
                 valueTopRight * 1.0 +
                 valueRight * 2.0 +
                 valueBottomRight * 1.0;

  float result_y = valueTopLeft * -1.0 +
                 valueTop * -2.0 +
                 valueTopRight * -1.0 +
                 valueBottomLeft * 1.0 +
                 valueBottom * 2.0 +
                 valueBottomRight * 1.0;

  float result = sqrt(result_x * result_x + result_y * result_y);
  WRITE_dst_IMAGE (dst, pos, CONVERT_dst_PIXEL_TYPE(result));
}

