__constant sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

__kernel void inferior_superior_2d (
    IMAGE_src_TYPE  src,
    IMAGE_dst_TYPE  dst
)
{
  const int x = get_global_id(0);
  const int y = get_global_id(1);

  const int2 pos = (int2){x,y};

  float value = READ_src_IMAGE(src, sampler, pos).x;

  // if value is already 1, dilate will return 1
  if (value == 1) {
    WRITE_dst_IMAGE(dst, pos, CONVERT_dst_PIXEL_TYPE(1));
    return;
  }

  /* Dilate with kernel [[1, 0, 0], 
                         [0, 1, 0], 
                         [0, 0, 1]] */
  value = READ_src_IMAGE(src, sampler, (pos + (int2){1, 1})).x;
  if (value == 0) {
    value = READ_src_IMAGE(src, sampler, (pos + (int2){-1, -1})).x;
    if (value == 0) {
      WRITE_dst_IMAGE(dst, pos, CONVERT_dst_PIXEL_TYPE(0));
      return;
    }
  }

  /* Dilate with kernel [[0, 1, 0], 
                         [0, 1, 0], 
                         [0, 1, 0]] */
  value = READ_src_IMAGE(src, sampler, (pos + (int2){0, 1})).x;
    if (value == 0) {
      value = READ_src_IMAGE(src, sampler, (pos + (int2){0, -1})).x;
      if (value == 0) {
        WRITE_dst_IMAGE(dst, pos, CONVERT_dst_PIXEL_TYPE(0));
        return;
      }
    }

  /* Dilate with kernel [[0, 0, 1], 
                         [0, 1, 0], 
                         [1, 0, 0]] */
  value = READ_src_IMAGE(src, sampler, (pos + (int2){-1, 1})).x;
    if (value == 0) {
      value = READ_src_IMAGE(src, sampler, (pos + (int2){1, -1})).x;
      if (value == 0) {
        WRITE_dst_IMAGE(dst, pos, CONVERT_dst_PIXEL_TYPE(0));
        return;
      }
    }

  /* Dilate with kernel [[0, 0, 0], 
                         [1, 1, 1], 
                         [0, 0, 0]] */
  value = READ_src_IMAGE(src, sampler, (pos + (int2){1, 0})).x;
    if (value == 0) {
      value = READ_src_IMAGE(src, sampler, (pos + (int2){-1, 0})).x;
      if (value == 0) {
        WRITE_dst_IMAGE(dst, pos, CONVERT_dst_PIXEL_TYPE(0));
        return;
      }
    }

  // If all dilates are 1 then return 1
  WRITE_dst_IMAGE(dst, pos, CONVERT_dst_PIXEL_TYPE(1));
}