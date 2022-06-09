const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

__kernel void cross_correlation(IMAGE_src1_TYPE src1,
                                    IMAGE_mean_src1_TYPE mean_src1,
                                    IMAGE_src2_TYPE src2,
                                    float mean_src2,
                                    IMAGE_dst_TYPE dst)
{

    const int x = get_global_id(0);
    const int y = get_global_id(1);
    const int z = get_global_id(2);

    const int kernelWidth  = GET_IMAGE_WIDTH(src2)  > 1 ? GET_IMAGE_WIDTH(src2)  : 1;
    const int kernelHeight = GET_IMAGE_HEIGHT(src2) > 1 ? GET_IMAGE_HEIGHT(src2) : 1;
    const int kernelDepth  = GET_IMAGE_DEPTH(src2)  > 1 ? GET_IMAGE_DEPTH(src2)  : 1;

    const int4 c = (int4){kernelWidth / 2, kernelHeight / 2, kernelDepth / 2, 0};

    const POS_src1_TYPE pos = POS_src1_INSTANCE(x, y, z, 0);

    printf(" ");
    if (x == 0 && y == 0) {
        printf("%d %d", kernelWidth, kernelHeight);
    }

    float sum1 = 0;
    float sum2 = 0;
    float sum3 = 0;

      for (int cx = -c.x; cx < (-c.x + kernelWidth); ++cx) {
        for (int cy = -c.y; cy < (-c.y + kernelHeight); ++cy) {
          for (int cz = -c.z; cz < (-c.z + kernelDepth); ++cz) {

            POS_src2_TYPE coord_kernel = POS_src2_INSTANCE(cx,cy,cz,0);
            POS_src1_TYPE coord_image = pos + POS_src1_INSTANCE(cx,cy,cz,0);

            float Ia = READ_IMAGE(src1, sampler, coord_image).x;
            float mean_Ia = READ_IMAGE(mean_src1, sampler, coord_image).x;

            float Ib = READ_IMAGE(src2, sampler, coord_kernel).x;


            sum1 = sum1 + (Ia - mean_Ia) * (Ib - mean_src2);
            sum2 = sum2 + pow((float)(Ia - mean_Ia), (float)2.0);
            sum3 = sum3 + pow((float)(Ib - mean_src2), (float)2.0);
          }
        }
      }
      if (x == 0 && y == 0) {
        printf("%f %f", sum2, sum3);
    }

      float result = sum1 / pow((float)(sum2 * sum3), (float)0.5);
      float n = kernelWidth * kernelHeight * kernelDepth;

      WRITE_IMAGE(dst, POS_dst_INSTANCE(x, y, z, 0), CONVERT_dst_PIXEL_TYPE(result));

}


// Go back to Robert's code
// Set radius to kernel size (mean image for source and one value for kernel)