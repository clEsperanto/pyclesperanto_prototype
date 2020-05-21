__constant sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;


__kernel void convolve_3d(
    IMAGE_src_TYPE src,
    IMAGE_kernelImage_TYPE kernelImage,
    IMAGE_dst_TYPE dst
) {
  const int i = get_global_id(0);
  const int j = get_global_id(1);
  const int k = get_global_id(2);

  int4 coord = (int4){i, j, k, 0};

  const int kernelWidth = GET_IMAGE_WIDTH(kernelImage);
  const int kernelHeight = GET_IMAGE_HEIGHT(kernelImage);
  const int kernelDepth = GET_IMAGE_DEPTH(kernelImage);

  int4 c = (int4){kernelWidth / 2, kernelHeight / 2, kernelDepth / 2, 0};

  float sum = 0;
  for (int x = -c.x; x <= c.x; x++) {
    for (int y = -c.y; y <= c.y; y++) {
      for (int z = -c.z; z <= c.z; z++) {
        int4 kernelCoord = c + (int4)(x,y,z,0);
        int4 imageCoord = coord+(int4)(x,y,z,0);
        sum = sum + (float)READ_IMAGE(kernelImage,sampler,kernelCoord).x
                  * (float)READ_IMAGE(src,sampler,imageCoord).x;
      }
    }
  }

  WRITE_IMAGE(dst,coord, CONVERT_dst_PIXEL_TYPE(sum));
}
