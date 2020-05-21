__constant sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

__kernel void binary_edge_detection_diamond_image3d
(
  IMAGE_dst_TYPE dst, IMAGE_src_TYPE src
)
{
  const int x = get_global_id(0);
  const int y = get_global_id(1);
  const int z = get_global_id(2);

  const int4 pos = (int4){x,y,z,0};

  float valueToWrite = READ_src_IMAGE(src, sampler, pos).x;
  if (valueToWrite != 0) {
      valueToWrite = 0;
      float value = READ_src_IMAGE(src, sampler, (pos + (int4){1, 0, 0, 0})).x;
      if ( value == 0) {
        valueToWrite = 1;
      } else {
        value = READ_src_IMAGE(src, sampler, (pos + (int4){-1, 0, 0, 0})).x;
        if ( value == 0) {
          valueToWrite = 1;
        } else {
          value = READ_src_IMAGE(src, sampler, (pos + (int4){0, 1, 0, 0})).x;
          if ( value == 0) {
            valueToWrite = 1;
          } else {
            value = READ_src_IMAGE(src, sampler, (pos + (int4){0, -1, 0, 0})).x;
            if ( value == 0) {
              valueToWrite = 1;
            } else {
              value = READ_src_IMAGE(src, sampler, (pos + (int4){0, 0, 1, 0})).x;
              if ( value == 0) {
                valueToWrite = 1;
              } else {
                value = READ_src_IMAGE(src, sampler, (pos + (int4){0, 0, -1, 0})).x;
                if ( value == 0) {
                  valueToWrite = 1;
                }
              }
            }
          }
        }
      }
    }
    WRITE_dst_IMAGE (dst, pos, CONVERT_dst_PIXEL_TYPE(valueToWrite));
}

