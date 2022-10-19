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
  IMAGE_shear_mat_TYPE shear_mat,
  IMAGE_shear_mat_inv_TYPE shear_mat_inv,
  IMAGE_translate_mat_yz1_TYPE translate_mat_yz1,
  IMAGE_translate_mat_yz2_TYPE translate_mat_yz2,
  IMAGE_translate_mat_yz3_TYPE translate_mat_yz3,
  IMAGE_translate_mat_yz4_TYPE translate_mat_yz4)
{

  const sampler_t sampler = CLK_NORMALIZED_COORDS_TRUE|
      SAMPLER_ADDRESS|	SAMPLER_FILTER;// 


  //dataset ussually divided into N parts, each work item processes on part.
  //get_global_id will get the global ID that 
  uint i = get_global_id(0);
  uint j = get_global_id(1);
  uint k = get_global_id(2);

  //get the size of the image or total number of work-items
  uint Nx = GET_IMAGE_WIDTH(input);//get_global_size(0);
  uint Ny = GET_IMAGE_HEIGHT(input);//get_global_size(1);
  uint Nz = GET_IMAGE_DEPTH(input);//get_global_size(2);

  //virtual plane coordinates, deskewed coord
  float x2 = i+0.5f;
  float y2 = j+0.5f;
  float z2 = k+0.5f;

  //corresponding coordinates on raw data 
  float z = (mat[8]*x2+mat[9]*y2+mat[10]*z2+mat[11]);
  float y = (mat[4]*x2+mat[5]*y2+mat[6]*z2+mat[7]);
  float x = (mat[0]*x2+mat[1]*y2+mat[2]*z2+mat[3]);

  //coordinates on intermediate sheared image,  multiply coord from raw skewed raw data with shear matrix
  
  float zi = (shear_mat[8]*x+shear_mat[9]*y+shear_mat[10]*z+shear_mat[11]);
  float yi = (shear_mat[4]*x+shear_mat[5]*y+shear_mat[6]*z+shear_mat[7]);
  float xi = (shear_mat[0]*x+shear_mat[1]*y+shear_mat[2]*z+shear_mat[3]);

  //int4 coord_norm = (int4)(x2 * GET_IMAGE_WIDTH(input) / GET_IMAGE_WIDTH(output),y2 * GET_IMAGE_HEIGHT(input) / GET_IMAGE_HEIGHT(output), z2  * GET_IMAGE_DEPTH(input) / GET_IMAGE_DEPTH(output),0.f);
  //int4 coord_norm = (int4)(x,y, z,0.f);

 

  float pix = 0;

  if (x >= 0 && y >= 0 && z >= 0 &&
      x < GET_IMAGE_WIDTH(input) && y < GET_IMAGE_HEIGHT(input) && z < GET_IMAGE_DEPTH(input)
  ) {
    


    //get neighbouring pixels by using a translation matrix for y and z coordinates
    float z1_shear  = (translate_mat_yz1[8]*xi+translate_mat_yz1[9]*yi+translate_mat_yz1[10]*zi+translate_mat_yz1[11]);
    float y1_shear = (translate_mat_yz1[4]*xi+translate_mat_yz1[5]*yi+translate_mat_yz1[6]*zi+translate_mat_yz1[7]);
    float x1_shear  = (translate_mat_yz1[0]*xi+translate_mat_yz1[1]*yi+translate_mat_yz1[2]*zi+translate_mat_yz1[3]);

    float z2_shear  = (translate_mat_yz2[8]*xi+translate_mat_yz2[9]*yi+translate_mat_yz2[10]*zi+translate_mat_yz2[11]);
    float y2_shear = (translate_mat_yz2[4]*xi+translate_mat_yz2[5]*yi+translate_mat_yz2[6]*zi+translate_mat_yz2[7]);
    float x2_shear  = (translate_mat_yz2[0]*xi+translate_mat_yz2[1]*yi+translate_mat_yz2[2]*zi+translate_mat_yz2[3]);

    float z3_shear  = (translate_mat_yz3[8]*xi+translate_mat_yz3[9]*yi+translate_mat_yz3[10]*zi+translate_mat_yz3[11]);
    float y3_shear = (translate_mat_yz3[4]*xi+translate_mat_yz3[5]*yi+translate_mat_yz3[6]*zi+translate_mat_yz3[7]);
    float x3_shear  = (translate_mat_yz3[0]*xi+translate_mat_yz3[1]*yi+translate_mat_yz3[2]*zi+translate_mat_yz3[3]);

    float z4_shear  = (translate_mat_yz4[8]*xi+translate_mat_yz4[9]*yi+translate_mat_yz4[10]*zi+translate_mat_yz4[11]);
    float y4_shear = (translate_mat_yz4[4]*xi+translate_mat_yz4[5]*yi+translate_mat_yz4[6]*zi+translate_mat_yz4[7]);
    float x4_shear  = (translate_mat_yz4[0]*xi+translate_mat_yz4[1]*yi+translate_mat_yz4[2]*zi+translate_mat_yz4[3]);
    
    //apply inverse shear transform to sheared image to obtain original image // get actual neighbour coordinates
    float z1_n = (shear_mat_inv[8]*x1_shear+shear_mat_inv[9]*y1_shear+shear_mat_inv[10]*z1_shear+shear_mat_inv[11]);
    float y1_n = (shear_mat_inv[4]*x1_shear+shear_mat_inv[5]*y1_shear+shear_mat_inv[6]*z1_shear+shear_mat_inv[7]);
    float x1_n = (shear_mat_inv[0]*x1_shear+shear_mat_inv[1]*y1_shear+shear_mat_inv[2]*z1_shear+shear_mat_inv[3]);

    float z2_n = (shear_mat_inv[8]*x2_shear+shear_mat_inv[9]*y2_shear+shear_mat_inv[10]*z2_shear+shear_mat_inv[11]);
    float y2_n = (shear_mat_inv[4]*x2_shear+shear_mat_inv[5]*y2_shear+shear_mat_inv[6]*z2_shear+shear_mat_inv[7]);
    float x2_n = (shear_mat_inv[0]*x2_shear+shear_mat_inv[1]*y2_shear+shear_mat_inv[2]*z2_shear+shear_mat_inv[3]);

    float z3_n = (shear_mat_inv[8]*x3_shear+shear_mat_inv[9]*y3_shear+shear_mat_inv[10]*z3_shear+shear_mat_inv[11]);
    float y3_n = (shear_mat_inv[4]*x3_shear+shear_mat_inv[5]*y3_shear+shear_mat_inv[6]*z3_shear+shear_mat_inv[7]);
    float x3_n = (shear_mat_inv[0]*x3_shear+shear_mat_inv[1]*y3_shear+shear_mat_inv[2]*z3_shear+shear_mat_inv[3]);

    float z4_n = (shear_mat_inv[8]*x4_shear+shear_mat_inv[9]*y4_shear+shear_mat_inv[10]*z4_shear+shear_mat_inv[11]); 
    float y4_n = (shear_mat_inv[4]*x4_shear+shear_mat_inv[5]*y4_shear+shear_mat_inv[6]*z4_shear+shear_mat_inv[7]);
    float x4_n = (shear_mat_inv[0]*x4_shear+shear_mat_inv[1]*y4_shear+shear_mat_inv[2]*z4_shear+shear_mat_inv[3]);

    //get pixel values at neighbour coordinates
    float left = (READ_input_IMAGE(input, sampler, (float4)(x/Nx, y1_n/Ny, z1_n/Nz, 0.f)).x);
    float top = (READ_input_IMAGE(input, sampler, (float4)(x/Nx, y2_n/Ny, z2_n/Nz, 0.f)).x);
    
    float right = (READ_input_IMAGE(input, sampler, (float4)(x/Nx, y3_n/Ny, z3_n/Nz, 0.f)).x);
    float bottom = (READ_input_IMAGE(input, sampler, (float4)(x/Nx, y4_n/Ny, z4_n/Nz, 0.f)).x);


    //Fix calculation here

    //bilinear interpolation
    float f1 = ((z2_n - z)* left + (z - z1_n)* top)/(z2_n - z1_n);
    float f2 = ((z3_n - z)* right + (z - z4_n)* bottom)/(z3_n - z4_n);
    pix = ((y4_n - y)* f1 + (y - y2_n)* f2)/(y4_n - y2_n);
    
    //linear interpolation along z and y axes
    //float f1 = ((z3_n - z)* left + (z - z1_n)* right)/(z3_n - z1_n);
    //float f2 = ((y4_n - y)* top + (y - y2_n)* bottom)/(y4_n - y2_n);
    //pix = f1+f2;//f1+f2;


  }


  int4 pos = (int4){i, j, k,0};

  WRITE_output_IMAGE(output, pos, CONVERT_output_PIXEL_TYPE(pix));


}