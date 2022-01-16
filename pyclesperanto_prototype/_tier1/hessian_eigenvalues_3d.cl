#define PRECISION ldexp(1.0f, -22)

// Returns 1 / sqrt(value)
inline double precise_rsqrt(double value) {
    // The opencl function rsqrt, might not give precise results.
    // This function uses the Newton method to improve the results precision.
    double x2 = value * 0.5;
    double y = rsqrt(value);
    y = y * ( 1.5 - ( x2 * y * y ) );   // Newton
    y = y * ( 1.5 - ( x2 * y * y ) );   // Newton
    y = y * ( 1.5 - ( x2 * y * y ) );   // Newton
    y = y * ( 1.5 - ( x2 * y * y ) );   // Newton
    y = y * ( 1.5 - ( x2 * y * y ) );   // Newton
    return y;
}

// Return the square root of value.
// This method has higher precision than opencl's sqrt() method.
inline double precise_sqrt(double value) {
    return value * precise_rsqrt(value);
}

inline void swap(double x[], int a, int b) {
    double tmp = x[a];
    x[a] = x[b];
    x[b] = tmp;
}

// Calculates the two solutions of the equation: x^2 + c1 * x + c0 == 0
// The results are written to x[], smaller value first.
inline void solve_quadratic_equation(double c0, double c1, double x[]) {
    double p = 0.5 * c1;
    double dis = p * p - c0;
    dis = (dis > 0) ? precise_sqrt(dis) : 0;
    x[0] = (-p - dis);
    x[1] = (-p + dis);
}

// One iteration of Halleys method applied to the depressed cubic equation:
//  x^3 + b1 * x + b0 == 0
inline double halleys_method(double b0, double b1, double x) {
    double dy = 3 * x * x + b1;
    double y = (x * x + b1) * x + b0;	/* ...looks odd, but saves CPU time */
    double dx = y * dy / (dy * dy - 3 * y * x);
    return dx;
}

// Returns one solution to the depressed cubic equation:
//  x^3 + b1 * x + b0 == 0
inline double find_root(double b0, double b1) {
    if(b0 == 0)
        return 0;
    double w = max(fabs(b0), fabs(b1)) + 1.0; /* radius of root circle */
    double h = (b0 > 0.0) ? -w : w;
    double dx;
    do {					/* find 1st root by Halley's method */
        dx = halleys_method(b0, b1, h);
        h -= dx;
    } while (fabs(dx) > fabs(PRECISION * w));
    return h;
}

// Returns all three real solutions of the depressed cubic equation:
//  x^3 + b1 * x + b0 == 0
// The solutions are written to x[]. Smallest solution first.
inline void solve_cubic_scaled_equation(double b0, double b1, double x[]) {
    double h = find_root(b0, b1);
    x[2] = h;
    double c1 = h;			/* deflation; c2 is 1 */
    double c0 = c1 * h + b1;
    solve_quadratic_equation(c0, c1, x);
    if (x[1] > x[2]) {			/* sort results */
        swap(x, 1, 2);
        if (x[0] > x[1]) swap(x, 0, 1);
    }
}

inline int exponent_of(double f) {
    int exponent;
    frexp(f, &exponent);
    return exponent;
}

// Returns all three real solutions of the depressed cubic equation:
//  x^3 + b1 * x + b0 == 0
// The solutions are written to x[]. Smallest solution first.
inline void solve_depressed_cubic_equation(double b0, double b1, double x[]) {
    int e0 = exponent_of(b0) / 3;
    int e1 = exponent_of(b1) / 2;
    int e = - max(e0, e1);
    double scaleFactor = ldexp(1.0, -e);
    b1 = ldexp(b1, 2*e);
    b0 = ldexp(b0, 3*e);
    solve_cubic_scaled_equation(b0, b1, x);
    x[0] *= scaleFactor;
    x[1] *= scaleFactor;
    x[2] *= scaleFactor;
}

