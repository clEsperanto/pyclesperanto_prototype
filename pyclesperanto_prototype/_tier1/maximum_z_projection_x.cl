
__kernel void maximum_z_projection(
    IMAGE_dst_max_TYPE dst_max,
    IMAGE_src_TYPE src
) {
  const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

  const int x = get_global_id(0);
  const int y = get_global_id(1);
  float max = 0;
  for(int z = 0; z < GET_IMAGE_DEPTH(src); z++)
  {
    POS_src_TYPE pos = POS_src_INSTANCE(x,y,z,0);
    float value = READ_src_IMAGE(src,sampler,pos).x;
    if (value > max || z == 0) {
      max = value;
    }
  }
  POS_dst_max_TYPE pos = POS_dst_max_INSTANCE(x,y,0,0);
  WRITE_dst_max_IMAGE(dst_max, pos, CONVERT_dst_max_PIXEL_TYPE(max));
}