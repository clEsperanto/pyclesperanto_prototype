# pyclesperanto
pyclesperanto is a prototype for [clEsperanto](http://clesperanto.net) - a multi-platform multi-language framework for GPU-accelerated image procesing. 
It uses [OpenCL kernels](https://github.com/clEsperanto/clij-opencl-kernels/tree/development/src/main/java/net/haesleinhuepf/clij/kernels) from [CLIJ](http://clij.github.io/)

Right now, this is very preliminary.

## Installation
* Get a python environment, e.g. via [mini-conda](https://docs.conda.io/en/latest/miniconda.html)
* Install [pyopencl](https://documen.tician.de/pyopencl/).

If installation of pyopencl for Windows fails, consider downloading a precompiled wheel (e.g. from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyopencl) ) and installing it manually:

```
pip install pyopencl-2019.1.1+cl12-cp37-cp37m-win_amd64.whl
```

Afterwards, install pyclesperanto:

```
pip install pyclesperanto-prototype
```

### Troubleshooting installation
If you receive an error like 
```
DLL load failed: The specified procedure could not be found.
```
Try downloading and installing a pyopencl with a lower cl version, e.g. cl12 : pyopencl-2020.1+cl12-cp37-cp37m-win_amd64

## Example code
Basically, you import clEsperanto:

```python
import pyclesperanto_prototype as cle
```

You can then push an image to the GPU and create memory there:
```python
import numpy as np

# push an array to the GPU
flip = cle.push(np.array([[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]]))

# create memory for the output
flop = cle.create((10,1))
```

And then you can call methods in the GPU without the need for learning OpenCL:

```python
# add a constant to all pixels
cle.add_image_and_scalar(flip, flop, 100.0)

# print result
print(flop)
```
