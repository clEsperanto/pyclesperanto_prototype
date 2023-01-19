
#ifndef SAMPLER_FILTER
#define SAMPLER_FILTER CLK_FILTER_LINEAR
#endif

#ifndef SAMPLER_ADDRESS
#define SAMPLER_ADDRESS CLK_ADDRESS_CLAMP
#endif


__kernel void apply_vectorfield_2d(
    IMAGE_src_TYPE src,
    IMAGE_vectorX_TYPE vectorX,
    IMAGE_vectorY_TYPE vectorY,
    IMAGE_dst_TYPE dst
)
{
  const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE|
      SAMPLER_ADDRESS |	SAMPLER_FILTER;

  uint i = get_global_id(0);
  uint j = get_global_id(1);

  uint Nx = get_global_size(0);
  uint Ny = get_global_size(1);

  float x = i+0.5f;
  float y = j+0.5f;

  const POS_vectorX_TYPE posX = POS_vectorX_INSTANCE(i, j, 0, 0);
  const POS_vectorY_TYPE posY = POS_vectorY_INSTANCE(i, j, 0, 0);

  float x2 = x + (float)(READ_vectorX_IMAGE(vectorX, sampler, posX).x);
  float y2 = y + (float)(READ_vectorY_IMAGE(vectorY, sampler, posY).x);


  int2 coord_norm = (int2)(x2, y2);

  float pix = 0;
  if (x2 >= 0 && y2 >= 0 &&
      x2 < GET_IMAGE_WIDTH(src) && y2 < GET_IMAGE_HEIGHT(src)
  ) {
    pix = (float)(READ_src_IMAGE(src, sampler, coord_norm).x);
  }


  const POS_dst_TYPE posD = POS_dst_INSTANCE(i, j, 0, 0);
  WRITE_dst_IMAGE(dst, posD, CONVERT_dst_PIXEL_TYPE(pix));
}