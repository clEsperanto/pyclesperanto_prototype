// adapted code from
// https://github.com/bgaster/opencl-book-samples/blob/master/src/Chapter_14/histogram/histogram_image.cl
//
// It was published unter BSD license according to
// https://code.google.com/archive/p/opencl-book-samples/
//
// Book:      OpenCL(R) Programming Guide
// Authors:   Aaftab Munshi, Benedict Gaster, Timothy Mattson, James Fung, Dan Ginsburg
// ISBN-10:   0-321-74964-2
// ISBN-13:   978-0-321-74964-2
// Publisher: Addison-Wesley Professional
// URLs:      http://safari.informit.com/9780132488006/
//            http://www.openclprogrammingguide.com
//
//
//

#pragma OPENCL EXTENSION cl_khr_local_int32_base_atomics : enable

const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

kernel void histogram_3d(
    IMAGE_src_TYPE src,
    IMAGE_dst_histogram_TYPE dst_histogram,
    float minimum,
    float maximum,
    int step_size_x,
    int step_size_y,
    int step_size_z
)
{
    int     image_width = GET_IMAGE_WIDTH(src);
    int     image_height = GET_IMAGE_HEIGHT(src);
    int     image_depth = GET_IMAGE_DEPTH(src);
    int     y = get_global_id(0);
    float range = maximum - minimum;

    uint tmp_histogram[NUMBER_OF_HISTOGRAM_BINS];
    for (int i = 0; i < NUMBER_OF_HISTOGRAM_BINS; i++) {
        tmp_histogram[i] = 0;
    }

    for (int z = 0; z < image_depth; z+= step_size_z) {
        for (int x = 0; x < image_width; x+= step_size_x) {
            float clr = READ_src_IMAGE(src, sampler, (int4)(x, y, z, 0)).x;
            uint   indx_x;
            indx_x = convert_uint_sat( (clr - minimum) * (float)(GET_IMAGE_WIDTH(dst_histogram) - 1) / range );
            tmp_histogram[indx_x]++;
        }
    }

    for (int idx = 0; idx < GET_IMAGE_WIDTH(dst_histogram); idx++) {
        int4 pos = {idx, 0, y, 0};
        WRITE_dst_histogram_IMAGE(dst_histogram, pos, CONVERT_dst_histogram_PIXEL_TYPE(tmp_histogram[idx]));
    }
}



