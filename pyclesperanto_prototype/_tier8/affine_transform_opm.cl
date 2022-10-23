// adapted from: https://spiral.imperial.ac.uk/bitstream/10044/1/68022/1/Maioli-V-2016-PhD-Thesis.pdf
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


//pass a yz transform image
#ifndef SAMPLER_FILTER
#define SAMPLER_FILTER CLK_FILTER_NEAREST
#endif

#ifndef SAMPLER_ADDRESS
#define SAMPLER_ADDRESS CLK_ADDRESS_CLAMP
#endif

__kernel void affine_transform_opm(
    IMAGE_input_TYPE input,
	IMAGE_output_TYPE output,
	IMAGE_mat_TYPE mat,
    float pixel_step,
    float tantheta,
    float costheta,
    float sintheta)
{
 //OpenCL nearest interpolation using OPM code


 
  const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE|
      SAMPLER_ADDRESS;

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
  
  if (z >= 0 && y >= 0 && x >= 0 &&
      x < Nx && y < Ny && z < Nz)
  {
    float virtual_plane = y2 - z2/tantheta;
    float plane_before = virtual_plane/pixel_step +0.5f;
    float plane_after = plane_before +0.5f;

    float l_before = virtual_plane - plane_before * pixel_step;
    float l_after = pixel_step - l_before;

    float za = z/sintheta;
    float virtual_pos_before = za + (l_before*costheta);
    float virtual_pos_after = za - (l_after*costheta);
    
    //determine nearest data points to interpoloated point in raw data
    float pos_before = round(virtual_pos_before);
    float pos_after = round(virtual_pos_after);

    if  (pos_before>=0 && pos_after >= 0 && pos_before < Ny && pos_after < Ny)
    {
        float dz_before = virtual_pos_before - pos_before;
        float dz_after = virtual_pos_after - pos_after;

        float y_after = (pos_after+1.0);
        float y_after1 = (pos_after);

        float y_before = (pos_before+1.0);
        float y_before1 = (pos_before);

        //get pixel values at neighbour coordinates
        float pix_1 = (float)(READ_input_IMAGE(input, sampler, (float4)(x, y_after, plane_after, 0.f)).x);
        float pix_2 = (float)(READ_input_IMAGE(input, sampler, (float4)(x, y_after1, plane_after, 0.f)).x);
        
        float pix_3 = (float)(READ_input_IMAGE(input, sampler, (float4)(x, y_before, plane_before, 0.f)).x);
        float pix_4 = (float)(READ_input_IMAGE(input, sampler, (float4)(x, y_before1, plane_before, 0.f)).x);
        
        pix = ((l_before*dz_after*pix_1) + (l_before*(1-dz_after)*pix_2) + (l_after*dz_before*pix_3) + (l_after*(1-dz_before)*pix_4))/pixel_step;
    }

  }
    
  int4 pos = (int4){i, j, k,0};

  WRITE_output_IMAGE(output, pos, CONVERT_output_PIXEL_TYPE(pix));



}