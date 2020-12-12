// the following two methods originate from
// https://github.com/ClearControl/fastfuse/blob/master/src/main/java/fastfuse/tasks/kernels/downsampling.cl

#define min_nobranch(x,y) x < y ? x : y;
#define max_nobranch(x,y) x > y ? x : y;

inline void swap(IMAGE_dst_PIXEL_TYPE *a, int i, int j) {
  IMAGE_dst_PIXEL_TYPE t;
  t    = min_nobranch(a[i],a[j]);
  a[j] = max_nobranch(a[i],a[j]);
  a[i] = t;
}


__kernel void downsample_xy_by_half_median_3d (
    IMAGE_dst_TYPE dst,
    IMAGE_src_TYPE src
) {
  const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

  const int i = get_global_id(0), j = get_global_id(1), k = get_global_id(2);
  const POS_dst_TYPE coord_out = POS_dst_INSTANCE(i,j,k,0);
  const int x = 2*i, y = 2*j, z = k;

  IMAGE_src_PIXEL_TYPE pixel[4];
  pixel[0] = READ_src_IMAGE(src,sampler,(POS_src_INSTANCE(x+0,y+0,z,0))).x;
  pixel[1] = READ_src_IMAGE(src,sampler,(POS_src_INSTANCE(x+0,y+1,z,0))).x;
  pixel[2] = READ_src_IMAGE(src,sampler,(POS_src_INSTANCE(x+1,y+0,z,0))).x;
  pixel[3] = READ_src_IMAGE(src,sampler,(POS_src_INSTANCE(x+1,y+1,z,0))).x;

  // // sort pixel array
  // swap(pixel,0,1);
  // swap(pixel,2,3);
  // swap(pixel,0,2);
  // swap(pixel,1,3);
  // swap(pixel,1,2);

  // if ((pixel[0] > pixel[1]) ||
  //     (pixel[1] > pixel[2]) ||
  //     (pixel[2] > pixel[3]))
  //   printf("array not sorted for i=%d, j=%d, k=%d\n", i,j,k);

  // swap array elements such that pixel[0] = "min(pixel)" and pixel[3] = "max(pixel)"
  // this tiny performance improvement is only there to make Martin happy
  swap(pixel,0,1);
  swap(pixel,2,3);
  swap(pixel,0,2);
  swap(pixel,1,3);

  // if ( (pixel[0] > pixel[1]) || (pixel[0] > pixel[2]) || (pixel[0] > pixel[3]) ||
  //      (pixel[3] < pixel[2]) || (pixel[3] < pixel[1]) || (pixel[3] < pixel[0]) )
  //   printf("array not sorted for i=%d, j=%d, k=%d\n", i,j,k);

  // output is mean of medians
  const float out = (pixel[1] + pixel[2]) / 2.0f;

  WRITE_dst_IMAGE(dst,coord_out, CONVERT_dst_PIXEL_TYPE(out));
}





















