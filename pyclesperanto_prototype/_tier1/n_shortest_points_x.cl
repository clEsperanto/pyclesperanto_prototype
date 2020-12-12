
__kernel void find_n_closest_points(
    IMAGE_src_distancematrix_TYPE src_distancematrix,
    IMAGE_dst_indexlist_TYPE dst_indexlist
) {
  const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

  const int pointIndex = get_global_id(0);

  // so many point candidates are available:
  const int height = GET_IMAGE_HEIGHT(src_distancematrix);

  // so many minima need to be found:
  const int n = GET_IMAGE_HEIGHT(dst_indexlist);

  float distances[1000];
  float indices[1000];

  int initialized_values = 0;

  for (int y = 0; y < height; y++) {
    float distance = READ_src_distancematrix_IMAGE(src_distancematrix, sampler, POS_src_distancematrix_INSTANCE(pointIndex, y, 0, 0)).x;

    if (initialized_values < n) {
      initialized_values++;
      distances[initialized_values - 1] = distance;
      indices[initialized_values - 1] = y;
    }
    // sort by insert
    for (int i = initialized_values - 1; i >= 0; i--) {
        if (distance > distances[i]) {
            break;
        }
        if (distance < distances[i] && (i == 0 || distance >= distances[i - 1])) {
           for (int j = initialized_values - 1; j > i; j--) {
                indices[j] = indices[j - 1];
                distances[j] = distances[j - 1];
           }
           distances[i] = distance;
           indices[i] = y;
           break;
        }
    }
  }

  for (int i = 0; i < initialized_values; i++) {
    WRITE_dst_indexlist_IMAGE(dst_indexlist, POS_dst_indexlist_INSTANCE(pointIndex, i, 0, 0), CONVERT_dst_indexlist_PIXEL_TYPE(indices[i]));
  }
}