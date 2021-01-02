__kernel void sum_per_label (
    IMAGE_dst_TYPE dst,
    IMAGE_src_TYPE src,
    int sum_background,
    int z
) {
  const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

  const int y = get_global_id(1);

  for(int x = 0; x < GET_IMAGE_WIDTH(src); x++)
  {
    int label = (int)(READ_src_IMAGE(src,sampler,POS_src_INSTANCE(x,y,z,0)).x);

    if (label > 0 || sum_background != 0) {
      float sum_x = READ_dst_IMAGE(dst,sampler,POS_dst_INSTANCE(label,y,0,0)).x + x;
      float sum_y = READ_dst_IMAGE(dst,sampler,POS_dst_INSTANCE(label,y,1,0)).x + y;
      float sum_z = READ_dst_IMAGE(dst,sampler,POS_dst_INSTANCE(label,y,2,0)).x + z;
      float sum = READ_dst_IMAGE(dst,sampler,POS_dst_INSTANCE(label,y,3,0)).x + 1;


      WRITE_dst_IMAGE(dst,POS_dst_INSTANCE(label,y,0,0), CONVERT_dst_PIXEL_TYPE(sum_x));
      WRITE_dst_IMAGE(dst,POS_dst_INSTANCE(label,y,1,0), CONVERT_dst_PIXEL_TYPE(sum_y));
      WRITE_dst_IMAGE(dst,POS_dst_INSTANCE(label,y,2,0), CONVERT_dst_PIXEL_TYPE(sum_z));
      WRITE_dst_IMAGE(dst,POS_dst_INSTANCE(label,y,3,0), CONVERT_dst_PIXEL_TYPE(sum));
    }
  }
}
