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

__kernel void affine_transform_3d_interpolate(
    IMAGE_input_TYPE input,
    IMAGE_output_TYPE output,
    IMAGE_mat_TYPE mat)
{

  const sampler_t sampler = CLK_NORMALIZED_COORDS_TRUE|
      SAMPLER_ADDRESS |	SAMPLER_FILTER;

  uint i = get_global_id(0);
  uint j = get_global_id(1);
  uint k = get_global_id(2);

  uint Nx = GET_IMAGE_WIDTH(input);
  uint Ny = GET_IMAGE_HEIGHT(input);
  uint Nz = GET_IMAGE_DEPTH(input);

  //float x = (mat[0]*i+mat[1]*j+mat[2]*k+mat[3]);
  //float y = (mat[4]*i+mat[5]*j+mat[6]*k+mat[7]);
  //float z = (mat[8]*i+mat[9]*j+mat[10]*k+mat[11]);
  ////ensure correct sampling, see opencl 1.2 specification pg. 329
  //x += 0.5f;
  //y += 0.5f;
  //z += 0.5f;

  float x = i+0.5f;
  float y = j+0.5f;
  float z = k+0.5f;

  float z2 = (mat[8]*x+mat[9]*y+mat[10]*z+mat[11]);
  float y2 = (mat[4]*x+mat[5]*y+mat[6]*z+mat[7]);
  float x2 = (mat[0]*x+mat[1]*y+mat[2]*z+mat[3]);

  //float4 coord_norm = (float4)(x2 * GET_IMAGE_WIDTH(input) / GET_IMAGE_WIDTH(output) / Nx,y2 * GET_IMAGE_HEIGHT(input) / GET_IMAGE_HEIGHT(output) / Ny, z2  * GET_IMAGE_DEPTH(input) / GET_IMAGE_DEPTH(output) / Nz,0.f); 
  float4 coord_norm = (float4)(x2/Nx,y2/Ny,z2/Nz,0.f);

  float pix = (float)(READ_input_IMAGE(input, sampler, coord_norm).x);
  int4 pos = (int4){i, j, k,0};

  WRITE_output_IMAGE(output, pos, CONVERT_output_PIXEL_TYPE(pix));
  
}