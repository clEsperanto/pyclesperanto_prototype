__constant sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;


__kernel void laplace_box_2d
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

  float valueA = READ_src_IMAGE(src, sampler, (pos + (int2){-1, -1})).x;
  float valueB = READ_src_IMAGE(src, sampler, (pos + (int2){1, -1})).x;
  float valueC = READ_src_IMAGE(src, sampler, (pos + (int2){-1, 1})).x;
  float valueD = READ_src_IMAGE(src, sampler, (pos + (int2){1, 1})).x;

  float result = valueCenter * 8.0 +
                valueRight * -1.0 +
                valueLeft * -1.0 +
                valueTop * -1.0 +
                valueBottom * -1.0 +
                valueA * -1.0 +
                valueB * -1.0 +
                valueC * -1.0 +
                valueD * -1.0;

  WRITE_dst_IMAGE (dst, pos, CONVERT_dst_PIXEL_TYPE(result));
}