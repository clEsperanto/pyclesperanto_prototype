

__kernel void power_images_3d(
    IMAGE_dst_TYPE dst,
    IMAGE_src1_TYPE src1,
    IMAGE_src2_TYPE src2
) {
  const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

  const int x = get_global_id(0);
  const int y = get_global_id(1);
  const int z = get_global_id(2);
  const int4 pos = (int4){x, y, z, 0};

  float a = READ_IMAGE(src1, sampler, pos).x;
  float b = READ_IMAGE(src2, sampler, pos).x;
  float result = pow(a, b);

  float out = result;
  WRITE_IMAGE(dst, pos, CONVERT_dst_PIXEL_TYPE(out));
}