import pyopencl as cl
from functools import lru_cache
import numpy as np
from typing import Tuple

from .._tier0 import get_device


def empty_image(ctx, shape, dtype, num_channels=1, channel_order=None):
    if not len(shape) in [2, 3]:
        raise ValueError(
            "number of dimension = %s not supported (can be 2 or 3)" % len(shape)
        )
    if num_channels not in [1, 2, 3, 4]:
        raise ValueError(
            "number of channels = %s not supported (can be 1,2, 3 or 4)" % num_channels
        )

    mem_flags = cl.mem_flags.READ_WRITE
    channel_type = cl.DTYPE_TO_CHANNEL_TYPE[np.dtype(dtype)]

    _dict_channel_order = {
        1: cl.channel_order.R,
        2: cl.channel_order.RG,
        3: cl.channel_order.RGB,
        4: cl.channel_order.RGBA,
    }

    if channel_order is None:
        channel_order = _dict_channel_order[num_channels]

    img_format, reshape = _get_image_format(ctx, num_channels, dtype, len(shape))
    if reshape:
        raise ValueError("unsupported")

    fmt = cl.ImageFormat(channel_order, channel_type)
    res = cl.Image(ctx, mem_flags, fmt, shape=shape[::-1])
    res.dtype = dtype
    res.num_channels = num_channels
    from ._pycl import _OCLImage
    return _OCLImage(res)


def empty_image_like(arr, ctx=None):
    from ._backends import Backend
    return Backend.get_instance().get().empty_image_like(arr, ctx)


def create_image(arr: np.ndarray, ctx: cl.Context = None, *args, **kwargs) -> cl.Image:
    if ctx is None:
        ctx = get_device().context

    """Create a pyopencl.Image from a numpy array.

    Parameters
    ----------
    arr : np.ndarray
        The numpy array to convert.  ndim must be between 2-4
    ctx : cl.Context
        The cl.Context object in which to create the Image

    Returns
    -------
    cl.Image
        The Image object.

    Raises
    ------
    ValueError
        If the arr has <2 or >4 dims
    """
    if arr.ndim not in {2, 3, 4}:
        raise ValueError("Array must have between 2-4 dims, but has {arr.ndim}")
    # if arr.dtype.type == np.complex64:
    #     raise ValueError("")
    #     # num_channels = 2
    #     # res = empty_image(ctx, arr.shape, dtype=np.float32, num_channels=num_channels)
    #     # res.write_array(arr)
    #     # res.dtype = np.float32
    # else:
    num_channels = arr.shape[-1] if arr.ndim == 4 else 1
    res = _image_from_array(
        ctx, np.ascontiguousarray(arr), num_channels, *args, **kwargs
    )
    res.dtype = arr.dtype

    res.num_channels = num_channels
    res.ndim = arr.ndim
    return res


@lru_cache(maxsize=64)
def _get_image_format(
    ctx: cl.Context, num_channels: int, dtype: np.dtype, ndim: int, mode: str = "rw"
) -> Tuple[cl.ImageFormat, bool]:
    """Maximize chance of finding a supported image format for the current device.

    Parameters
    ----------
    ctx : cl.Context
        The Context object creating the image
    num_channels : int
        Number of channels in the image
    dtype : np.dtype
        Image type
    ndim : int (must be 1, 2, or 3)
        Number of dimensions in the array.
    mode : {'rw', 'r', 'w'}, optional
        The memory mode, by default "rw"

    Returns
    -------
    tuple
        A tuple of (format, bool) with an cl.ImageFormat suitable for this image,
        and a "reshape" flag indicating that Device support forced reshaping of
        single channel array to RGBA.  (The actual reshaping is handled in
        _image_from_array)

    Raises
    ------
    ValueError
        If mode is not one of {'rw', 'r', 'w'}
        If the number of dimensions is not 1, 2, or 3
        If the dtype is not supported
        If num_channels > 4
    """
    if mode == "rw":
        mode_flag = cl.mem_flags.READ_WRITE
    elif mode == "r":
        mode_flag = cl.mem_flags.READ_ONLY
    elif mode == "w":
        mode_flag = cl.mem_flags.WRITE_ONLY
    else:
        raise ValueError(f"invalid value {mode!r} for 'mode'")

    if ndim == 3:
        _dim = cl.mem_object_type.IMAGE3D
    elif ndim == 2:
        _dim = cl.mem_object_type.IMAGE2D
    elif ndim == 1:
        _dim = cl.mem_object_type.IMAGE1D
    else:
        raise ValueError(f"Unsupported number of image dimensions: {ndim}")

    supported_formats = cl.get_supported_image_formats(ctx, mode_flag, _dim)
    try:
        channel_type = cl.DTYPE_TO_CHANNEL_TYPE[dtype]
    except KeyError:
        raise ValueError(f"Unsupported dtype for image: {dtype}")

    if num_channels == 1:
        for order in [
            cl.channel_order.INTENSITY,
            cl.channel_order.R,
            cl.channel_order.Rx,
        ]:
            fmt = cl.ImageFormat(order, channel_type)
            if fmt in supported_formats:
                return fmt, False

        fmt = cl.ImageFormat(cl.channel_order.RGBA, channel_type)
        if fmt in supported_formats:
            return fmt, True
        raise ValueError(
            f"No supported ImageFormat found for dtype {dtype} with 1 channel\n",
            f"Supported formats include: {supported_formats!r}",
        )
    img_format = {
        2: cl.channel_order.RG,
        3: cl.channel_order.RGB,
        4: cl.channel_order.RGBA,
    }
    if num_channels not in img_format:
        raise ValueError(f"Cannot handle image with {num_channels} channels.")

    return cl.ImageFormat(img_format[num_channels], channel_type), False


# vendored from pyopencl.image_from_array so that we can change the img_format
# used for a single channel image to channel_order.INTENSITY
def _image_from_array(
    ctx: cl.Context,
    ary: np.ndarray,
    num_channels: int = None,
    mode: str = "r",
    norm_int: bool = False,
) -> cl.Image:
    if not ary.flags.c_contiguous:
        raise ValueError("array must be C-contiguous")

    dtype = ary.dtype
    if num_channels is None:

        import pyopencl.cltypes

        try:
            dtype, num_channels = pyopencl.cltypes.vec_type_to_scalar_and_count[dtype]
        except KeyError:
            # It must be a scalar type then.
            num_channels = 1

        shape = ary.shape
        strides = ary.strides

    elif num_channels == 1:
        shape = ary.shape
        strides = ary.strides
    else:
        if ary.shape[-1] != num_channels:
            raise RuntimeError("last dimension must be equal to number of channels")

        shape = ary.shape[:-1]
        strides = ary.strides[:-1]

    if mode == "r":
        mode_flags = cl.mem_flags.READ_ONLY
    elif mode == "w":
        mode_flags = cl.mem_flags.WRITE_ONLY
    else:
        raise ValueError("invalid value '%s' for 'mode'" % mode)

    img_format, reshape = _get_image_format(ctx, num_channels, dtype, ary.ndim)
    if reshape:
        import warnings

        warnings.warn("Device support forced reshaping of single channel array to RGBA")
        ary = np.ascontiguousarray(np.repeat(ary[..., np.newaxis], 4, axis=-1))
        shape = ary.shape[:-1]
        strides = ary.strides[:-1]

    assert ary.strides[-1] == ary.dtype.itemsize

    return cl.Image(
        ctx,
        mode_flags | cl.mem_flags.COPY_HOST_PTR,
        img_format,
        shape=shape[::-1],
        pitches=strides[::-1][1:],
        hostbuf=ary,
    )
