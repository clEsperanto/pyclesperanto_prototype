__constant sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

__kernel void sobel_3d
(
  IMAGE_dst_TYPE dst,
  IMAGE_src_TYPE src
)
{

  /*need 3 operations with 3 kernels for 3d sobel*/
  const int x = get_global_id(0);
  const int y = get_global_id(1);
  const int z = get_global_id(2);

  const int4 pos = (int4){x,y,z,0};

  int gy[3][3][3];
  int gx[3][3][3];
  int gz[3][3][3];
  
  int hx[3]={1,2,1};
  int hy[3]={1,2,1};
  int hz[3]={1,2,1};

  int hpx[3]={1,0,-1};
  int hpy[3]={1,0,-1};
  int hpz[3]={1,0,-1};

  float sum_x,sum_y,sum_z;
  int m,n,k;

  /*build the kernels i.e. h'_x(x,y,z)=h'(x)h(y)h(z)=gx(x,y,z)*/
  for(m=0;m<=2;m++) {
    for(n=0;n<=2;n++) {
      for(k=0;k<=2;k++){
  	    gx[m][n][k] = hpx[m] * hy[n]  * hz[k];
  	    gy[m][n][k] = hx[m]  * hpy[n] * hz[k];
  	    gz[m][n][k] = hx[m]  * hy[n]  * hpz[k];
      }
    }
  }

    sum_x=0,sum_y=0,sum_z=0;
    for(m=0;m<=2;m++){
        for(n=0;n<=2;n++){
            for(k=0;k<=3;k++){
                sum_x += gx[m][n][k]*(READ_src_IMAGE(src, sampler, (pos + (int4){m-1, n-1,k-1, 0})).x);
                sum_y += gy[m][n][k]*(READ_src_IMAGE(src, sampler, (pos + (int4){m-1, n-1,k-1, 0})).x);
                sum_z += gz[m][n][k]*(READ_src_IMAGE(src, sampler, (pos + (int4){m-1, n-1,k-1, 0})).x);
            }
        }
    }

	float result = sqrt(sum_x * sum_x + sum_y * sum_y + sum_z * sum_z);

    WRITE_dst_IMAGE (dst, pos, CONVERT_dst_PIXEL_TYPE(result));
}
