

inline void sort(float array[], int array_size)
{
    float temp;
    for(int i = 0; i < array_size; i++) {
        int j;
        temp = array[i];
        for(j = i - 1; j >= 0 && temp < array[j]; j--) {
            array[j+1] = array[j];
        }
        array[j+1] = temp;
    }
}

inline float median(float array[], int array_size)
{
    sort(array, array_size);
    return array[array_size / 2];
}

__kernel void median_value_of_touching_neighbors (
    IMAGE_src_values_TYPE src_values,
    IMAGE_src_touch_matrix_TYPE src_touch_matrix,
    IMAGE_dst_values_TYPE dst_values,
    int x_correction
) {
  const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

  const int label_id = get_global_id(0);
  const int label_count = get_global_size(0);

  float array[MAX_ARRAY_SIZE];

  int count = 0;
  float sum = 0;

  int y = label_id;
  int x = 0;
  for (x = 0; x < label_id; x++) {
    float value = READ_IMAGE(src_touch_matrix, sampler, POS_src_touch_matrix_INSTANCE(x, y, 0, 0)).x;
    if (value > 0) {
      array[count] = READ_IMAGE(src_values, sampler, POS_src_values_INSTANCE(x + x_correction, 0, 0, 0)).x;
      count++;
    }
  }

  // assume the object is included in mean calculation
  array[count] = READ_IMAGE(src_values, sampler, POS_src_values_INSTANCE(label_id + x_correction, 0, 0, 0)).x;
  count++;

  x = label_id;
  for (y = label_id + 1; y < label_count; y++) {
    float value = READ_IMAGE(src_touch_matrix, sampler, POS_src_touch_matrix_INSTANCE(x, y, 0, 0)).x;
    if (value > 0) {
      array[count] =  READ_IMAGE(src_values, sampler, POS_src_values_INSTANCE(y + x_correction, 0, 0, 0)).x;
      count++;
    }
  }

  float med = median(array, count);
  WRITE_IMAGE(dst_values, POS_dst_values_INSTANCE(label_id, 0, 0, 0), CONVERT_dst_values_PIXEL_TYPE(med));
}

