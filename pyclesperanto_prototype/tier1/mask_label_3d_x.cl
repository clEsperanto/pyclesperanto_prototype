__constant sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

__kernel void mask_label_3d(
    IMAGE_src_TYPE src,
    IMAGE_src_label_map_TYPE src_label_map,
    const float label_id,
    IMAGE_dst_TYPE  dst
)
{
  const int x = get_global_id(0);
  const int y = get_global_id(1);
  const int z = get_global_id(2);

  const int4 pos = (int4){x,y,z,0};

  float value = 0;
  if (fabs(((float)READ_src_label_map_IMAGE(src_label_map, sampler, pos).x) - label_id) < 0.1) {
    value = READ_src_IMAGE(src, sampler, pos).x;
  }

  WRITE_dst_IMAGE (dst, pos, CONVERT_dst_PIXEL_TYPE(value));
}

