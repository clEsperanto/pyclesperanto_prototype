
__kernel void read_intensities(
    IMAGE_pointlist_TYPE pointlist,
    IMAGE_input_TYPE input,
    IMAGE_intensities_TYPE intensities
)
{
    const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

    const int pointlist_x = get_global_id(0);

    int x = READ_IMAGE(pointlist, sampler, POS_pointlist_INSTANCE(pointlist_x, 0, 0, 0)).x;
    int y = READ_IMAGE(pointlist, sampler, POS_pointlist_INSTANCE(pointlist_x, 1, 0, 0)).x;
    int z = 0;
    if (GET_IMAGE_HEIGHT(input) > 2) {
        z = READ_IMAGE(pointlist, sampler, POS_pointlist_INSTANCE(pointlist_x, 2, 0, 0)).x;
    }

    float intensity = READ_IMAGE(input, sampler, POS_input_INSTANCE(x, y, z, 0)).x;

    POS_intensities_TYPE dpos = POS_intensities_INSTANCE(pointlist_x, 0, 0, 0);
    WRITE_intensities_IMAGE(intensities, dpos, CONVERT_intensities_PIXEL_TYPE(intensity));
}
