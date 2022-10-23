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

__kernel void affine_transform_3d_interpolate_bilinear(
    IMAGE_input_TYPE input,
	IMAGE_output_TYPE output,
	IMAGE_mat_TYPE mat,
  IMAGE_shear_mat_TYPE shear_mat,
  IMAGE_shear_mat_inv_TYPE shear_mat_inv,
  IMAGE_orth_mat_yz1_TYPE orth_mat_yz1,
  IMAGE_orth_mat_yz2_TYPE orth_mat_yz2,
  IMAGE_nearest_mat_yz3_TYPE nearest_mat_yz3,
  IMAGE_nearest_mat_yz4_TYPE nearest_mat_yz4)
{

  const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE|
      SAMPLER_ADDRESS;// 


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

  //get shear coordinates
  float z_shear = (shear_mat[8]*x+shear_mat[9]*y+shear_mat[10]*z+shear_mat[11]);
  float y_shear = (shear_mat[4]*x+shear_mat[5]*y+shear_mat[6]*z+shear_mat[7]);
  float x_shear = (shear_mat[0]*x+shear_mat[1]*y+shear_mat[2]*z+shear_mat[3]);

  float pix = 0;

  if (x >= 0 && y >= 0 && z >= 0 &&
      x < GET_IMAGE_WIDTH(input) && y < GET_IMAGE_HEIGHT(input) && z < GET_IMAGE_DEPTH(input)
  ) {
    


    //get yz neighbours coordinates in deskew space; (orthogonal in deskewed space)
    float z1_orth_deskew  = (orth_mat_yz1[8]*x2+orth_mat_yz1[9]*y2+orth_mat_yz1[10]*z2+orth_mat_yz1[11]);
    float y1_orth_deskew = (orth_mat_yz1[4]*x2+orth_mat_yz1[5]*y2+orth_mat_yz1[6]*z2+orth_mat_yz1[7]);
    float x1_orth_deskew  = (orth_mat_yz1[0]*x2+orth_mat_yz1[1]*y2+orth_mat_yz1[2]*z2+orth_mat_yz1[3]);

    float z2_orth_deskew  = (orth_mat_yz2[8]*x2+orth_mat_yz2[9]*y2+orth_mat_yz2[10]*z2+orth_mat_yz2[11]);
    float y2_orth_deskew = (orth_mat_yz2[4]*x2+orth_mat_yz2[5]*y2+orth_mat_yz2[6]*z2+orth_mat_yz2[7]);
    float x2_orth_deskew  = (orth_mat_yz2[0]*x2+orth_mat_yz2[1]*y2+orth_mat_yz2[2]*z2+orth_mat_yz2[3]);

  
    //apply deskew inverse matrix to get the corresponding orthogonal coordinates in raw data
    float z1_orth = (mat[8]*x1_orth_deskew+mat[9]*y1_orth_deskew+mat[10]*z1_orth_deskew+mat[11]);
    float y1_orth = (mat[4]*x1_orth_deskew+mat[5]*y1_orth_deskew+mat[6]*z1_orth_deskew+mat[7]);
    float x1_orth = (mat[0]*x1_orth_deskew+mat[1]*y1_orth_deskew+mat[2]*z1_orth_deskew+mat[3]);

    float z2_orth = (mat[8]*x2_orth_deskew+mat[9]*y2_orth_deskew+mat[10]*z2_orth_deskew+mat[11]);
    float y2_orth = (mat[4]*x2_orth_deskew+mat[5]*y2_orth_deskew+mat[6]*z2_orth_deskew+mat[7]);
    float x2_orth = (mat[0]*x2_orth_deskew+mat[1]*y2_orth_deskew+mat[2]*z2_orth_deskew+mat[3]);


    //get nearest neighbours in the shear plane
    //apply translation to coordinates on shear plane
    
    float z3_nearest_shear = (nearest_mat_yz3[8]*x_shear+nearest_mat_yz3[9]*y_shear+nearest_mat_yz3[10]*z_shear+nearest_mat_yz3[11]);
    float y3_nearest_shear = (nearest_mat_yz3[4]*x_shear+nearest_mat_yz3[5]*y_shear+nearest_mat_yz3[6]*z_shear+nearest_mat_yz3[7]);
    float x3_nearest_shear = (nearest_mat_yz3[0]*x_shear+nearest_mat_yz3[1]*y_shear+nearest_mat_yz3[2]*z_shear+nearest_mat_yz3[3]);

    float z4_nearest_shear = (nearest_mat_yz4[8]*x_shear+nearest_mat_yz4[9]*y_shear+nearest_mat_yz4[10]*z_shear+nearest_mat_yz4[11]);
    float y4_nearest_shear = (nearest_mat_yz4[4]*x_shear+nearest_mat_yz4[5]*y_shear+nearest_mat_yz4[6]*z_shear+nearest_mat_yz4[7]);
    float x4_nearest_shear = (nearest_mat_yz4[0]*x_shear+nearest_mat_yz4[1]*y_shear+nearest_mat_yz4[2]*z_shear+nearest_mat_yz4[3]);

    //find corresponding coordinates from shear in raw plane

    float z3_nearest = (shear_mat_inv[8]*x3_nearest_shear+shear_mat_inv[9]*y3_nearest_shear+shear_mat_inv[10]*z3_nearest_shear+nearest_mat_yz3[11]);
    float y3_nearest = (shear_mat_inv[4]*x3_nearest_shear+shear_mat_inv[5]*y3_nearest_shear+shear_mat_inv[6]*z3_nearest_shear+nearest_mat_yz3[7]);
    float x3_nearest = (shear_mat_inv[0]*x3_nearest_shear+shear_mat_inv[1]*y3_nearest_shear+shear_mat_inv[2]*z3_nearest_shear+nearest_mat_yz3[3]);

    float z4_nearest = (shear_mat_inv[8]*x4_nearest_shear+shear_mat_inv[9]*y4_nearest_shear+shear_mat_inv[10]*z4_nearest_shear+nearest_mat_yz4[11]);
    float y4_nearest = (shear_mat_inv[4]*x4_nearest_shear+shear_mat_inv[5]*y4_nearest_shear+shear_mat_inv[6]*z4_nearest_shear+nearest_mat_yz4[7]);
    float x4_nearest = (shear_mat_inv[0]*x4_nearest_shear+shear_mat_inv[1]*y4_nearest_shear+shear_mat_inv[2]*z4_nearest_shear+nearest_mat_yz4[3]);


    //apply inverse shear to get nearest coordinates on raw data

    //get pixel values at orthogonal coord
    float orth_1 = (READ_input_IMAGE(input, sampler, (float4)(x, y1_orth, z1_orth, 0.f)).x);
    float orth_2 = (READ_input_IMAGE(input, sampler, (float4)(x, y2_orth, z2_orth, 0.f)).x);

    //get pixel values at nearest neighbours on raw data space 
    float nearest_1 = (READ_input_IMAGE(input, sampler, (float4)(x, y3_nearest, z3_nearest, 0.f)).x);
    float nearest_2 = (READ_input_IMAGE(input, sampler, (float4)(x, y4_nearest, z4_nearest, 0.f)).x);
  

    //bilinear interpolation
    float f1 = ((z2_orth - z)* orth_1 + (z - z1_orth)* orth_2)/(z2_orth - z1_orth);
    float f2 = ((z4_nearest - z)* nearest_1 + (z - z3_nearest)* nearest_2)/(z4_nearest - z3_nearest);
    
    pix = f1;
    
    //linear interpolation along z and y axes
    //float f1 = ((z3_n - z)* left + (z - z1_n)* right)/(z3_n - z1_n);
    //float f2 = ((y4_n - y)* top + (y - y2_n)* bottom)/(y4_n - y2_n);
    //pix = f1+f2;//f1+f2;


  }


  int4 pos = (int4){i, j, k,0};

  WRITE_output_IMAGE(output, pos, CONVERT_output_PIXEL_TYPE(pix));


}