__constant sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

__kernel void mean_sphere_3d
(
  IMAGE_dst_TYPE dst,
  IMAGE_src_TYPE src,
  const int Nx,
  const int Ny,
  const int Nz
)
{
  const int i = get_global_id(0);
  const int j = get_global_id(1);
  const int k = get_global_id(2);
  const int4 coord = (int4){i,j,k,0};

  const int4   e = (int4)  {(Nx-1)/2, (Ny-1)/2, (Nz-1)/2, 0 };
  int count = 0;
  float sum = 0;

  float aSquared = e.x * e.x;
  float bSquared = e.y * e.y;
  float cSquared = e.z * e.z;
    if (aSquared == 0) {
        aSquared = FLT_MIN;
    }
    if (bSquared == 0) {
        bSquared = FLT_MIN;
    }
    if (cSquared == 0) {
        cSquared = FLT_MIN;
    }

  for (int x = -e.x; x <= e.x; x++) {
    float xSquared = x * x;
    for (int y = -e.y; y <= e.y; y++) {
      float ySquared = y * y;
      for (int z = -e.z; z <= e.z; z++) {
        float zSquared = z * z;
        if (xSquared / aSquared + ySquared / bSquared + zSquared / cSquared <= 1.0) {

          int x1 = coord.x + x;
          int x2 = coord.y + y;
          int x3 = coord.z + z;
          const int4 pos = (int4){x1,x2,x3,0};
          float value_res = (float)READ_src_IMAGE(src,sampler,pos).x;
          sum = sum + value_res;
          count++;
        }
      }
    }
  }


  IMAGE_dst_PIXEL_TYPE res = CONVERT_dst_PIXEL_TYPE(sum / count);
  WRITE_dst_IMAGE(dst, coord, res);
}
