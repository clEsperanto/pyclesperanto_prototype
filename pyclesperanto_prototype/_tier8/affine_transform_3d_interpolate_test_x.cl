// adapted from: https://github.com/maweigert/gputools/blob/master/gputools/transforms/kernels/transformations.cl
//
// Copyright (c) 2016, Martin Weigert
// All rights reserved.
//
// Redistribution and use in source and binary forms, with or without
// modification, are permitted provided that the following conditions are met:
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
// IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
// DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
// FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
// DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
// SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
// CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
// OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
// OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.



#ifndef SAMPLER_FILTER
#define SAMPLER_FILTER CLK_FILTER_LINEAR
#endif

#ifndef SAMPLER_ADDRESS
#define SAMPLER_ADDRESS CLK_ADDRESS_CLAMP
#endif

__kernel void affine_transform_3d_interpolate_test(
    IMAGE_input_TYPE input,
	IMAGE_output_TYPE output,
	IMAGE_mat_TYPE mat,
  IMAGE_trans_rotate_mat_TYPE trans_rotate_mat,
  IMAGE_shear_mat_TYPE shear_mat,
  IMAGE_shear_mat_inv_TYPE shear_mat_inv,
  IMAGE_translate_x_mat_TYPE translate_x_mat,
  IMAGE_translate_y_mat_TYPE translate_y_mat,
  IMAGE_translate_z_mat_TYPE translate_z_mat)
{

  const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE|
      SAMPLER_ADDRESS |	SAMPLER_FILTER;

  //dataset ussually divided into N parts, each work item processes on part.
  //get_global_id will get the global ID that 
  uint i = get_global_id(0);
  uint j = get_global_id(1);
  uint k = get_global_id(2);

  //get the size of the image or total number of work-items
  uint Nx = get_global_size(0);
  uint Ny = get_global_size(1);
  uint Nz = get_global_size(2);

  //float x = (mat[0]*i+mat[1]*j+mat[2]*k+mat[3]);
  //float y = (mat[4]*i+mat[5]*j+mat[6]*k+mat[7]);
  //float z = (mat[8]*i+mat[9]*j+mat[10]*k+mat[11]);
  ////ensure correct sampling, see opencl 1.2 specification pg. 329
  //x += 0.5f;
  //y += 0.5f;
  //z += 0.5f;

  //virtual plane coordinates
  float x2 = i+0.5f;
  float y2 = j+0.5f;
  float z2 = k+0.5f;

  //coordinates on raw data that will be transformed
  float z = (mat[8]*x2+mat[9]*y2+mat[10]*z2+mat[11]);
  float y = (mat[4]*x2+mat[5]*y2+mat[6]*z2+mat[7]);
  float x = (mat[0]*x2+mat[1]*y2+mat[2]*z2+mat[3]);

  //coordinates on intermediate image, apply the translate_rotate matrix transform to get sheared image coordinates
  //use this to get neighbours
  float zi = (shear_mat_inv[8]*x2+shear_mat_inv[9]*y2+shear_mat_inv[10]*z2+shear_mat_inv[11]);
  float yi = (shear_mat_inv[4]*x2+shear_mat_inv[5]*y2+shear_mat_inv[6]*z2+shear_mat_inv[7]);
  float xi = (shear_mat_inv[0]*x2+shear_mat_inv[1]*y2+shear_mat_inv[2]*z2+shear_mat_inv[3]);

  //int4 coord_norm = (int4)(x2 * GET_IMAGE_WIDTH(input) / GET_IMAGE_WIDTH(output),y2 * GET_IMAGE_HEIGHT(input) / GET_IMAGE_HEIGHT(output), z2  * GET_IMAGE_DEPTH(input) / GET_IMAGE_DEPTH(output),0.f);
  int4 coord_norm = (int4)(x,y, z,0.f);

 

  float pix = 0;

  if (x >= 0 && y >= 0 && z >= 0 &&
      x < GET_IMAGE_WIDTH(input) && y < GET_IMAGE_HEIGHT(input) && z < GET_IMAGE_DEPTH(input)
  ) {
    


    //get neighbouring pixels 
    float z_before = (translate_z_mat[8]*xi+translate_z_mat[9]*yi+translate_z_mat[10]*zi-translate_z_mat[11]);
    float z_after = (translate_z_mat[8]*xi+translate_z_mat[9]*yi+translate_z_mat[10]*zi+translate_z_mat[11]);

    float y_before = (translate_y_mat[4]*xi+translate_y_mat[5]*yi+translate_y_mat[6]*zi-translate_y_mat[7]);
    float y_after =  (translate_y_mat[4]*xi+translate_y_mat[5]*yi+translate_y_mat[6]*zi+translate_y_mat[7]);

    float x_before = (translate_x_mat[0]*xi+translate_x_mat[1]*yi+translate_x_mat[2]*zi-translate_x_mat[3]);
    float x_after = (translate_x_mat[0]*xi+translate_x_mat[1]*yi+translate_x_mat[2]*zi+translate_x_mat[3]);
    
    //apply shear transform from shear to original image to get values at neighbour coordinates
    z_before = (shear_mat[8]*x_before+shear_mat[9]*y_before+shear_mat[10]*z_before+shear_mat[11]);
    y_before = (shear_mat[4]*x_before+shear_mat[5]*y_before+shear_mat[6]*z_before+shear_mat[7]);
    x_before = (shear_mat[0]*x_before+shear_mat[1]*y_before+shear_mat[2]*z_before+shear_mat[3]);

    z_after = (shear_mat[8]*x_after+shear_mat[9]*y_after+shear_mat[10]*z_after+shear_mat[11]);
    y_after = (shear_mat[4]*x_after+shear_mat[5]*y_after+shear_mat[6]*z_after+shear_mat[7]);
    x_after = (shear_mat[0]*x_after+shear_mat[1]*y_after+shear_mat[2]*z_after+shear_mat[3]);

    
    float pix_1 = (float)(READ_input_IMAGE(input, sampler, POS_input_INSTANCE(x_before, y_before, z_before, 0)).x);
    float pix_2 = (float)(READ_input_IMAGE(input, sampler, POS_input_INSTANCE(x_after, y_before, z_before, 0)).x);
    
    float pix_3 = (float)(READ_input_IMAGE(input, sampler, POS_input_INSTANCE(x_before, y_after, z_before, 0)).x);
    float pix_4 = (float)(READ_input_IMAGE(input, sampler, POS_input_INSTANCE(x_after, y_after, z_before, 0)).x);

    //value at coordinate in raw image
    //pix = (float)(READ_input_IMAGE(input, sampler, POS_input_INSTANCE(x, y, z, 0)).x);

    //interpolate x direction
    float f1 = ((x_after - x)* pix_1/(x_after - x_before)) + ((x - x_before)* pix_2/(x_after - x_before));
    float f2 = ((x_after - x)* pix_3/(x_after - x_before)) + ((x - x_before)* pix_4/(x_after - x_before));

    //pix = f1+f2;//((z_after - y)* f1/(z_after - z_before)) + ((y - z_before)* f2/(z_after - z_before));
    pix = (float)(READ_input_IMAGE(input, sampler, POS_input_INSTANCE(x_after, y_after, z_after, 0)).x);

  }


  int4 pos = (int4){i, j, k,0};

  WRITE_output_IMAGE(output, POS_output_INSTANCE(i, j, k, 0), CONVERT_output_PIXEL_TYPE(pix));


}