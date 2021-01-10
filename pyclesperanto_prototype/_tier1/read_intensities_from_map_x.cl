
__kernel void read_intensities_from_map(
    IMAGE_labels_TYPE labels,
    IMAGE_map_image_TYPE map_image,
    IMAGE_intensities_TYPE intensities
)
{
    const sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

    const int x = get_global_id(0);
    const int y = get_global_id(1);
    const int z = get_global_id(2);

    int label = READ_IMAGE(labels, sampler, POS_labels_INSTANCE(x, y, z, 0)).x;

    float intensity = READ_IMAGE(map_image, sampler, POS_map_image_INSTANCE(x, y, z, 0)).x;

    POS_intensities_TYPE dpos = POS_intensities_INSTANCE(label, 0, 0, 0);
    WRITE_intensities_IMAGE(intensities, dpos, CONVERT_intensities_PIXEL_TYPE(intensity));
}
