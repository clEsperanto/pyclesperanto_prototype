__kernel void point_index_list_to_touch_matrix(
    IMAGE_src_indexlist_TYPE src_indexlist,
    IMAGE_dst_matrix_TYPE dst_matrix
) {

  const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

  const int pointIndex = get_global_id(0);

  //int4 pointA = (int4){pointAx, pointAy, pointAz, 0};

  // so many point candidates are available:
  const int num_pointBs = GET_IMAGE_HEIGHT(src_indexlist);
  for (int pointB = 0; pointB < num_pointBs; pointB++) {
    float pointIndexB = READ_IMAGE(src_indexlist, sampler, POS_src_indexlist_INSTANCE(pointIndex, pointB, 0, 0)).x;
    if (pointIndexB < 0) {
      continue;
    }
    pointIndexB = pointIndexB - 1;
    printf("? %d: %d %d\n", pointB, (int)(pointIndex + 1), (int)(pointIndexB + 1));


    POS_dst_matrix_TYPE tPos;
    if (pointIndex == pointIndexB) {
        continue;
    } else if (pointIndex > pointIndexB) {
       // we add 1 here because the 0th column/row stands for background in touch matrices
        printf("A %d %d\n", (int)(pointIndex), (int)(pointIndexB));
       tPos = POS_dst_matrix_INSTANCE(pointIndexB + 1, pointIndex + 1, 0, 0);
    } else {
        printf("B %d %d\n", (int)(pointIndex), (int)(pointIndexB));
       tPos = POS_dst_matrix_INSTANCE(pointIndex + 1, pointIndexB + 1, 0, 0);
    }
    WRITE_dst_matrix_IMAGE(dst_matrix, tPos, 1);
  }
}