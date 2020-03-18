# pyclesperanto
pyclesperanto is a prototype for [clEsperanto](http://clesperanto.net) - a multi-platform multi-language framework for GPU-accelerated image procesing. 
It uses [OpenCL kernels](https://github.com/clEsperanto/clij-opencl-kernels/tree/development/src/main/java/net/haesleinhuepf/clij/kernels) from [CLIJ](http://clij.github.io/)

Right now, this is very preliminary.

## Installation
* Get a python environment, e.g. via [mini-conda](https://docs.conda.io/en/latest/miniconda.html)
* Install [pyopencl](https://documen.tician.de/pyopencl/) and [gputools](https://github.com/maweigert/gputools/). 

If installation of gputools doesn't work because of issues with pyopencl for Windows, consider downloading a precompiled wheel (e.g. from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyopencl) ) and installing it manually:

```
pip install pyopencl-2019.1.1+cl12-cp37-cp37m-win_amd64.whl
pip install gputools
```

## Example code
An example is available in [this script](https://github.com/clEsperanto/pyclesperanto_prototype/blob/master/cle_test.py). 
Basically, you import the methods from clEsperanto you need:

```python
from clesperanto import push
from clesperanto import create
from clesperanto import addImageAndScalar
```

You can then push image to the GPU and create memory there:
```python
# push an array to the GPU
flip = push(np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]))

# create memory for the output
flop = create((10,))
```

And then you can call method in the GPU without the need for learning OpenCL:

```python
# add a constant to all pixels
addImageAndScalar(flip, flop, 100.0)

# print result
print(flop)
```
