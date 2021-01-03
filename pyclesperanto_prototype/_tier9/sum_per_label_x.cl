__kernel void sum_per_label (
    IMAGE_dst_TYPE dst,
    IMAGE_src_TYPE src,
    int sum_background,
    int z
) {
  const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

  const int y = get_global_id(1);
  int former_label = -1;

  float sum_x = 0;
  float sum_y = 0;
  float sum_z = 0;
  float sum = 0;

  int width = GET_IMAGE_WIDTH(src);

  for(int x = 0; x <= width; x++)
  {
    int label = (int)(READ_src_IMAGE(src,sampler,POS_src_INSTANCE(x,y,z,0)).x);

    if (x == width || (label != former_label && former_label >= 0)) {

      if (former_label > 0 || sum_background != 0) {
        WRITE_dst_IMAGE(dst,POS_dst_INSTANCE(former_label,y,0,0), CONVERT_dst_PIXEL_TYPE(sum_x));
        WRITE_dst_IMAGE(dst,POS_dst_INSTANCE(former_label,y,1,0), CONVERT_dst_PIXEL_TYPE(sum_y));
        WRITE_dst_IMAGE(dst,POS_dst_INSTANCE(former_label,y,2,0), CONVERT_dst_PIXEL_TYPE(sum_z));
        WRITE_dst_IMAGE(dst,POS_dst_INSTANCE(former_label,y,3,0), CONVERT_dst_PIXEL_TYPE(sum));
      }
    }

    if (x != width && (label != former_label)) {
      if (label > 0 || sum_background != 0) {
        sum_x = READ_dst_IMAGE(dst,sampler,POS_dst_INSTANCE(label,y,0,0)).x;
        sum_y = READ_dst_IMAGE(dst,sampler,POS_dst_INSTANCE(label,y,1,0)).x;
        sum_z = READ_dst_IMAGE(dst,sampler,POS_dst_INSTANCE(label,y,2,0)).x;
        sum = READ_dst_IMAGE(dst,sampler,POS_dst_INSTANCE(label,y,3,0)).x;
      }
    }

    former_label = label;

    if (label > 0 || sum_background != 0) {
      sum_x = sum_x + x;
      sum_y = sum_y + y;
      sum_z = sum_z + z;
      sum = sum + 1;
    }
  }
}
