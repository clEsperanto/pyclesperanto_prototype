
__kernel void detect_maxima_3d(
        IMAGE_src_TYPE src,
        IMAGE_dst_TYPE dst
)
{
    const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

    int radius = 1;

    int i = get_global_id(0);
    int j = get_global_id(1);
    int k = get_global_id(2);

    if (i == 0 && j == 0 && k == 0) {
        printf("size: %d\n", get_global_size(2));
    }

    POS_src_TYPE pos = POS_src_INSTANCE(i, j, k, 0);
    float localMax = READ_src_IMAGE(src, sampler, pos).x - 1;
    int4 localMaxPos = pos;

    for(int x = -radius; x < radius + 1; x++)
    {
        for(int y = -radius; y < radius + 1; y++)
        {
            for(int z = -radius; z < radius + 1; z++)
            {
                const POS_src_TYPE localPos = POS_src_INSTANCE( i + x, j + y, k + z, 0);

                float value = READ_src_IMAGE(src, sampler, localPos).x;

                
                if (value > localMax) {
                    localMax = value;
                    localMaxPos = localPos;
                }
            }
        }
    }


    POS_dst_TYPE dpos = POS_dst_INSTANCE(get_global_id(0), get_global_id(1), get_global_id(2), 0);
    if (pos.x == localMaxPos.x && pos.y == localMaxPos.y && pos.z == localMaxPos.z) {
        WRITE_dst_IMAGE(dst, dpos, 1);
    } else {
        WRITE_dst_IMAGE(dst, dpos, 0);
    }
}
