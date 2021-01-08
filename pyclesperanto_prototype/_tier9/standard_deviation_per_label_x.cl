__kernel void standard_deviation_per_label (
    IMAGE_dst_TYPE dst,
    IMAGE_src_statistics_TYPE src_statistics,
    IMAGE_src_label_TYPE src_label,
    IMAGE_src_image_TYPE src_image,
    int sum_background,
    int z
) {
  const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

  const int y = get_global_id(1);
  int former_label = -1;

  float sum_distance_centroid = 0;
  float sum_distance_mass_center = 0;
  float sum_squared_difference = 0;
  float sum = 0;
  float max_distance_centroid = 0;
  float max_distance_mass_center = 0;

  int width = GET_IMAGE_WIDTH(src_label);

  for(int x = 0; x <= width; x++)
  {
    int label = (int)(READ_IMAGE(src_label,sampler,POS_src_label_INSTANCE(x,y,z,0)).x);
    float value = READ_IMAGE(src_image,sampler,POS_src_image_INSTANCE(x,y,z,0)).x;

    if (x == width || (label != former_label && former_label >= 0)) {

      if (former_label > 0 || sum_background != 0) {
        WRITE_IMAGE(dst,POS_dst_INSTANCE(former_label,y,0,0), CONVERT_dst_PIXEL_TYPE(sum_distance_centroid));
        WRITE_IMAGE(dst,POS_dst_INSTANCE(former_label,y,1,0), CONVERT_dst_PIXEL_TYPE(sum_distance_mass_center));
        WRITE_IMAGE(dst,POS_dst_INSTANCE(former_label,y,2,0), CONVERT_dst_PIXEL_TYPE(sum_squared_difference));
        WRITE_IMAGE(dst,POS_dst_INSTANCE(former_label,y,3,0), CONVERT_dst_PIXEL_TYPE(sum));
        WRITE_IMAGE(dst,POS_dst_INSTANCE(former_label,y,4,0), CONVERT_dst_PIXEL_TYPE(max_distance_centroid));
        WRITE_IMAGE(dst,POS_dst_INSTANCE(former_label,y,5,0), CONVERT_dst_PIXEL_TYPE(max_distance_mass_center));
      }
    }

    if (x != width && (label != former_label)) {
      if (label > 0 || sum_background != 0) {
        sum_distance_centroid = READ_IMAGE(dst,sampler,POS_dst_INSTANCE(label,y,0,0)).x;
        sum_distance_mass_center = READ_IMAGE(dst,sampler,POS_dst_INSTANCE(label,y,1,0)).x;
        sum_squared_difference = READ_IMAGE(dst,sampler,POS_dst_INSTANCE(label,y,2,0)).x;
        sum = READ_IMAGE(dst,sampler,POS_dst_INSTANCE(label,y,3,0)).x;
        max_distance_centroid = READ_IMAGE(dst,sampler,POS_dst_INSTANCE(label,y,4,0)).x;
        max_distance_mass_center = READ_IMAGE(dst,sampler,POS_dst_INSTANCE(label,y,5,0)).x;
      }
    }

    former_label = label;

    if (label > 0 || sum_background != 0) {
      float centroid_x = READ_IMAGE(src_statistics,sampler,POS_src_statistics_INSTANCE(label,0,0,0)).x;
      float centroid_y = READ_IMAGE(src_statistics,sampler,POS_src_statistics_INSTANCE(label,1,0,0)).x;
      float centroid_z = READ_IMAGE(src_statistics,sampler,POS_src_statistics_INSTANCE(label,2,0,0)).x;
      float mass_center_x = READ_IMAGE(src_statistics,sampler,POS_src_statistics_INSTANCE(label,3,0,0)).x;
      float mass_center_y = READ_IMAGE(src_statistics,sampler,POS_src_statistics_INSTANCE(label,4,0,0)).x;
      float mass_center_z = READ_IMAGE(src_statistics,sampler,POS_src_statistics_INSTANCE(label,5,0,0)).x;
      float mean_intensity = READ_IMAGE(src_statistics,sampler,POS_src_statistics_INSTANCE(label,6,0,0)).x;
      float area = READ_IMAGE(src_statistics,sampler,POS_src_statistics_INSTANCE(label,7,0,0)).x;

      const float centroid_distance = sqrt(
        pow((float)x - centroid_x, (float)2.0) +
        pow((float)y - centroid_y, (float)2.0) +
        pow((float)z - centroid_z, (float)2.0)
      );

      const float mass_center_distance = sqrt(
        pow((float)x - mass_center_x, (float)2.0) +
        pow((float)y - mass_center_y, (float)2.0) +
        pow((float)z - mass_center_z, (float)2.0)
      );

      const float intensity_difference_squared =
        pow(value - mean_intensity, (float)2.0) / area;

      if (sum == 0) { // no pixels yet found for this label
        max_distance_centroid = centroid_distance;
        max_distance_mass_center = mass_center_distance;
      } else {
        if (max_distance_centroid < centroid_distance) {
          max_distance_centroid = centroid_distance;
        }
        if (max_distance_mass_center < mass_center_distance) {
          max_distance_mass_center = mass_center_distance;
        }
      }

      sum_distance_centroid += centroid_distance;
      sum_distance_mass_center += mass_center_distance;
      sum_squared_difference += intensity_difference_squared;
      sum += 1;
    }
  }
}
