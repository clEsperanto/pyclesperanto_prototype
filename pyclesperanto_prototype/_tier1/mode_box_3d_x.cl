__constant sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

__kernel void mode_box_3d
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

  long histogram[256];
  for (int i = 0; i < 256; i++){
    histogram[i]=0;
  }


  const int4   e = (int4)  { (Nx-1)/2, (Ny-1)/2, (Nz-1)/2, 0 };

  for (int x = -e.x; x <= e.x; x++) {
    for (int y = -e.y; y <= e.y; y++) {
      for (int z = -e.z; z <= e.z; z++) {
        int x1 = coord.x + x;
        int x2 = coord.y + y;
        int x3 = coord.z + z;
        const int4 pos = (int4){x1,x2,x3,0};
        int value_res = (int)READ_src_IMAGE(src,sampler,pos).x;
        histogram[value_res]++;
      }
    }
  }


  long max_value = 0;
  int max_pos = 0;
  for (int i = 0; i < 256; i++){
    if (max_value < histogram[i]){
      max_value = histogram[i];
      max_pos = i;
    }
  }

  WRITE_dst_IMAGE(dst, coord, CONVERT_dst_PIXEL_TYPE(max_pos));
}

