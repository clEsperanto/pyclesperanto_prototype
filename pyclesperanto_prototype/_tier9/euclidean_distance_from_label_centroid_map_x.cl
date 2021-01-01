
const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

__kernel void euclidean_distance_from_label_centroid_map
(
  IMAGE_dst_TYPE dst,
  IMAGE_src_TYPE src,
  IMAGE_pointlist_TYPE pointlist
)
{
  const int i = get_global_id(0);
  const int j = get_global_id(1);
  const int k = get_global_id(2);

  const int w = GET_IMAGE_WIDTH(src);
  const int h = GET_IMAGE_HEIGHT(src);
  const int d = GET_IMAGE_DEPTH(src);

  int index = (int)(READ_IMAGE(src,sampler,POS_src_INSTANCE(i,j,k,0)).x);
  float distance = 0;
  if (index > 0) {
      const float dx = (float)(READ_IMAGE(pointlist,sampler,POS_pointlist_INSTANCE(index,0,0,0)).x);
      const float dy = (float)(READ_IMAGE(pointlist,sampler,POS_pointlist_INSTANCE(index,1,0,0)).x);

      float dz = 0;
      if (d > 1) {
        dz = (float)(READ_IMAGE(pointlist,sampler,POS_pointlist_INSTANCE(index,2,0,0)).x);
      }
      const float distance_squared =
        pow((float)i - dx, (float)2.0) +
        pow((float)j - dy, (float)2.0) +
        pow((float)k - dz, (float)2.0) ;
      distance = sqrt(distance_squared);
  }
  WRITE_IMAGE(dst, POS_dst_INSTANCE(i,j,k,0), CONVERT_dst_PIXEL_TYPE(distance));
}

