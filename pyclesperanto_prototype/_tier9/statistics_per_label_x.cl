__kernel void statistics_per_label (
    IMAGE_dst_TYPE dst,
    IMAGE_src_label_TYPE src_label,
    IMAGE_src_image_TYPE src_image,
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

  float sum_intensity_x = 0;
  float sum_intensity_y = 0;
  float sum_intensity_z = 0;
  float sum_intensity = 0;

  float min_intensity = 0;
  float max_intensity = 0;

  float min_x = 0;
  float max_x = 0;

  float min_y = 0;
  float max_y = 0;

  float min_z = 0;
  float max_z = 0;

  int width = GET_IMAGE_WIDTH(src_label);

  for(int x = 0; x <= width; x++)
  {
    int label = (int)(READ_IMAGE(src_label,sampler,POS_src_label_INSTANCE(x,y,z,0)).x);
    float value = READ_IMAGE(src_image,sampler,POS_src_image_INSTANCE(x,y,z,0)).x;

    if (x == width || (label != former_label && former_label >= 0)) {

      if (former_label > 0 || sum_background != 0) {
        WRITE_IMAGE(dst,POS_dst_INSTANCE(former_label,y,0,0), CONVERT_dst_PIXEL_TYPE(sum_x));
        WRITE_IMAGE(dst,POS_dst_INSTANCE(former_label,y,1,0), CONVERT_dst_PIXEL_TYPE(sum_y));
        WRITE_IMAGE(dst,POS_dst_INSTANCE(former_label,y,2,0), CONVERT_dst_PIXEL_TYPE(sum_z));
        WRITE_IMAGE(dst,POS_dst_INSTANCE(former_label,y,3,0), CONVERT_dst_PIXEL_TYPE(sum));

        WRITE_IMAGE(dst,POS_dst_INSTANCE(former_label,y,4,0), CONVERT_dst_PIXEL_TYPE(sum_intensity_x));
        WRITE_IMAGE(dst,POS_dst_INSTANCE(former_label,y,5,0), CONVERT_dst_PIXEL_TYPE(sum_intensity_y));
        WRITE_IMAGE(dst,POS_dst_INSTANCE(former_label,y,6,0), CONVERT_dst_PIXEL_TYPE(sum_intensity_z));
        WRITE_IMAGE(dst,POS_dst_INSTANCE(former_label,y,7,0), CONVERT_dst_PIXEL_TYPE(sum_intensity));

        WRITE_IMAGE(dst,POS_dst_INSTANCE(former_label,y,8,0), CONVERT_dst_PIXEL_TYPE(min_intensity));
        WRITE_IMAGE(dst,POS_dst_INSTANCE(former_label,y,9,0), CONVERT_dst_PIXEL_TYPE(max_intensity));

        WRITE_IMAGE(dst,POS_dst_INSTANCE(former_label,y,10,0), CONVERT_dst_PIXEL_TYPE(min_x));
        WRITE_IMAGE(dst,POS_dst_INSTANCE(former_label,y,11,0), CONVERT_dst_PIXEL_TYPE(max_x));
        WRITE_IMAGE(dst,POS_dst_INSTANCE(former_label,y,12,0), CONVERT_dst_PIXEL_TYPE(min_y));
        WRITE_IMAGE(dst,POS_dst_INSTANCE(former_label,y,13,0), CONVERT_dst_PIXEL_TYPE(max_y));
        WRITE_IMAGE(dst,POS_dst_INSTANCE(former_label,y,14,0), CONVERT_dst_PIXEL_TYPE(min_z));
        WRITE_IMAGE(dst,POS_dst_INSTANCE(former_label,y,15,0), CONVERT_dst_PIXEL_TYPE(max_z));
      }
    }

    if (x != width && (label != former_label)) {
      if (label > 0 || sum_background != 0) {
        sum_x = READ_IMAGE(dst,sampler,POS_dst_INSTANCE(label,y,0,0)).x;
        sum_y = READ_IMAGE(dst,sampler,POS_dst_INSTANCE(label,y,1,0)).x;
        sum_z = READ_IMAGE(dst,sampler,POS_dst_INSTANCE(label,y,2,0)).x;
        sum = READ_IMAGE(dst,sampler,POS_dst_INSTANCE(label,y,3,0)).x;

        sum_intensity_x = READ_IMAGE(dst,sampler,POS_dst_INSTANCE(label,y,4,0)).x;
        sum_intensity_y = READ_IMAGE(dst,sampler,POS_dst_INSTANCE(label,y,5,0)).x;
        sum_intensity_z = READ_IMAGE(dst,sampler,POS_dst_INSTANCE(label,y,6,0)).x;
        sum_intensity = READ_IMAGE(dst,sampler,POS_dst_INSTANCE(label,y,7,0)).x;

        min_intensity = READ_IMAGE(dst,sampler,POS_dst_INSTANCE(label,y,8,0)).x;
        max_intensity = READ_IMAGE(dst,sampler,POS_dst_INSTANCE(label,y,9,0)).x;

        min_x = READ_IMAGE(dst,sampler,POS_dst_INSTANCE(label,y,10,0)).x;
        max_x = READ_IMAGE(dst,sampler,POS_dst_INSTANCE(label,y,11,0)).x;
        min_y = READ_IMAGE(dst,sampler,POS_dst_INSTANCE(label,y,12,0)).x;
        max_y = READ_IMAGE(dst,sampler,POS_dst_INSTANCE(label,y,13,0)).x;
        min_z = READ_IMAGE(dst,sampler,POS_dst_INSTANCE(label,y,14,0)).x;
        max_z = READ_IMAGE(dst,sampler,POS_dst_INSTANCE(label,y,15,0)).x;
      }
    }

    former_label = label;

    if (label > 0 || sum_background != 0) {

      if (sum == 0) { // no pixels yet found for this label
        min_intensity = value;
        max_intensity = value;
        min_x = x;
        max_x = x;
        min_y = y;
        max_y = y;
        min_z = z;
        max_z = z;
      } else {
        if (min_intensity > value) {
          min_intensity = value;
        }
        if (max_intensity < value) {
          max_intensity = value;
        }

        if (min_x > x) {
          min_x = x;
        }
        if (max_x < x) {
          max_x = x;
        }
        if (min_y > y) {
          min_y = y;
        }
        if (max_y < y) {
          max_y = y;
        }
        if (min_z > z) {
          min_z = z;
        }
        if (max_z < z) {
          max_z = z;
        }

      }

      sum_x = sum_x + x;
      sum_y = sum_y + y;
      sum_z = sum_z + z;
      sum = sum + 1;

      sum_intensity_x = sum_intensity_x + x * value;
      sum_intensity_y = sum_intensity_y + y * value;
      sum_intensity_z = sum_intensity_z + z * value;
      sum_intensity = sum_intensity + value;


    }
  }
}
