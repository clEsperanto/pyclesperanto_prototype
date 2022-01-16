
#define PIXEL(x, y) (READ_src_IMAGE(src, sampler,POS_src_INSTANCE((x),(y),0,0)).x)
#define WRITE_PIXEL(image, x, y, value) WRITE_ ## image ## _IMAGE(image,POS_ ## image ## _INSTANCE((x),(y),0,0), CONVERT_ ## image ## _PIXEL_TYPE(value))

/*
  This kernel computes the eigenvalues of the hessian matrix of a 2d image.

  Hessian matrix:
    [Ixx, Ixy]
    [Ixy, Iyy]
  Where Ixx denotes the second derivative in x.

  Ixx and Iyy are calculated by convolving the image with the 1d kernel [1 -2 1].
  Ixy is calculated by a convolution with the 2d kernel:
    [ 0.25 0 -0.25]
    [    0 0     0]
    [-0.25 0  0.25]
*/
__kernel void hessian_eigenvalues_2d(
        IMAGE_src_TYPE src,
        IMAGE_small_eigenvalue_TYPE small_eigenvalue,
        IMAGE_large_eigenvalue_TYPE large_eigenvalue
) {
  const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

  const int x = get_global_id(0);
  const int y = get_global_id(1);

  float aa = PIXEL(x - 1, y - 1);
  float ab = PIXEL(x - 1, y);
  float ac = PIXEL(x - 1, y + 1);
  float ba = PIXEL(x, y - 1);
  float bb = PIXEL(x, y);
  float bc = PIXEL(x, y + 1);
  float ca = PIXEL(x + 1, y - 1);
  float cb = PIXEL(x + 1, y);
  float cc = PIXEL(x + 1, y + 1);
  float s_xx = ab - 2 * bb + cb;
  float s_yy = ba - 2 * bb + bc;
  float s_xy = (aa + cc - ac - ca) * 0.25;
  float trace = s_xx + s_yy;
  float l = (float) (trace / 2.0 + sqrt(4 * s_xy * s_xy + (s_xx - s_yy) * (s_xx - s_yy)) / 2.0);
  float s = (float) (trace / 2.0 - sqrt(4 * s_xy * s_xy + (s_xx - s_yy) * (s_xx - s_yy)) / 2.0);
  WRITE_PIXEL(small_eigenvalue, x, y, s);
  WRITE_PIXEL(large_eigenvalue, x, y, l);
}
