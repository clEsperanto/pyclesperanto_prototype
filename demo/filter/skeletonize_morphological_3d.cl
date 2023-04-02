__constant sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

__kernel void skeletonize3D(IMAGE_input_TYPE input, IMAGE_output_TYPE output)
{
    int x = get_global_id(0);
    int y = get_global_id(1);
    int z = get_global_id(2);
    int width = GET_IMAGE_WIDTH(input);
    int height = GET_IMAGE_HEIGHT(input);
    int depth = GET_IMAGE_DEPTH(input);
    int index = z * width * height + y * width + x;
    float skeletonValue = 1;
    uchar D = (float)READ_IMAGE(input, sampler, POS_input_INSTANCE(x, y, z,0)).x;
    
    // Check if the current voxel is inside the image boundary
    if (x >= 1 && y >= 1 && z >= 1 && x < width - 1 && y < height - 1 && z < depth - 1)
    {
        // Apply morphological operations to the object in the image
        uchar A = (float)READ_IMAGE(input, sampler, POS_input_INSTANCE(x, y, z-1,0)).x;
        uchar B = (float)READ_IMAGE(input, sampler, POS_input_INSTANCE(x, y-1, z,0)).x;
        uchar C = (float)READ_IMAGE(input, sampler, POS_input_INSTANCE(x-1, y, z,0)).x;
        
        uchar E = (float)READ_IMAGE(input, sampler, POS_input_INSTANCE(x+1, y, z,0)).x;
        uchar F = (float)READ_IMAGE(input, sampler, POS_input_INSTANCE(x, y+1, z,0)).x;
        uchar G = (float)READ_IMAGE(input, sampler, POS_input_INSTANCE(x, y, z+1,0)).x;
        
        int P1 = (!B && (A + D >= 1)) + 
                 (!D && (A + B >= 1)) + 
                 (!F && (B + E >= 1)) + 
                 (!E && (D + G >= 1)) + 
                 (!G && (H + F >= 1)) + 
                 (!H && (A + F >= 1)) + 
                 (!C && (A + E >= 1)) + 
                 (!A && (C + G >= 1));
        


        int S1 = (!A && B) + (!B && C) + (!C && D) + (!D && E) + (!E && F) + (!F && G) + (!G && A);
        int S2 = A + B + C + D + E + F + G;
        int S3 = (!A && !B && !D) || (!B && !C && !E) || (!C && !D && !F) || (!D && !E && !G) || (!E && !F && !A) || (!F && !G && !B) || (!G && !A && !C);
        int S4 = (A && B && C) || (B && C && D) || (C && D && E) || (D && E && F) || (E && F && G) || (F && G && A) || (G && A && B);
        
        // Check if the current voxel satisfies the thinning condition
        if (S1 == 1 && (S2 >= 2 && S2 <= 6) && S3 && S4 == 0)
        {
            WRITE_IMAGE(output, POS_output_INSTANCE(x, y, z,0), skeletonValue);
            //output[index] = skeletonValue;
        }
        else
        {
            WRITE_IMAGE(output, POS_output_INSTANCE(x, y, z,0), D);
            //output[index] = D;
        }
    }
    else
    {
        WRITE_IMAGE(output, POS_output_INSTANCE(x, y, z,0), D);
    }
}
