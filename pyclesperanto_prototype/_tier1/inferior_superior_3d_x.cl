__constant sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

__kernel void inferior_superior_3d (
    IMAGE_src_TYPE  src,
    IMAGE_dst_TYPE  dst
)
{
  const int x = get_global_id(0);
  const int y = get_global_id(1);
  const int z = get_global_id(2);

  const int4 pos = (int4){x, y, z, 0};

  float value = READ_src_IMAGE(src, sampler, pos).x;

  // if value is already 0, erode will return 0
  if (value != 0) {
    WRITE_dst_IMAGE(dst, pos, CONVERT_dst_PIXEL_TYPE(1));
    return;
  }

  // printf("pixel at coord x%i y%i z%i\n", x, y, z);


  // P0
  for (int i = -1; i <= 1; i++) {
      for (int j = -1; j <= 1; j++) {
        value = READ_src_IMAGE(src, sampler, (pos + (int4){i, j, 0, 0})).x;
        // printf("value %i\n", value);
        if (value != 0) {
          break;
        }
      }
      if (value != 0) {
        break;
      }
    }
  if (value == 0) {
    WRITE_dst_IMAGE(dst, pos, CONVERT_dst_PIXEL_TYPE(0));
    return;
  }

  // P1
  for (int i = -1; i <= 1; i++) {
      for (int j = -1; j <= 1; j++) {
        value = READ_src_IMAGE(src, sampler, (pos + (int4){i, 0, j, 0})).x;
        if (value != 0) {
          break;
        }
      }
      if (value != 0) {
        break;
      }
    }
  if (value == 0) {
    WRITE_dst_IMAGE(dst, pos, CONVERT_dst_PIXEL_TYPE(0));
    return;
  }

  // P2
  for (int i = -1; i <= 1; i++) {
      for (int j = -1; j <= 1; j++) {
        value = READ_src_IMAGE(src, sampler, (pos + (int4){0, i, j, 0})).x;
        if (value != 0) {
          break;
        }
      }
      if (value != 0) {
        break;
      }
    }
  if (value == 0) {
    WRITE_dst_IMAGE(dst, pos, CONVERT_dst_PIXEL_TYPE(0));
    return;
  }

  // P3
  for (int i = -1; i <= 1; i++) {
      for (int j = -1; j <= 1; j++) {
        value = READ_src_IMAGE(src, sampler, (pos + (int4){i, j, j, 0})).x;
        if (value != 0) {
          break;
        }
      }
      if (value != 0) {
        break;
      }
    }
  if (value == 0) {
    WRITE_dst_IMAGE(dst, pos, CONVERT_dst_PIXEL_TYPE(0));
    return;
  }

  // P4
  for (int i = -1; i <= 1; i++) {
      for (int j = -1; j <= 1; j++) {
        value = READ_src_IMAGE(src, sampler, (pos + (int4){j, i, -i, 0})).x;
        if (value != 0) {
          break;
        }
      }
      if (value != 0) {
        break;
      }
    }
  if (value == 0) {
    WRITE_dst_IMAGE(dst, pos, CONVERT_dst_PIXEL_TYPE(0));
    return;
  }

  // P5
  for (int i = -1; i <= 1; i++) {
      for (int j = -1; j <= 1; j++) {
        value = READ_src_IMAGE(src, sampler, (pos + (int4){i, j, i, 0})).x;
        if (value != 0) {
          break;
        }
      }
      if (value != 0) {
        break;
      }
    }
  if (value == 0) {
    WRITE_dst_IMAGE(dst, pos, CONVERT_dst_PIXEL_TYPE(0));
    return;
  }

  // P6
  for (int i = -1; i <= 1; i++) {
      for (int j = -1; j <= 1; j++) {
        value = READ_src_IMAGE(src, sampler, (pos + (int4){i, j, -i, 0})).x;
        if (value != 0) {
          break;
        }
      }
      if (value != 0) {
        break;
      }
    }
  if (value == 0) {
    WRITE_dst_IMAGE(dst, pos, CONVERT_dst_PIXEL_TYPE(0));
    return;
  }

  // P7
  for (int i = -1; i <= 1; i++) {
      for (int j = -1; j <= 1; j++) {
        value = READ_src_IMAGE(src, sampler, (pos + (int4){i, i, j, 0})).x;
        if (value != 0) {
          break;
        }
      }
      if (value != 0) {
        break;
      }
    }
  if (value == 0) {
    WRITE_dst_IMAGE(dst, pos, CONVERT_dst_PIXEL_TYPE(0));
    return;
  }

  // P8
  for (int i = -1; i <= 1; i++) {
      for (int j = -1; j <= 1; j++) {
        value = READ_src_IMAGE(src, sampler, (pos + (int4){i, -i, j, 0})).x;
        if (value != 0) {
          break;
        }
      }
      if (value != 0) {
        break;
      }
    }
  if (value == 0) {
    WRITE_dst_IMAGE(dst, pos, CONVERT_dst_PIXEL_TYPE(0));
    return;
  }

  // If all erodes are 0 then return 0
  WRITE_dst_IMAGE(dst, pos, CONVERT_dst_PIXEL_TYPE(1));
}