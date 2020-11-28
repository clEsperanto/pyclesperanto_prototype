__constant sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

__kernel void detect_label_edges_diamond_2d
(
  IMAGE_src_label_map_TYPE src_label_map, IMAGE_dst_edge_image_TYPE dst_edge_image
)
{
  const int x = get_global_id(0);
  const int y = get_global_id(1);

  const int2 pos = (int2){x,y};

  float center = READ_src_label_map_IMAGE(src_label_map, sampler, pos).x;
  float valueToWrite = 0;
  float value = READ_src_label_map_IMAGE(src_label_map, sampler, (pos + (int2){-1, 0})).x;
  if ( value != center) {
    valueToWrite = 1;
  } else {
    value = READ_src_label_map_IMAGE(src_label_map, sampler, (pos + (int2){0, -1})).x;
    if ( value != center ) {
      valueToWrite = 1;
    } else {
      value = READ_src_label_map_IMAGE(src_label_map, sampler, (pos + (int2){1, 0})).x;
      if ( value != center ) {
        valueToWrite = 1;
      } else {
        value = READ_src_label_map_IMAGE(src_label_map, sampler, (pos + (int2){0, 1})).x;
        if ( value != center ) {
          valueToWrite = 1;
        }
      }
    }
  }

  WRITE_dst_edge_image_IMAGE (dst_edge_image, pos, CONVERT_dst_edge_image_PIXEL_TYPE(valueToWrite));
}

