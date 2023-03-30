__constant sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

__kernel void superior_inferior_2d (
    IMAGE_src_TYPE  src,
    IMAGE_dst_TYPE  dst
)
{
  const int x = get_global_id(0);
  const int y = get_global_id(1);

  const int2 pos = (int2){x,y};

  float value = READ_src_IMAGE(src, sampler, pos).x;

  if (value != 0) {
    /* Erode with kernel [[1, 0, 0], 
                          [0, 1, 0], 
                          [0, 0, 1]] */
    value = READ_src_IMAGE(src, sampler, (pos + (int2){1, 1})).x;
    if (value != 0) {
        value = READ_src_IMAGE(src, sampler, (pos + (int2){-1, -1})).x;
    }
    // continue if value is zero after first erode as we are looking for max after all erodes i.e. value = 1
    if (value == 0) {
      /* Erode with kernel [[0, 1, 0], 
                            [0, 1, 0], 
                            [0, 1, 0]] */
      value = READ_src_IMAGE(src, sampler, (pos + (int2){0, 1})).x;
      if (value != 0) {
          value = READ_src_IMAGE(src, sampler, (pos + (int2){0, -1})).x;
      }

      if (value == 0) {
        /* Erode with kernel [[0, 0, 1], 
                              [0, 1, 0], 
                              [1, 0, 0]] */
        value = READ_src_IMAGE(src, sampler, (pos + (int2){-1, 1})).x;
        if (value != 0) {
            value = READ_src_IMAGE(src, sampler, (pos + (int2){1, -1})).x;
        }

        if (value == 0) {
          /* Erode with kernel [[0, 0, 0], 
                                [1, 1, 1], 
                                [0, 0, 0]] */
          value = READ_src_IMAGE(src, sampler, (pos + (int2){1, 0})).x;
          if (value != 0) {
              value = READ_src_IMAGE(src, sampler, (pos + (int2){-1, 0})).x;
          }
        }
      }
    }
  }

  if (value != 0) {
    value = 1;
  }

  WRITE_dst_IMAGE (dst, pos, CONVERT_dst_PIXEL_TYPE(value));
}