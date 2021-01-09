__kernel void maximum_distance_of_n_closest_points(
    IMAGE_src_distancematrix_TYPE src_distancematrix,
    IMAGE_dst_distancelist_TYPE dst_distancelist,
    int nPoints
) {
  const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

  const int pointIndex = get_global_id(0);

  // so many point candidates are available:
  const int height = GET_IMAGE_HEIGHT(src_distancematrix);

  float distances[1000];
  float indices[1000];

  int initialized_values = 0;

  // start at 1 to exclude background
  for (int y = 1; y < height; y++) {
    if (pointIndex != y) { // exclude distance to self
        float distance = READ_src_distancematrix_IMAGE(src_distancematrix, sampler, POS_src_distancematrix_INSTANCE(pointIndex, y, 0, 0)).x;

        if (initialized_values < nPoints) {
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
  }

  float maximum = -1;

  for (int i = 0; i < initialized_values; i++) {
    if (distances[i] > maximum) {
      maximum = distances[i];
    }
  }

  WRITE_dst_distancelist_IMAGE(dst_distancelist, POS_dst_distancelist_INSTANCE(pointIndex, 0, 0, 0), CONVERT_dst_distancelist_PIXEL_TYPE(maximum));
}