// find neighbours in deskewed image and then applyy inverse deskew to find neighbours in raw data
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



#ifndef SAMPLER_ADDRESS
#define SAMPLER_ADDRESS CLK_ADDRESS_CLAMP
#endif

__kernel void affine_transform_3d_interpolate_linear(
    IMAGE_input_TYPE input,
	IMAGE_output_TYPE output,
	IMAGE_mat_TYPE mat,
  IMAGE_yz1_mat_TYPE yz1_mat,
  IMAGE_yz2_mat_TYPE yz2_mat,
  IMAGE_yz3_mat_TYPE yz3_mat,
  IMAGE_yz4_mat_TYPE yz4_mat)
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

  float pix = 0;

  if (x >= 0 && y >= 0 && z >= 0 &&
      x < Nx && y < Ny && z < Nz) 
  {
    

    //get nearest neighbours in the shear plane
    //apply translation to coordinates on shear plane
    
    float z1_deskew = (yz1_mat[8]*x2+yz1_mat[9]*y2+yz1_mat[10]*z2+yz1_mat[11]);
    float y1_deskew = (yz1_mat[4]*x2+yz1_mat[5]*y2+yz1_mat[6]*z2+yz1_mat[7]);
    float x1_deskew = (yz1_mat[0]*x2+yz1_mat[1]*y2+yz1_mat[2]*z2+yz1_mat[3]);

    float z2_deskew = (yz2_mat[8]*x2+yz2_mat[9]*y2+yz2_mat[10]*z2+yz2_mat[11]);
    float y2_deskew = (yz2_mat[4]*x2+yz2_mat[5]*y2+yz2_mat[6]*z2+yz2_mat[7]);
    float x2_deskew = (yz2_mat[0]*x2+yz2_mat[1]*y2+yz2_mat[2]*z2+yz2_mat[3]);

    float z3_deskew = (yz3_mat[8]*x2+yz3_mat[9]*y2+yz3_mat[10]*z2+yz3_mat[11]);
    float y3_deskew = (yz3_mat[4]*x2+yz3_mat[5]*y2+yz3_mat[6]*z2+yz3_mat[7]);
    float x3_deskew = (yz3_mat[0]*x2+yz3_mat[1]*y2+yz3_mat[2]*z2+yz3_mat[3]);

    float z4_deskew = (yz4_mat[8]*x2+yz4_mat[9]*y2+yz4_mat[10]*z2+yz4_mat[11]);
    float y4_deskew = (yz4_mat[4]*x2+yz4_mat[5]*y2+yz4_mat[6]*z2+yz4_mat[7]);
    float x4_deskew = (yz4_mat[0]*x2+yz4_mat[1]*y2+yz4_mat[2]*z2+yz4_mat[3]);
    
    //apply inverse shear to get corresponding neighbouring coordinates on raw data
    float z1_raw = (mat[8]*x1_deskew+mat[9]*y1_deskew+mat[10]*z1_deskew+mat[11]);
    float y1_raw = (mat[4]*x1_deskew+mat[5]*y1_deskew+mat[6]*z1_deskew+mat[7]);
    float x1_raw = (mat[0]*x1_deskew+mat[1]*y1_deskew+mat[2]*z1_deskew+mat[3]);

    float z2_raw = (mat[8]*x2_deskew+mat[9]*y2_deskew+mat[10]*z2_deskew+mat[11]);
    float y2_raw = (mat[4]*x2_deskew+mat[5]*y2_deskew+mat[6]*z2_deskew+mat[7]);
    float x2_raw = (mat[0]*x2_deskew+mat[1]*y2_deskew+mat[2]*z2_deskew+mat[3]);

    float z3_raw = (mat[8]*x3_deskew+mat[9]*y3_deskew+mat[10]*z3_deskew+mat[11]);
    float y3_raw = (mat[4]*x3_deskew+mat[5]*y3_deskew+mat[6]*z3_deskew+mat[7]);
    float x3_raw = (mat[0]*x3_deskew+mat[1]*y3_deskew+mat[2]*z3_deskew+mat[3]);

    float z4_raw = (mat[8]*x4_deskew+mat[9]*y4_deskew+mat[10]*z4_deskew+mat[11]);
    float y4_raw = (mat[4]*x4_deskew+mat[5]*y4_deskew+mat[6]*z4_deskew+mat[7]);
    float x4_raw = (mat[0]*x4_deskew+mat[1]*y4_deskew+mat[2]*z4_deskew+mat[3]);

    //get pixel values at each coordinate
    float yz1 = (float)(READ_input_IMAGE(input, sampler, (int4)(x2, y1_raw, z1_raw, 0)).x);
    float yz2 = (float)(READ_input_IMAGE(input, sampler, (int4)(x2, y2_raw, z2_raw, 0)).x);

    //get pixel values at nearest neighbours on raw data space 
    float yz3 = (float)(READ_input_IMAGE(input, sampler, (int4)(x2, y3_raw, z3_raw, 0)).x);
    float yz4 = (float)(READ_input_IMAGE(input, sampler, (int4)(x2, y4_raw, z4_raw, 0)).x);
  

    //bi?/linear interpolation
    //interpolate between z and diagonally across planes
    float f1 = ((z4_raw- z)* yz2 +(z-z2_raw)*yz4)/((z4_raw - z2_raw));
    float f2 = ((z3_raw- z)* yz1 +(z-z1_raw)*yz3)/((z3_raw - z1_raw));

    pix = f1 + f2;
    
  }


  int4 pos = (int4){i, j, k,0};

  WRITE_output_IMAGE(output, pos, CONVERT_output_PIXEL_TYPE(pix));


}