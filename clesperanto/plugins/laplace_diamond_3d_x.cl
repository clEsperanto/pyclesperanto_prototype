__constant sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

__kernel void laplace_diamond_3d
(
  IMAGE_dst_TYPE dst,
  IMAGE_src_TYPE src
)
{
  const int x = get_global_id(0);
  const int y = get_global_id(1);
  const int z = get_global_id(2);

  const int4 pos = (int4){x,y,z,0};

  float valueCenter = READ_src_IMAGE(src, sampler, pos).x;

  float valueRight = READ_src_IMAGE(src, sampler, (pos + (int4){1, 0, 0, 0})).x;
  float valueLeft = READ_src_IMAGE(src, sampler, (pos + (int4){-1, 0, 0, 0})).x;
  float valueBottom = READ_src_IMAGE(src, sampler, (pos + (int4){0, 1, 0, 0})).x;
  float valueTop = READ_src_IMAGE(src, sampler, (pos + (int4){0, -1, 0, 0})).x;
  float valueFront = READ_src_IMAGE(src, sampler, (pos + (int4){0, 0, 1, 0})).x;
  float valueBack = READ_src_IMAGE(src, sampler, (pos + (int4){0, 0, -1, 0})).x;

  float result = valueCenter * 6.0 +
                valueRight * -1.0 +
                valueLeft * -1.0 +
                valueTop * -1.0 +
                valueBottom * -1.0 +
                valueFront * -1.0 +
                valueBack * -1.0;

  WRITE_dst_IMAGE(dst, pos, CONVERT_dst_PIXEL_TYPE(result));
}
