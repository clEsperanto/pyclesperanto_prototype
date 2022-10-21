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

__kernel void affine_transform_3d_interpolate_trilinear(
    IMAGE_input_TYPE input,
	IMAGE_output_TYPE output,
    IMAGE_mat_TYPE mat,
    IMAGE_shear_mat_TYPE shear_mat,
    IMAGE_shear_mat_inv_TYPE shear_mat_inv,
    IMAGE_translate_mat_xyz1_TYPE translate_mat_xyz1,
    IMAGE_translate_mat_xyz2_TYPE translate_mat_xyz2,
    IMAGE_translate_mat_xyz3_TYPE translate_mat_xyz3,
    IMAGE_translate_mat_xyz4_TYPE translate_mat_xyz4,
    IMAGE_translate_mat_xyz5_TYPE translate_mat_xyz5,
    IMAGE_translate_mat_xyz6_TYPE translate_mat_xyz6,
    IMAGE_translate_mat_xyz7_TYPE translate_mat_xyz7,
    IMAGE_translate_mat_xyz8_TYPE translate_mat_xyz8)
{

  const sampler_t sampler = CLK_NORMALIZED_COORDS_TRUE|
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
    


    //get neighbouring vertices by using a translation matrix for x,y and z coordinates
    
    float z_xyz1_shear  = (translate_mat_xyz1[8]*xi+translate_mat_xyz1[9]*yi+translate_mat_xyz1[10]*zi+translate_mat_xyz1[11]);
    float y_xyz1_shear = (translate_mat_xyz1[4]*xi+translate_mat_xyz1[5]*yi+translate_mat_xyz1[6]*zi+translate_mat_xyz1[7]);
    float x_xyz1_shear  = (translate_mat_xyz1[0]*xi+translate_mat_xyz1[1]*yi+translate_mat_xyz1[2]*zi+translate_mat_xyz1[3]);
    
    float z_xyz2_shear  = (translate_mat_xyz2[8]*xi+translate_mat_xyz2[9]*yi+translate_mat_xyz2[10]*zi+translate_mat_xyz2[11]);
    float y_xyz2_shear = (translate_mat_xyz2[4]*xi+translate_mat_xyz2[5]*yi+translate_mat_xyz2[6]*zi+translate_mat_xyz2[7]);
    float x_xyz2_shear  = (translate_mat_xyz2[0]*xi+translate_mat_xyz2[1]*yi+translate_mat_xyz2[2]*zi+translate_mat_xyz2[3]);

    float z_xyz3_shear  = (translate_mat_xyz3[8]*xi+translate_mat_xyz3[9]*yi+translate_mat_xyz3[10]*zi+translate_mat_xyz3[11]);
    float y_xyz3_shear = (translate_mat_xyz3[4]*xi+translate_mat_xyz3[5]*yi+translate_mat_xyz3[6]*zi+translate_mat_xyz3[7]);
    float x_xyz3_shear  = (translate_mat_xyz3[0]*xi+translate_mat_xyz3[1]*yi+translate_mat_xyz3[2]*zi+translate_mat_xyz3[3]);

    float z_xyz4_shear  = (translate_mat_xyz4[8]*xi+translate_mat_xyz4[9]*yi+translate_mat_xyz4[10]*zi+translate_mat_xyz4[11]);
    float y_xyz4_shear = (translate_mat_xyz4[4]*xi+translate_mat_xyz4[5]*yi+translate_mat_xyz4[6]*zi+translate_mat_xyz4[7]);
    float x_xyz4_shear  = (translate_mat_xyz4[0]*xi+translate_mat_xyz4[1]*yi+translate_mat_xyz4[2]*zi+translate_mat_xyz4[3]);

    float z_xyz5_shear  = (translate_mat_xyz5[8]*xi+translate_mat_xyz5[9]*yi+translate_mat_xyz5[10]*zi+translate_mat_xyz5[11]);
    float y_xyz5_shear = (translate_mat_xyz5[4]*xi+translate_mat_xyz5[5]*yi+translate_mat_xyz5[6]*zi+translate_mat_xyz5[7]);
    float x_xyz5_shear  = (translate_mat_xyz5[0]*xi+translate_mat_xyz5[1]*yi+translate_mat_xyz5[2]*zi+translate_mat_xyz5[3]);

    float z_xyz6_shear  = (translate_mat_xyz6[8]*xi+translate_mat_xyz6[9]*yi+translate_mat_xyz6[10]*zi+translate_mat_xyz6[11]);
    float y_xyz6_shear = (translate_mat_xyz6[4]*xi+translate_mat_xyz6[5]*yi+translate_mat_xyz6[6]*zi+translate_mat_xyz6[7]);
    float x_xyz6_shear  = (translate_mat_xyz6[0]*xi+translate_mat_xyz6[1]*yi+translate_mat_xyz6[2]*zi+translate_mat_xyz6[3]);

    float z_xyz7_shear  = (translate_mat_xyz7[8]*xi+translate_mat_xyz7[9]*yi+translate_mat_xyz7[10]*zi+translate_mat_xyz7[11]);
    float y_xyz7_shear = (translate_mat_xyz7[4]*xi+translate_mat_xyz7[5]*yi+translate_mat_xyz7[6]*zi+translate_mat_xyz7[7]);
    float x_xyz7_shear  = (translate_mat_xyz7[0]*xi+translate_mat_xyz7[1]*yi+translate_mat_xyz7[2]*zi+translate_mat_xyz7[3]);

    float z_xyz8_shear  = (translate_mat_xyz8[8]*xi+translate_mat_xyz8[9]*yi+translate_mat_xyz8[10]*zi+translate_mat_xyz8[11]);
    float y_xyz8_shear = (translate_mat_xyz8[4]*xi+translate_mat_xyz8[5]*yi+translate_mat_xyz8[6]*zi+translate_mat_xyz8[7]);
    float x_xyz8_shear  = (translate_mat_xyz8[0]*xi+translate_mat_xyz8[1]*yi+translate_mat_xyz8[2]*zi+translate_mat_xyz8[3]);
 
    //apply an inverse shear transform to the vertices above to get the coordinates int eh original image
    //i.e., get actual neighbours
    float z_xyz1 = (shear_mat_inv[8]*x_xyz1_shear+shear_mat_inv[9]*y_xyz1_shear+shear_mat_inv[10]*z_xyz1_shear+shear_mat_inv[11]);
    float y_xyz1 = (shear_mat_inv[4]*x_xyz1_shear+shear_mat_inv[5]*y_xyz1_shear+shear_mat_inv[6]*z_xyz1_shear+shear_mat_inv[7]);
    float x_xyz1 = (shear_mat_inv[0]*x_xyz1_shear+shear_mat_inv[1]*y_xyz1_shear+shear_mat_inv[2]*z_xyz1_shear+shear_mat_inv[3]);

    float z_xyz2 = (shear_mat_inv[8]*x_xyz2_shear+shear_mat_inv[9]*y_xyz2_shear+shear_mat_inv[10]*z_xyz2_shear+shear_mat_inv[11]);
    float y_xyz2 = (shear_mat_inv[4]*x_xyz2_shear+shear_mat_inv[5]*y_xyz2_shear+shear_mat_inv[6]*z_xyz2_shear+shear_mat_inv[7]);
    float x_xyz2 = (shear_mat_inv[0]*x_xyz2_shear+shear_mat_inv[1]*y_xyz2_shear+shear_mat_inv[2]*z_xyz2_shear+shear_mat_inv[3]);

    float z_xyz3 = (shear_mat_inv[8]*x_xyz3_shear+shear_mat_inv[9]*y_xyz3_shear+shear_mat_inv[10]*z_xyz3_shear+shear_mat_inv[11]);
    float y_xyz3 = (shear_mat_inv[4]*x_xyz3_shear+shear_mat_inv[5]*y_xyz3_shear+shear_mat_inv[6]*z_xyz3_shear+shear_mat_inv[7]);
    float x_xyz3 = (shear_mat_inv[0]*x_xyz3_shear+shear_mat_inv[1]*y_xyz3_shear+shear_mat_inv[2]*z_xyz3_shear+shear_mat_inv[3]);

    float z_xyz4 = (shear_mat_inv[8]*x_xyz4_shear+shear_mat_inv[9]*y_xyz4_shear+shear_mat_inv[10]*z_xyz4_shear+shear_mat_inv[11]);
    float y_xyz4 = (shear_mat_inv[4]*x_xyz4_shear+shear_mat_inv[5]*y_xyz4_shear+shear_mat_inv[6]*z_xyz4_shear+shear_mat_inv[7]);
    float x_xyz4 = (shear_mat_inv[0]*x_xyz4_shear+shear_mat_inv[1]*y_xyz4_shear+shear_mat_inv[2]*z_xyz4_shear+shear_mat_inv[3]);

    float z_xyz5 = (shear_mat_inv[8]*x_xyz5_shear+shear_mat_inv[9]*y_xyz5_shear+shear_mat_inv[10]*z_xyz5_shear+shear_mat_inv[11]);
    float y_xyz5 = (shear_mat_inv[4]*x_xyz5_shear+shear_mat_inv[5]*y_xyz5_shear+shear_mat_inv[6]*z_xyz5_shear+shear_mat_inv[7]);
    float x_xyz5 = (shear_mat_inv[0]*x_xyz5_shear+shear_mat_inv[1]*y_xyz5_shear+shear_mat_inv[2]*z_xyz5_shear+shear_mat_inv[3]);

    float z_xyz6 = (shear_mat_inv[8]*x_xyz6_shear+shear_mat_inv[9]*y_xyz6_shear+shear_mat_inv[10]*z_xyz6_shear+shear_mat_inv[11]);
    float y_xyz6 = (shear_mat_inv[4]*x_xyz6_shear+shear_mat_inv[5]*y_xyz6_shear+shear_mat_inv[6]*z_xyz6_shear+shear_mat_inv[7]);
    float x_xyz6 = (shear_mat_inv[0]*x_xyz6_shear+shear_mat_inv[1]*y_xyz6_shear+shear_mat_inv[2]*z_xyz6_shear+shear_mat_inv[3]);

    float z_xyz7 = (shear_mat_inv[8]*x_xyz7_shear+shear_mat_inv[9]*y_xyz7_shear+shear_mat_inv[10]*z_xyz7_shear+shear_mat_inv[11]);
    float y_xyz7 = (shear_mat_inv[4]*x_xyz7_shear+shear_mat_inv[5]*y_xyz7_shear+shear_mat_inv[6]*z_xyz7_shear+shear_mat_inv[7]);
    float x_xyz7 = (shear_mat_inv[0]*x_xyz7_shear+shear_mat_inv[1]*y_xyz7_shear+shear_mat_inv[2]*z_xyz7_shear+shear_mat_inv[3]);

    float z_xyz8 = (shear_mat_inv[8]*x_xyz8_shear+shear_mat_inv[9]*y_xyz8_shear+shear_mat_inv[10]*z_xyz8_shear+shear_mat_inv[11]);
    float y_xyz8 = (shear_mat_inv[4]*x_xyz8_shear+shear_mat_inv[5]*y_xyz8_shear+shear_mat_inv[6]*z_xyz8_shear+shear_mat_inv[7]);
    float x_xyz8 = (shear_mat_inv[0]*x_xyz8_shear+shear_mat_inv[1]*y_xyz8_shear+shear_mat_inv[2]*z_xyz8_shear+shear_mat_inv[3]);



    //get pixel values at each coordinate
    float xyz1 = (READ_input_IMAGE(input, sampler, (float4)(x_xyz1/Nx, y_xyz1/Ny, z_xyz1/Nz, 0.f)).x);
    float xyz2 = (READ_input_IMAGE(input, sampler, (float4)(x_xyz2/Nx, y_xyz2/Ny, z_xyz1/Nz, 0.f)).x);
    
    float xyz3 = (READ_input_IMAGE(input, sampler, (float4)(x_xyz3/Nx, y_xyz3/Ny, z_xyz3/Nz, 0.f)).x);
    float xyz4 = (READ_input_IMAGE(input, sampler, (float4)(x_xyz4/Nx, y_xyz4/Ny, z_xyz4/Nz, 0.f)).x);

    float xyz5 = (READ_input_IMAGE(input, sampler, (float4)(x_xyz5/Nx, y_xyz5/Ny, z_xyz5/Nz, 0.f)).x);
    float xyz6 = (READ_input_IMAGE(input, sampler, (float4)(x_xyz6/Nx, y_xyz6/Ny, z_xyz6/Nz, 0.f)).x);
    
    float xyz7 = (READ_input_IMAGE(input, sampler, (float4)(x_xyz7/Nx, y_xyz7/Ny, z_xyz7/Nz, 0.f)).x);
    float xyz8 = (READ_input_IMAGE(input, sampler, (float4)(x_xyz8/Nx, y_xyz8/Ny, z_xyz8/Nz, 0.f)).x);


    
    //trilinear interpolation

    float xd = (x - x_xyz1_shear)/(x_xyz4_shear - x_xyz1_shear);
    float yd = (y - y_xyz2_shear) /(y_xyz1_shear - y_xyz2_shear);
    float zd = (z - z_xyz1_shear)/(z_xyz5_shear - z_xyz1_shear);

    //interpolate along x
    float x1_f = (xyz1*(1 - xd)) + xyz4*xd;  //((x_xyz4 - x)* xyz1 + (x - x_xyz1)* xyz4)/(x_xyz4 - x_xyz1);
    float x2_f =  (xyz2*(1 - xd)) + xyz3*xd;//((x_xyz3 - x)* xyz2 + (x - x_xyz2)* xyz3)/(x_xyz3 - x_xyz2);
    float x3_f =  (xyz5*(1 - xd)) + xyz5*xd;//((x_xyz8 - x)* xyz5 + (x - x_xyz5)* xyz8)/(x_xyz8 - x_xyz5);
    float x4_f =  (xyz6*(1 - xd)) + xyz7*xd;//((x_xyz7- x)* xyz6 + (x - x_xyz6)* xyz7)/(x_xyz7 - x_xyz6);

    //interpolate along y
    float y1_f = (x2_f*(1 - yd)) + x1_f*yd;//((y_xyz1 - y)*x2_f  + (y - y_xyz2 )*x1_f )/(y_xyz1 - y_xyz2);
    float y2_f = (x4_f*(1 - yd)) + x3_f*yd;//((y_xyz5 - y)*x4_f  + (y - y_xyz6 )*x3_f )/(y_xyz5 - y_xyz6);

    //interpolate along z
    pix = (y1_f*(1 - zd)) + y2_f*zd;//((z_xyz5 - z)*y1_f  + (z - z_xyz1)*y2_f)/(z_xyz5 - z_xyz1);

    


    //pix = ((y4_zn - y)* f1 + (y - y2_zn)* f2)/(y4_zn - y2_zn);
    
    //linear interpolation along z and y axes
    //float f1 = ((z3_zn - z)* left + (z - z1_zn)* right)/(z3_zn - z1_zn);
    //float f2 = ((y4_zn - y)* top + (y - y2_zn)* bottom)/(y4_zn - y2_zn);
    //pix = f1+f2;//f1+f2;


  }


  int4 pos = (int4){i, j, k,0};

  WRITE_output_IMAGE(output, pos, CONVERT_output_PIXEL_TYPE(pix));


}