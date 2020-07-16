__kernel void copy_2d(
    IMAGE_dst_TYPE dst, 
    IMAGE_src_TYPE src
) {
  const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

  const int dx = get_global_id(0);
  const int dy = get_global_id(1);


  const int2 pos = (int2){dx,dy};

  const float out = READ_src_IMAGE(src,sampler,pos).x;
  WRITE_dst_IMAGE(dst,pos, CONVERT_dst_PIXEL_TYPE(out));
}
