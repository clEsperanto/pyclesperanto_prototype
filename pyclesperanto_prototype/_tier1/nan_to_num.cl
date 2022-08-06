
__kernel void nan_to_num(
    IMAGE_dst_TYPE dst,
    IMAGE_src_TYPE src,
    float new_nan_value,
    float new_posinf_value,
    float new_neginf_value
) {
  const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

  const int x = get_global_id(0);
  const int y = get_global_id(1);
  const int z = get_global_id(2);

  if (isinf(new_posinf_value)) {
    new_posinf_value = FLT_MAX;
  }
  if (isinf(new_neginf_value)) {
    new_neginf_value = -FLT_MAX;
  }

  float value = READ_src_IMAGE(src,sampler, POS_src_INSTANCE(x, y, z,0)).x;
  if (isnan(value)) {
    value = new_nan_value;
  }
  if (isinf(value) && value > 0) {
    value = new_posinf_value;
  }
  if (isinf(value) && value < 0) {
    value = new_neginf_value;
  }

  WRITE_dst_IMAGE(dst, POS_dst_INSTANCE(x, y, z,0), CONVERT_dst_PIXEL_TYPE(value));
}