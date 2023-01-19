
#ifndef SAMPLER_FILTER
#define SAMPLER_FILTER CLK_FILTER_LINEAR
#endif

#ifndef SAMPLER_ADDRESS
#define SAMPLER_ADDRESS CLK_ADDRESS_CLAMP
#endif

__kernel void apply_vectorfield_3d_interpolate(
    IMAGE_src_TYPE src,
    IMAGE_vectorX_TYPE vectorX,
    IMAGE_vectorY_TYPE vectorY,
    IMAGE_vectorZ_TYPE vectorZ,
    IMAGE_dst_TYPE dst
)
{
  const sampler_t sampler = CLK_NORMALIZED_COORDS_TRUE|
      SAMPLER_ADDRESS |	SAMPLER_FILTER;

  uint i = get_global_id(0);
  uint j = get_global_id(1);
  uint k = get_global_id(2);

  uint Nx = GET_IMAGE_WIDTH(src);
  uint Ny = GET_IMAGE_HEIGHT(src);
  uint Nz = GET_IMAGE_DEPTH(src);

  float x = i+0.5f;
  float y = j+0.5f;
  float z = k+0.5f;

  int4 pos = (int4){i, j, k,0};

  float x2 = x + (float)(READ_vectorX_IMAGE(vectorX, sampler, pos).x);
  float y2 = y + (float)(READ_vectorY_IMAGE(vectorY, sampler, pos).x);
  float z2 = z + (float)(READ_vectorZ_IMAGE(vectorZ, sampler, pos).x);


  //int4 coord_norm = (int4)(x2 * GET_IMAGE_WIDTH(input) / GET_IMAGE_WIDTH(output),y2 * GET_IMAGE_HEIGHT(input) / GET_IMAGE_HEIGHT(output), z2  * GET_IMAGE_DEPTH(input) / GET_IMAGE_DEPTH(output),0.f);
  float4 coord_norm = (float4)(x2 / Nx, y2 / Ny, z2 / Nz,0.f);



  float pix = 0;
  if (x2 >= 0 && y2 >= 0 && z2 >= 0 &&
      x2 < GET_IMAGE_WIDTH(src) && y2 < GET_IMAGE_HEIGHT(src) && z2 < GET_IMAGE_DEPTH(src)
  ) {
    pix = (float)(READ_src_IMAGE(src, sampler, coord_norm).x);
  }

  WRITE_dst_IMAGE(dst, pos, CONVERT_dst_PIXEL_TYPE(pix));
}
