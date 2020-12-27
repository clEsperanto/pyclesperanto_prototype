
#pragma OPENCL EXTENSION cl_khr_local_int32_base_atomics : enable

const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

kernel void find_maxima_plateaus_1d_x(
    IMAGE_src_TYPE src,
    IMAGE_dst_TYPE dst
)
{
    const int image_width = GET_IMAGE_WIDTH(src);
    const int image_height = GET_IMAGE_HEIGHT(src);
    const int image_depth = GET_IMAGE_DEPTH(src);

    const int     y = get_global_id(1);
    const int     z = get_global_id(2);

    float maximum = 0;
    int last_step_up = -1;
    for (int x = 0; x < image_width; x++) {
        float value  = READ_src_IMAGE(src, sampler, POS_src_INSTANCE(x, y, z, 0)).x;
        if (value > maximum || x == 0) {
            maximum = value;
            last_step_up = x;
        }

        if (value < maximum || x == image_width - 1) {

            int delta = -1;
            if (x == image_width - 1 && last_step_up == x) {
                delta = 0;
            }
            maximum = value;

            if ( last_step_up > -1 ) {
                for (int tx = last_step_up; tx <= x + delta; tx++) {
                    WRITE_dst_IMAGE(dst, POS_dst_INSTANCE(tx, y, z, 0), 1);
                }
            }
            last_step_up = -1;
        }
    }
}

kernel void find_maxima_plateaus_1d_y(
    IMAGE_src_TYPE src,
    IMAGE_dst_TYPE dst
)
{
    const int image_width = GET_IMAGE_WIDTH(src);
    const int image_height = GET_IMAGE_HEIGHT(src);
    const int image_depth = GET_IMAGE_DEPTH(src);

    const int     x = get_global_id(0);
    const int     z = get_global_id(2);

    float maximum = 0;
    int last_step_up = -1;
    for (int y = 0; y < image_height; y++) {
        float value  = READ_src_IMAGE(src, sampler, POS_src_INSTANCE(x, y, z, 0)).x;
        if (value > maximum || y == 0) {
            maximum = value;
            last_step_up = y;
        }

        if (value < maximum || y == image_width - 1) {

            int delta = -1;
            if (y == image_width - 1 && last_step_up == y) {
                delta = 0;
            }
            maximum = value;

            if ( last_step_up > -1 ) {
                for (int ty = last_step_up; ty <= y + delta; ty++) {
                    WRITE_dst_IMAGE(dst, POS_dst_INSTANCE(x, ty, z, 0), 1);
                }
            }
            last_step_up = -1;
        }
    }
}


kernel void find_maxima_plateaus_1d_z(
    IMAGE_src_TYPE src,
    IMAGE_dst_TYPE dst
)
{
    const int image_width = GET_IMAGE_WIDTH(src);
    const int image_height = GET_IMAGE_HEIGHT(src);
    const int image_depth = GET_IMAGE_DEPTH(src);

    const int     x = get_global_id(0);
    const int     y = get_global_id(1);

    float maximum = 0;
    int last_step_up = -1;
    for (int z = 0; z < image_depth; z++) {
        float value  = READ_src_IMAGE(src, sampler, POS_src_INSTANCE(x, y, z, 0)).x;
        if (value > maximum || z == 0) {
            maximum = value;
            last_step_up = z;
        }

        if (value < maximum || z == image_width - 1) {

            int delta = -1;
            if (z == image_width - 1 && last_step_up == z) {
                delta = 0;
            }
            maximum = value;

            if ( last_step_up > -1 ) {
                for (int tz = last_step_up; tz <= z + delta; tz++) {
                    WRITE_dst_IMAGE(dst, POS_dst_INSTANCE(x, y, tz, 0), 1);
                }
            }
            last_step_up = -1;
        }
    }
}