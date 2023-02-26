__kernel void maximum_intensity_between_points_matrix (
    IMAGE_src_touch_matrix_TYPE src_touch_matrix,
    IMAGE_src_pointlist_TYPE src_pointlist,
    IMAGE_src_intensity_TYPE src_intensity,                                            
    IMAGE_dst_maximum_intensity_matrix_TYPE dst_maximum_intensity_matrix,
    int num_samples
)
{
  const sampler_t intsampler  = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_NONE | CLK_FILTER_NEAREST;

  const int touch_x = get_global_id(0);
  const int touch_y = get_global_id(1);

  const int touching = READ_IMAGE(src_touch_matrix, intsampler, POS_src_touch_matrix_INSTANCE(touch_x, touch_y, 0, 0)).x;
  if (touching == 0 || touch_x == 0 || touch_y == 0) {
    WRITE_IMAGE (dst_maximum_intensity_matrix, POS_dst_maximum_intensity_matrix_INSTANCE(touch_x, touch_y,0,0), 0);
    return;
  }

  const float x1 = READ_IMAGE(src_pointlist, intsampler, POS_src_pointlist_INSTANCE(touch_x-1, 0, 0, 0)).x;
  const float y1 = READ_IMAGE(src_pointlist, intsampler, POS_src_pointlist_INSTANCE(touch_x-1, 1, 0, 0)).x;
  const float z1 = READ_IMAGE(src_pointlist, intsampler, POS_src_pointlist_INSTANCE(touch_x-1, 2, 0, 0)).x;

  const float x2 = READ_IMAGE(src_pointlist, intsampler, POS_src_pointlist_INSTANCE(touch_y-1, 0, 0, 0)).x;
  const float y2 = READ_IMAGE(src_pointlist, intsampler, POS_src_pointlist_INSTANCE(touch_y-1, 1, 0, 0)).x;
  const float z2 = READ_IMAGE(src_pointlist, intsampler, POS_src_pointlist_INSTANCE(touch_y-1, 2, 0, 0)).x;
  
  
  float4 directionVector = (float4){x2 - x1, y2 - y1, z2 - z1, 0};

  // const float len = length(directionVector);
  directionVector.x = directionVector.x / (num_samples - 1);
  directionVector.y = directionVector.y / (num_samples - 1);
  directionVector.z = directionVector.z / (num_samples - 1);

  if (touch_x == 1 && touch_y == 2) {
    printf("DIR %f / %f \n", directionVector.x, directionVector.y);
  }

  int width = GET_IMAGE_WIDTH(src_intensity);
  int height = GET_IMAGE_HEIGHT(src_intensity);
  int depth = GET_IMAGE_DEPTH(src_intensity);

  float4 position = (float4){x1, y1, z1, 0};
  float maximum = 0;

  for (int i = 0; i < num_samples; i++) {
      POS_src_intensity_TYPE pos = POS_src_intensity_INSTANCE((int)(position.x + 0.5), (int)(position.y + 0.5), (int)(position.z + 5), 0);

      float value = (float)(READ_IMAGE(src_intensity, intsampler, pos).x);
      if (maximum < value || i == 0) {
        maximum = value;
      }

      position = position + directionVector;
  }

  WRITE_IMAGE (dst_maximum_intensity_matrix, POS_dst_maximum_intensity_matrix_INSTANCE(touch_x, touch_y,0,0), maximum);
}
