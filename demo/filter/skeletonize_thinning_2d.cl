__constant sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

__kernel void skeletonize3D(IMAGE_input_TYPE input, IMAGE_output_TYPE output)
{
    int x = get_global_id(0);
    int y = get_global_id(1);
    int width = GET_IMAGE_WIDTH(input);
    int height = GET_IMAGE_HEIGHT(input);
    int index = y * width + x;
    uchar skeletonValue = 255;
    
    // Check if the current pixel is inside the image boundary
    if (x >= 1 && y >= 1 && x < width - 1 && y < height - 1)
    {
        uchar A = input[(y-1) * width + (x-1)];
        uchar B = input[(y-1) * width + x];
        uchar C = input[(y-1) * width + (x+1)];
        uchar D = input[y * width + (x+1)];
        uchar E = input[(y+1) * width + (x+1)];
        uchar F = input[(y+1) * width + x];
        uchar G = input[(y+1) * width + (x-1)];
        uchar H = input[y * width + (x-1)];
        
        // Apply Zhang-Suen Thinning Algorithm
        int P1 = (!B && (A + D >= 1)) + (!D && (A + B >= 1)) + (!F && (B + E >= 1)) + (!E && (D + G >= 1)) + (!G && (H + F >= 1)) + (!H && (A + F >= 1)) + (!C && (A + E >= 1)) + (!A && (C + G >= 1));
        int P2 = A + B + C + D + E + F + G + H;
        int P3 = (!A || !B || !D) && (!B || !D || !E) && (!D || !E || !F) && (!E || !F || !G) && (!F || !G || !H) && (!G || !H || !A) && (!H || !A || !C) && (!A || !C || !B);
        int P4 = (B + C + D >= 1) && (D + E + F >= 1) && (F + G + H >= 1) && (H + A + B >= 1);
        
        // Check if the current pixel satisfies the thinning condition
        if (P1 == 1 && (P2 >= 2 && P2 <= 6) && P3 && P4 == 1)
        {
            output[index] = skeletonValue;
        }
        else
        {
            output[index] = input[index];
        }
    }
    else
    {
        output[index] = input[index];
    }
}
