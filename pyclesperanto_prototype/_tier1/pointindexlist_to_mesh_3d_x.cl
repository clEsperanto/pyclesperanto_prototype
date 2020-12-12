__kernel void pointindexlist_to_mesh_3d(
IMAGE_src_pointlist_TYPE src_pointlist,
IMAGE_src_indexlist_TYPE src_indexlist,
IMAGE_dst_mesh_TYPE dst_mesh) {

  const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

  const int pointIndex = get_global_id(0);
  if (pointIndex == 0) {
    return;
  }
  const float pointAx = READ_src_pointlist_IMAGE(src_pointlist, sampler, POS_src_pointlist_INSTANCE(pointIndex - 1, 0, 0, 0)).x;
  const float pointAy = READ_src_pointlist_IMAGE(src_pointlist, sampler, POS_src_pointlist_INSTANCE(pointIndex - 1, 1, 0, 0)).x;
  const float pointAz = READ_src_pointlist_IMAGE(src_pointlist, sampler, POS_src_pointlist_INSTANCE(pointIndex - 1, 2, 0, 0)).x;

  //int4 pointA = (int4){pointAx, pointAy, pointAz, 0};

  // so many point candidates are available:
  const int num_pointBs = GET_IMAGE_HEIGHT(src_indexlist);
  for (int pointB = 0; pointB < num_pointBs; pointB++) {
    const float pointBIndex = READ_src_indexlist_IMAGE(src_indexlist, sampler, POS_src_indexlist_INSTANCE(pointIndex, pointB, 0, 0)).x - 1;
    if (pointBIndex < 0) {
      continue;
    }

    const float pointBx = READ_src_pointlist_IMAGE(src_pointlist, sampler, POS_src_pointlist_INSTANCE(pointBIndex, 0, 0, 0)).x;
    const float pointBy = READ_src_pointlist_IMAGE(src_pointlist, sampler, POS_src_pointlist_INSTANCE(pointBIndex, 2, 0, 0)).x;
    const float pointBz = READ_src_pointlist_IMAGE(src_pointlist, sampler, POS_src_pointlist_INSTANCE(pointBIndex, 3, 0, 0)).x;

    // draw line from A to B
    float distanceX = pow(pointAx - pointBx, (float)2.0);
    float distanceY = pow(pointAy - pointBy, (float)2.0);
    float distanceZ = pow(pointAz - pointBz, (float)2.0);

    float distance = sqrt(distanceX + distanceY + distanceZ);
    for (float d = 0; d < distance; d = d + 0.5) {
      POS_dst_mesh_TYPE tPos = POS_dst_mesh_INSTANCE(pointAx + (pointBx - pointAx) * d / distance,
                         pointAy + (pointBy - pointAy) * d / distance,
                         pointAz + (pointBz - pointAz) * d / distance,
                         0);
      WRITE_dst_mesh_IMAGE(dst_mesh, tPos, 1);
    }
  }
}