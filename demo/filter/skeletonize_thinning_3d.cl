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
    int neighbors[26];
    int count, transitionCount;
    float currentValue, neighborValue;
    float skeletonValue = 1;
    
    // Check if the current voxel is inside the image boundary
    if (x >= 1 && y >= 1 && z >= 1 && x < width - 1 && y < height - 1 && z < depth - 1)
    {
        currentValue = (float)READ_IMAGE(input, sampler, POS_input_INSTANCE(x, y, z,0)).x;
        //input[index];
        count = 0;
        transitionCount = 0;
        
        // Compute the 26-neighborhood of the current voxel
        for (int k = -1; k <= 1; k++)
        {
            for (int j = -1; j <= 1; j++)
            {
                for (int i = -1; i <= 1; i++)
                {
                    if (i == 0 && j == 0 && k == 0) continue;
                    neighborValue = (float)READ_IMAGE(input, sampler, POS_input_INSTANCE(x+i, y+j, z+k,0)).x;
                    //input[(z + k) * width * height + (y + j) * width + (x + i)];
                    neighbors[count++] = neighborValue;
                    if (currentValue != neighborValue) transitionCount++;
                }
            }
        }
        
        // Check if the current voxel satisfies the thinning condition
        if (currentValue == 0 && transitionCount >= 2 && transitionCount <= 6)
        {
            // Compute the 6 sub-neighborhoods of the current voxel
            for (int i = 0; i < 6; i++)
            {
                int subNeighbors[8];
                int subCount = 0;
                int tCount = 0;
                for (int j = 0; j < 4; j++)
                {
                    int idx = i * 4 + j;
                    neighborValue = neighbors[idx];
                    subNeighbors[subCount++] = neighborValue;
                    if (currentValue != neighborValue) tCount++;
                }
                for (int j = 0; j < 4; j++)
                {
                    int idx = i * 4 + (j + 1) % 4;
                    neighborValue = neighbors[idx];
                    subNeighbors[subCount++] = neighborValue;
                    if (currentValue != neighborValue) tCount++;
                }
                if (currentValue == 0 && tCount == 2)
                {
                    int A = subNeighbors[0] * subNeighbors[2] * subNeighbors[6];
                    int B = subNeighbors[0] * subNeighbors[4] * subNeighbors[6];
                    if (A == 0 || B == 0)
                    {
                        WRITE_IMAGE(output, POS_output_INSTANCE(x, y, z,0), skeletonValue);
                        //output[index] = skeletonValue;
                    }
                }
            }
        }
        else
        {
            WRITE_IMAGE(output, POS_output_INSTANCE(x, y, z,0), currentValue);
            //output[index] = currentValue;
        }
    }
}