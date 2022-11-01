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


#ifndef SAMPLER_ADDRESS
#define SAMPLER_ADDRESS CLK_ADDRESS_CLAMP
#endif

__kernel void affine_transform_3d_interpolate_trilinear(
    IMAGE_input_TYPE input,
	  IMAGE_output_TYPE output,
    IMAGE_mat_TYPE mat,
    IMAGE_translate_mat_xyz1_TYPE translate_mat_xyz1,
    IMAGE_translate_mat_xyz2_TYPE translate_mat_xyz2,
    IMAGE_translate_mat_xyz3_TYPE translate_mat_xyz3,
    IMAGE_translate_mat_xyz4_TYPE translate_mat_xyz4,
    IMAGE_translate_mat_xyz5_TYPE translate_mat_xyz5,
    IMAGE_translate_mat_xyz6_TYPE translate_mat_xyz6,
    IMAGE_translate_mat_xyz7_TYPE translate_mat_xyz7,
    IMAGE_translate_mat_xyz8_TYPE translate_mat_xyz8)
{

  const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE|
      SAMPLER_ADDRESS;// |	SAMPLER_FILTER ;//siable interpolation as we are doing it manually


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
    


    //get neighbouring vertices on deskew by using a translation affine transform for x,y and z coordinates
    
    float z_xyz1_deskew  = (translate_mat_xyz1[8]*x2+translate_mat_xyz1[9]*y2+translate_mat_xyz1[10]*z2+translate_mat_xyz1[11]);
    float y_xyz1_deskew = (translate_mat_xyz1[4]*x2+translate_mat_xyz1[5]*y2+translate_mat_xyz1[6]*z2+translate_mat_xyz1[7]);
    float x_xyz1_deskew  = (translate_mat_xyz1[0]*x2+translate_mat_xyz1[1]*y2+translate_mat_xyz1[2]*z2+translate_mat_xyz1[3]);
    
    float z_xyz2_deskew  = (translate_mat_xyz2[8]*x2+translate_mat_xyz2[9]*y2+translate_mat_xyz2[10]*z2+translate_mat_xyz2[11]);
    float y_xyz2_deskew = (translate_mat_xyz2[4]*x2+translate_mat_xyz2[5]*y2+translate_mat_xyz2[6]*z2+translate_mat_xyz2[7]);
    float x_xyz2_deskew  = (translate_mat_xyz2[0]*x2+translate_mat_xyz2[1]*y2+translate_mat_xyz2[2]*z2+translate_mat_xyz2[3]);

    float z_xyz3_deskew  = (translate_mat_xyz3[8]*x2+translate_mat_xyz3[9]*y2+translate_mat_xyz3[10]*z2+translate_mat_xyz3[11]);
    float y_xyz3_deskew = (translate_mat_xyz3[4]*x2+translate_mat_xyz3[5]*y2+translate_mat_xyz3[6]*z2+translate_mat_xyz3[7]);
    float x_xyz3_deskew  = (translate_mat_xyz3[0]*x2+translate_mat_xyz3[1]*y2+translate_mat_xyz3[2]*z2+translate_mat_xyz3[3]);

    float z_xyz4_deskew  = (translate_mat_xyz4[8]*x2+translate_mat_xyz4[9]*y2+translate_mat_xyz4[10]*z2+translate_mat_xyz4[11]);
    float y_xyz4_deskew = (translate_mat_xyz4[4]*x2+translate_mat_xyz4[5]*y2+translate_mat_xyz4[6]*z2+translate_mat_xyz4[7]);
    float x_xyz4_deskew  = (translate_mat_xyz4[0]*x2+translate_mat_xyz4[1]*y2+translate_mat_xyz4[2]*z2+translate_mat_xyz4[3]);

    float z_xyz5_deskew  = (translate_mat_xyz5[8]*x2+translate_mat_xyz5[9]*y2+translate_mat_xyz5[10]*z2+translate_mat_xyz5[11]);
    float y_xyz5_deskew = (translate_mat_xyz5[4]*x2+translate_mat_xyz5[5]*y2+translate_mat_xyz5[6]*z2+translate_mat_xyz5[7]);
    float x_xyz5_deskew  = (translate_mat_xyz5[0]*x2+translate_mat_xyz5[1]*y2+translate_mat_xyz5[2]*z2+translate_mat_xyz5[3]);

    float z_xyz6_deskew  = (translate_mat_xyz6[8]*x2+translate_mat_xyz6[9]*y2+translate_mat_xyz6[10]*z2+translate_mat_xyz6[11]);
    float y_xyz6_deskew = (translate_mat_xyz6[4]*x2+translate_mat_xyz6[5]*y2+translate_mat_xyz6[6]*z2+translate_mat_xyz6[7]);
    float x_xyz6_deskew  = (translate_mat_xyz6[0]*x2+translate_mat_xyz6[1]*y2+translate_mat_xyz6[2]*z2+translate_mat_xyz6[3]);

    float z_xyz7_deskew  = (translate_mat_xyz7[8]*x2+translate_mat_xyz7[9]*y2+translate_mat_xyz7[10]*z2+translate_mat_xyz7[11]);
    float y_xyz7_deskew = (translate_mat_xyz7[4]*x2+translate_mat_xyz7[5]*y2+translate_mat_xyz7[6]*z2+translate_mat_xyz7[7]);
    float x_xyz7_deskew  = (translate_mat_xyz7[0]*x2+translate_mat_xyz7[1]*y2+translate_mat_xyz7[2]*z2+translate_mat_xyz7[3]);

    float z_xyz8_deskew  = (translate_mat_xyz8[8]*x2+translate_mat_xyz8[9]*y2+translate_mat_xyz8[10]*z2+translate_mat_xyz8[11]);
    float y_xyz8_deskew = (translate_mat_xyz8[4]*x2+translate_mat_xyz8[5]*y2+translate_mat_xyz8[6]*z2+translate_mat_xyz8[7]);
    float x_xyz8_deskew  = (translate_mat_xyz8[0]*x2+translate_mat_xyz8[1]*y2+translate_mat_xyz8[2]*z2+translate_mat_xyz8[3]);
 
    //apply an inverse deskew transform to the get the actual neighbouring vertices in the skewed image
    //i.e., get actual neighbours

    float z_xyz1 = (mat[8]*x_xyz1_deskew+mat[9]*y_xyz1_deskew+mat[10]*z_xyz1_deskew+mat[11]);
    float y_xyz1 = (mat[4]*x_xyz1_deskew+mat[5]*y_xyz1_deskew+mat[6]*z_xyz1_deskew+mat[7]);
    float x_xyz1 = (mat[0]*x_xyz1_deskew+mat[1]*y_xyz1_deskew+mat[2]*z_xyz1_deskew+mat[3]);

    float z_xyz2 = (mat[8]*x_xyz2_deskew+mat[9]*y_xyz2_deskew+mat[10]*z_xyz2_deskew+mat[11]);
    float y_xyz2 = (mat[4]*x_xyz2_deskew+mat[5]*y_xyz2_deskew+mat[6]*z_xyz2_deskew+mat[7]);
    float x_xyz2 = (mat[0]*x_xyz2_deskew+mat[1]*y_xyz2_deskew+mat[2]*z_xyz2_deskew+mat[3]);

    float z_xyz3 = (mat[8]*x_xyz3_deskew+mat[9]*y_xyz3_deskew+mat[10]*z_xyz3_deskew+mat[11]);
    float y_xyz3 = (mat[4]*x_xyz3_deskew+mat[5]*y_xyz3_deskew+mat[6]*z_xyz3_deskew+mat[7]);
    float x_xyz3 = (mat[0]*x_xyz3_deskew+mat[1]*y_xyz3_deskew+mat[2]*z_xyz3_deskew+mat[3]);

    float z_xyz4 = (mat[8]*x_xyz4_deskew+mat[9]*y_xyz4_deskew+mat[10]*z_xyz4_deskew+mat[11]);
    float y_xyz4 = (mat[4]*x_xyz4_deskew+mat[5]*y_xyz4_deskew+mat[6]*z_xyz4_deskew+mat[7]);
    float x_xyz4 = (mat[0]*x_xyz4_deskew+mat[1]*y_xyz4_deskew+mat[2]*z_xyz4_deskew+mat[3]);

    float z_xyz5 = (mat[8]*x_xyz5_deskew+mat[9]*y_xyz5_deskew+mat[10]*z_xyz5_deskew+mat[11]);
    float y_xyz5 = (mat[4]*x_xyz5_deskew+mat[5]*y_xyz5_deskew+mat[6]*z_xyz5_deskew+mat[7]);
    float x_xyz5 = (mat[0]*x_xyz5_deskew+mat[1]*y_xyz5_deskew+mat[2]*z_xyz5_deskew+mat[3]);

    float z_xyz6 = (mat[8]*x_xyz6_deskew+mat[9]*y_xyz6_deskew+mat[10]*z_xyz6_deskew+mat[11]);
    float y_xyz6 = (mat[4]*x_xyz6_deskew+mat[5]*y_xyz6_deskew+mat[6]*z_xyz6_deskew+mat[7]);
    float x_xyz6 = (mat[0]*x_xyz6_deskew+mat[1]*y_xyz6_deskew+mat[2]*z_xyz6_deskew+mat[3]);

    float z_xyz7 = (mat[8]*x_xyz7_deskew+mat[9]*y_xyz7_deskew+mat[10]*z_xyz7_deskew+mat[11]);
    float y_xyz7 = (mat[4]*x_xyz7_deskew+mat[5]*y_xyz7_deskew+mat[6]*z_xyz7_deskew+mat[7]);
    float x_xyz7 = (mat[0]*x_xyz7_deskew+mat[1]*y_xyz7_deskew+mat[2]*z_xyz7_deskew+mat[3]);

    float z_xyz8 = (mat[8]*x_xyz8_deskew+mat[9]*y_xyz8_deskew+mat[10]*z_xyz8_deskew+mat[11]);
    float y_xyz8 = (mat[4]*x_xyz8_deskew+mat[5]*y_xyz8_deskew+mat[6]*z_xyz8_deskew+mat[7]);
    float x_xyz8 = (mat[0]*x_xyz8_deskew+mat[1]*y_xyz8_deskew+mat[2]*z_xyz8_deskew+mat[3]);


    //determine orthoganal plane as z_orth ; xyz4-z/tan(theta)

    //get pixel values at each coordinate
    float xyz1 = (READ_input_IMAGE(input, sampler, (int4)(x_xyz1, y_xyz1, z_xyz1, 0)).x);
    float xyz2 = (READ_input_IMAGE(input, sampler, (int4)(x_xyz2, y_xyz2, z_xyz2, 0)).x);
    
    float xyz3 = (READ_input_IMAGE(input, sampler, (int4)(x_xyz3, y_xyz3, z_xyz3, 0)).x);
    float xyz4 = (READ_input_IMAGE(input, sampler, (int4)(x_xyz4, y_xyz4, z_xyz4, 0)).x);

    float xyz5 = (READ_input_IMAGE(input, sampler, (int4)(x_xyz5, y_xyz5, z_xyz5, 0)).x);
    float xyz6 = (READ_input_IMAGE(input, sampler, (int4)(x_xyz6, y_xyz6, z_xyz6, 0)).x);
    
    float xyz7 = (READ_input_IMAGE(input, sampler, (int4)(x_xyz7, y_xyz7, z_xyz7, 0)).x);
    float xyz8 = (READ_input_IMAGE(input, sampler, (int4)(x_xyz8, y_xyz8, z_xyz8, 0)).x);


    
    //trilinear interpolation

    //interpolate along x
    float x1_f = ((x_xyz7 - x)* xyz6 + (x - x_xyz6)* xyz7)/(x_xyz7 - x_xyz6);//(xyz1*(1 - xd)) + xyz4*xd;  //
    float x2_f =  ((x_xyz3 - x)* xyz2 + (x - x_xyz2)* xyz3)/(x_xyz3 - x_xyz2);//(xyz2*(1 - xd)) + xyz3*xd;//
    float x3_f =  ((x_xyz8 - x)* xyz5 + (x - x_xyz5)* xyz8)/(x_xyz8 - x_xyz5);//(xyz5*(1 - xd)) + xyz5*xd;//
    float x4_f =  ((x_xyz4 - x)* xyz1 + (x - x_xyz1)* xyz4)/(x_xyz4 - x_xyz1);//(xyz6*(1 - xd)) + xyz7*xd;//

    //interpolate along y
    float y1_f = ((y_xyz6 - y)*x2_f  + (y - y_xyz2 )*x1_f )/(y_xyz6 - y_xyz2);//(x2_f*(1 - yd)) + x1_f*yd;//
    float y2_f = ((y_xyz5 - y)*x4_f  + (y - y_xyz1 )*x3_f )/(y_xyz5 - y_xyz1);//(x4_f*(1 - yd)) + x3_f*yd;//

    //interpolate along z
    pix = ((z_xyz6 - z)*y2_f  + (z - z_xyz1)*y1_f)/(z_xyz6 - z_xyz1);//(y1_f*(1 - zd)) + y2_f*zd;//
    
    //as the planes are tilted, how do we interpolate along them?
    //float z1_f = ((z_xyz4 - z)*y1_f  + (z - z_xyz3 )*y2_f )/(z_xyz4 - z_xyz3);
    //float z2_f = ((z_xyz8 - z)*y1_f  + (z - z_xyz7 )*y2_f )/(z_xyz8 - z_xyz7);

    //pix =  z1_f + z2_f;
    
    
    //float z_plane1 = (z_xyz2 + z_xyz6)/2;
    //float z_plane2 = (z_xyz1 + z_xyz5)/2;
    //pix = ((z_plane2 - z)*y1_f  + (z - z_plane1)*y2_f)/(z_plane2 - z_plane1);//(y1_f*(1 - zd)) + y2_f*zd;//
    
  }


  int4 pos = (int4){i, j, k,0};

  WRITE_output_IMAGE(output, pos, CONVERT_output_PIXEL_TYPE(pix));


}