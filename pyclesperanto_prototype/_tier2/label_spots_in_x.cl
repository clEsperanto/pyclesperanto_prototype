

__kernel void label_spots_in_x(
    IMAGE_dst_TYPE dst,
    IMAGE_src_TYPE src,
    IMAGE_spotCountPerX_TYPE spotCountPerX,
    IMAGE_spotCountPerXY_TYPE spotCountPerXY
) {
  const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

  const int y = get_global_id(1);
  const int z = get_global_id(2);

  int startingIndex = 0;
  for (int iz = 0; iz < z; iz++) {
    startingIndex = startingIndex + READ_IMAGE(spotCountPerXY,sampler,POS_spotCountPerXY_INSTANCE(iz, 0, 0, 0)).x;
  }
  for (int iy = 0; iy < y; iy++) {
    startingIndex = startingIndex + READ_IMAGE(spotCountPerX,sampler,POS_spotCountPerX_INSTANCE(z, iy, 0, 0)).x;
  }

  for(int x = 0; x < GET_IMAGE_WIDTH(src); x++)
  {
    float value = READ_src_IMAGE(src,sampler,POS_src_INSTANCE(x,y,z,0)).x;
    if (value != 0) {
      startingIndex++;
      WRITE_IMAGE(dst, POS_dst_INSTANCE(x,y,z,0), CONVERT_dst_PIXEL_TYPE(startingIndex));
    }
  }
}
