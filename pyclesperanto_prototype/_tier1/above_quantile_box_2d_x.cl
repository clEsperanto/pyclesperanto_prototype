__constant sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

__kernel void above_quantile_box_2d
(
  IMAGE_dst_TYPE dst,
  IMAGE_src_TYPE src,
  const int Nx,
  const int Ny
)
{
  const int i = get_global_id(0);
  const int j = get_global_id(1);
  const int2 coord = (int2){i,j};
  const int4   e = (int4)  { (Nx-1)/2, (Ny-1)/2, 0, 0 };
  float value = (float)READ_src_IMAGE(src,sampler,coord).x;
  int count_all = 0;
  int count_below = 0;

  for (int x = -e.x; x <= e.x; x++) {
    for (int y = -e.y; y <= e.y; y++) {
      int x1 = coord.x + x;
      int x2 = coord.y + y;

      if (x1 < 0 || x2 < 0|| x1 >= GET_IMAGE_WIDTH(src) || x2 >= GET_IMAGE_HEIGHT(src)) {
        continue;
      }
      if (x1 == i && x2 == j) {
        continue;
      }

      const int2 pos = (int2){x1,x2};

      if (value >= (float)READ_src_IMAGE(src,sampler,pos).x){
        count_below++;
      }
      count_all++;
    }
  }

  WRITE_dst_IMAGE(dst, coord, CONVERT_dst_PIXEL_TYPE((float)count_below * 100.0 / count_all ));
}


