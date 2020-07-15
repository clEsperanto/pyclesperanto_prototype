__constant sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;


__kernel void convolve_2d(
    IMAGE_src_TYPE src,
    IMAGE_kernelImage_TYPE kernelImage,
    IMAGE_dst_TYPE dst
) {
  const int i = get_global_id(0);
  const int j = get_global_id(1);

  int2 coord = (int2){i, j};

  const int kernelWidth = GET_IMAGE_WIDTH(kernelImage);
  const int kernelHeight = GET_IMAGE_HEIGHT(kernelImage);

  int2 c = (int2){kernelWidth / 2, kernelHeight / 2};

  float sum = 0;
  for (int x = -c.x; x <= c.x; x++) {
    for (int y = -c.y; y <= c.y; y++) {
        int2 kernelCoord = c + (int2)(x,y);
        int2 imageCoord = coord+(int2)(x,y);
        sum = sum + ((float)READ_IMAGE(kernelImage,sampler,kernelCoord).x
                  * (float)READ_IMAGE(src,sampler,imageCoord).x);
    }
  }
  WRITE_IMAGE(dst,coord,CONVERT_dst_PIXEL_TYPE(sum));
}


