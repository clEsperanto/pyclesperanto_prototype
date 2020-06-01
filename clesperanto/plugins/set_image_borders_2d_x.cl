
__kernel void set_image_borders_2d(
    IMAGE_dst_TYPE dst,
    float value
)
{
  const int x = get_global_id(0);
  const int y = get_global_id(1);

  if (x == 0 || x == GET_IMAGE_WIDTH(dst) - 1 || y == 0 || y == GET_IMAGE_HEIGHT(dst) - 1) {
    WRITE_dst_IMAGE (dst, POS_dst_INSTANCE(x,y,0,0), CONVERT_dst_PIXEL_TYPE(value));
  }
}
