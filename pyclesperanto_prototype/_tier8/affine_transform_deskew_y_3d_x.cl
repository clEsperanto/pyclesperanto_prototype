// OpenCL kernel for orthogonal interpolation for oblique plane microscopy
// images adapted from:
// https://github.com/QI2lab/OPM/blob/master/reconstruction/image_post_processing.py#L34
// and
// https://spiral.imperial.ac.uk/bitstream/10044/1/68022/1/Maioli-V-2016-PhD-Thesis.pdf
// and
// Sapoznik et al. (2020) A versatile oblique plane microscope for
// large-scale and high-resolution imaging of subcellular dynamics eLife
// 9:e57681. https://doi.org/10.7554/eLife.57681
//
// Redistribution and use in
// source and binary forms, with or without modification, are permitted provided
// that the following conditions are met:
//
// * Redistributions of source code must retain the above copyright notice, this
//   list of conditions and the following disclaimer.
//
// * Redistributions in binary form must reproduce the above copyright notice,
//   this list of conditions and the following disclaimer in the documentation
//   and/or other materials provided with the distribution.
//
// * Neither the name of gputools nor the names of its
//   contributors may be used to endorse or promote products derived from
//   this software without specific prior written permission.
//
// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
// AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
// IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
// ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
// LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
// CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
// SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
// INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
// CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
// ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
// POSSIBILITY OF SUCH DAMAGE.

#ifndef SAMPLER_ADDRESS
#define SAMPLER_ADDRESS CLK_ADDRESS_CLAMP
#endif

__kernel void
affine_transform_deskew_y_3d(IMAGE_input_TYPE input, IMAGE_output_TYPE output,
                             IMAGE_mat_TYPE mat,
                             const int deskewed_Nx, const int deskewed_Ny,
                             const int deskewed_Nz, float pixel_step,
                             float tantheta, float costheta, float sintheta) {

  const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | SAMPLER_ADDRESS;

  // get id for each pixel
  uint x = get_global_id(0);
  uint y = get_global_id(1);
  uint z = get_global_id(2);

  // get the size of the image or total number of work-items
  uint Nx = GET_IMAGE_WIDTH(input);  // get_global_size(0);
  uint Ny = GET_IMAGE_HEIGHT(input); // get_global_size(1);
  uint Nz = GET_IMAGE_DEPTH(input);  // get_global_size(2);

  // virtual plane coordinates, deskewed coord
  //uint x = i;
  //uint y = j;
  //uint z = k;

  // corresponding coordinates on raw data
  uint z_orig = (mat[8] * x + mat[9] * y + mat[10] * z + mat[11]);
  uint y_orig = (mat[4] * x + mat[5] * y + mat[6] * z + mat[7]);
  uint x_orig = (mat[0] * x + mat[1] * y + mat[2] * z + mat[3]);

   float pix = 0;
   
  // ensure within bounds of final image/deskewed image

  if (x >= 0 && y >= 0 && z >= 0 && x < deskewed_Nx && y < deskewed_Ny &&
      z < deskewed_Nz) {
    //printf("%d\n,%d\n,%d\n", z,y,x);
    float virtual_plane = (y - z / tantheta);
    // get plane before
    long plane_before = floor(virtual_plane / pixel_step);
    // get plane after
    long plane_after = plane_before + 1;

    if (plane_before >= 0 && plane_after < Nz) {
      float l_before = virtual_plane - (plane_before * pixel_step);
      float l_after = pixel_step - l_before;

      float za = z / sintheta;
      float virtual_pos_before = za + (l_before * costheta);
      float virtual_pos_after = za - (l_after * costheta);

      // determine nearest data points to interpoloated point in raw data
      long pos_before = floor(virtual_pos_before);
      long pos_after = floor(virtual_pos_after);

      if (pos_before >= 0 && pos_after >= 0 && pos_before < Ny - 1 &&
          pos_after < Ny - 1) {
        float dz_before = virtual_pos_before - pos_before;
        float dz_after = virtual_pos_after - pos_after;

        long y_after = (pos_after + 1);
        long y_after1 = (pos_after);

        // translate by 1
        long y_before = (pos_before + 1);
        long y_before1 = (pos_before);

        // get pixel values at neighbour coordinates
        float pix_1 =
            (float)(READ_input_IMAGE(input, sampler,
                                     (int4)(x, y_after, plane_after, 0))
                        .x);
        float pix_2 =
            (float)(READ_input_IMAGE(input, sampler,
                                     (int4)(x, y_after1, plane_after, 0))
                        .x);

        float pix_3 =
            (float)(READ_input_IMAGE(input, sampler,
                                     (int4)(x, y_before, plane_before, 0))
                        .x);
        float pix_4 =
            (float)(READ_input_IMAGE(input, sampler,
                                     (int4)(x, y_before1, plane_before, 0))
                        .x);

        pix = ((l_before * dz_after * pix_1) +
               (l_before * (1 - dz_after) * pix_2) +
               (l_after * dz_before * pix_3) +
               (l_after * (1 - dz_before) * pix_4)) /
              pixel_step;
      }
    }
  }

  // if rotate coverslip, apply flipping on Z axis
  int4 pos = (int4){x, y, z, 0};

  WRITE_output_IMAGE(output, pos, CONVERT_output_PIXEL_TYPE(pix));
}