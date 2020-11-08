__constant sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

__kernel void detect_label_edges_diamond_3d
(
  IMAGE_src_label_map_TYPE src_label_map, IMAGE_dst_edge_image_TYPE dst_edge_image
)
{
  const int x = get_global_id(0);
  const int y = get_global_id(1);
  const int z = get_global_id(2);

  const int4 pos = (int4){x,y,z,0};

  float center = READ_src_label_map_IMAGE(src_label_map, sampler, pos).x;
  float valueToWrite = 0;

  float value = READ_src_label_map_IMAGE(src_label_map, sampler, (pos + (int4){-1, 0, 0, 0})).x;
  if ( value != center) {
    valueToWrite = 1;
  } else {
    value = READ_src_label_map_IMAGE(src_label_map, sampler, (pos + (int4){0, -1, 0, 0})).x;
    if ( value != center ) {
      valueToWrite = 1;
    } else {
      value = READ_src_label_map_IMAGE(src_label_map, sampler, (pos + (int4){0, 0, -1, 0})).x;
      if ( value != center ) {
        valueToWrite = 1;
      } else {
        value = READ_src_label_map_IMAGE(src_label_map, sampler, (pos + (int4){1, 0, 0, 0})).x;
        if ( value != center ) {
          valueToWrite = 1;
        } else {
          value = READ_src_label_map_IMAGE(src_label_map, sampler, (pos + (int4){0, 1, 0, 0})).x;
          if ( value != center ) {
            valueToWrite = 1;
          } else {
            value = READ_src_label_map_IMAGE(src_label_map, sampler, (pos + (int4){0, 0, 1, 0})).x;
            if ( value != center ) {
              valueToWrite = 1;
            }
          }
        }
      }
    }
  }
  WRITE_dst_edge_image_IMAGE (dst_edge_image, pos, CONVERT_dst_edge_image_PIXEL_TYPE(valueToWrite));
}

