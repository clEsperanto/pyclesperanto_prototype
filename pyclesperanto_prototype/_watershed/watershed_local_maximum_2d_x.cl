__kernel void watershed_local_maximum_2d
(
  IMAGE_src_labelmap_TYPE src_labelmap,
  IMAGE_src_distancemap_TYPE src_distancemap,
  IMAGE_dst_labelmap_TYPE dst_labelmap,
  IMAGE_dst_distancemap_TYPE dst_distancemap,
  IMAGE_flag_dst_TYPE flag_dst,
  IMAGE_src_mask_TYPE src_mask,
  IMAGE_src_original_distance_map_TYPE src_original_distance_map
)
{
  const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

  const int x = get_global_id(0);
  const int y = get_global_id(1);

  const int2 pos = (int2){x,y};

  float mask_value = READ_IMAGE(src_mask, sampler, pos).x;
  float currentlabel = READ_IMAGE(src_labelmap, sampler, pos).x;
  float currentdistance = READ_IMAGE(src_distancemap, sampler, pos).x;
  float originaldistance = READ_IMAGE(src_original_distance_map, sampler, pos).x;

  float bestlabel = currentlabel;
  float bestdistance = currentdistance;

  if (mask_value > 0 && currentlabel < 1) {
      for (int ax = -1; ax <= 1; ax++) {
        for (int ay = -1; ay <= 1; ay++) {
          float distance = READ_IMAGE(src_distancemap, sampler, (pos + (int2){ax, ay})).x;
          float remote_distance = READ_IMAGE(src_original_distance_map, sampler, (pos + (int2){ax, ay})).x;
          //if (distance > 0) {
          if (distance > bestdistance) {
            //if (distance > bestdistance) {
              float label = READ_IMAGE(src_labelmap, sampler, (pos + (int2){ax, ay})).x;
              bestdistance = distance;
              bestlabel = label;
            //}
          }
        }
      }

    if (fabs(((float)bestlabel - currentlabel)) > 0) {
      WRITE_flag_dst_IMAGE(flag_dst,(int4)(0,0,0,0),1);
    }
  }
  WRITE_dst_labelmap_IMAGE (dst_labelmap, pos, CONVERT_dst_labelmap_PIXEL_TYPE(bestlabel));
  WRITE_dst_distancemap_IMAGE (dst_distancemap, pos, CONVERT_dst_distancemap_PIXEL_TYPE(bestdistance));
}