// Returns all three real solutions of the cubic equation:
//  x^3 + b2 * x^2 + b1 * x + b0 == 0
// The solutions are written to x[]. Smallest solution first.
inline void solve_cubic_equation(double b0, double b1, double b2, double x[]) {
    double s = 1.0 / 3.0 * b2;
    double q = (2. * s * s - b1) * s + b0;
    double p = b1 - b2 * s;
    solve_depressed_cubic_equation(q, p, x);
    x[0] = x[0] - s;
    x[1] = x[1] - s;
    x[2] = x[2] - s;
}

#define PIXEL(x, y, z) (READ_src_IMAGE(src, sampler,POS_src_INSTANCE((x),(y),(z),0)).x)
#define WRITE_PIXEL(image, x, y, z, value) WRITE_ ## image ## _IMAGE(image,POS_ ## image ## _INSTANCE((x),(y),(z),0), CONVERT_ ## image ## _PIXEL_TYPE(value))

/*
  This kernel computes the eigenvalues of the hessian matrix of a 3d image.

  Hessian matrix:
    [Ixx, Ixy, Ixz]
    [Ixy, Iyy, Iyz]
    [Ixz, Iyz, Izz]
  Where Ixx denotes the second derivative in x.

  Ixx and Iyy are calculated by convolving the image with the 1d kernel [1 -2 1].
  Ixy is calculated by a convolution with the 2d kernel:
    [ 0.25 0 -0.25]
    [    0 0     0]
    [-0.25 0  0.25]
*/
__kernel void hessian_eigenvalues_3d(
        IMAGE_src_TYPE src,
        IMAGE_small_eigenvalue_TYPE small_eigenvalue,
        IMAGE_middle_eigenvalue_TYPE middle_eigenvalue,
        IMAGE_large_eigenvalue_TYPE large_eigenvalue
) {
  const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

  const int x = get_global_id(0);
  const int y = get_global_id(1);
  const int z = get_global_id(2);

  float aab = PIXEL(x - 1, y - 1, z);
  float aba = PIXEL(x - 1, y, z - 1);
  float abb = PIXEL(x - 1, y, z);
  float abc = PIXEL(x - 1, y, z + 1);
  float acb = PIXEL(x - 1, y + 1, z);
  float baa = PIXEL(x, y - 1, z - 1);
  float bab = PIXEL(x, y - 1, z);
  float bac = PIXEL(x, y - 1, z + 1);
  float bba = PIXEL(x, y, z - 1);
  float bbb = PIXEL(x, y, z);
  float bbc = PIXEL(x, y, z + 1);
  float bca = PIXEL(x, y + 1, z - 1);
  float bcb = PIXEL(x, y + 1, z);
  float bcc = PIXEL(x, y + 1, z + 1);
  float cab = PIXEL(x + 1, y - 1, z);
  float cba = PIXEL(x + 1, y, z - 1);
  float cbb = PIXEL(x + 1, y, z);
  float cbc = PIXEL(x + 1, y, z + 1);
  float ccb = PIXEL(x + 1, y + 1, z);
  double g_xx = abb - 2 * bbb + cbb;
  double g_yy = bab - 2 * bbb + bcb;
  double g_zz = bba - 2 * bbb + bbc;
  double g_xy = (aab + ccb - acb - cab) * 0.25;
  double g_xz = (aba + cbc - abc - cba) * 0.25;
  double g_yz = (baa + bcc - bac - bca) * 0.25;
  double a = -(g_xx + g_yy + g_zz);
  double b = g_xx * g_yy + g_xx * g_zz + g_yy * g_zz - g_xy * g_xy - g_xz * g_xz - g_yz * g_yz;
  double c = g_xx * (g_yz * g_yz - g_yy * g_zz) + g_yy * g_xz * g_xz + g_zz * g_xy * g_xy - 2 * g_xy * g_xz * g_yz;
  double eigenvalues[3];
  solve_cubic_equation(c, b, a, eigenvalues);
  WRITE_PIXEL(small_eigenvalue, x, y, z, eigenvalues[0]);
  WRITE_PIXEL(middle_eigenvalue, x, y, z, eigenvalues[1]);
  WRITE_PIXEL(large_eigenvalue, x, y, z, eigenvalues[2]);
}
