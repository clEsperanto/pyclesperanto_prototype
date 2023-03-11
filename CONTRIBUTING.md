# Contributing to pyclesperanto_prototype

This page explains how to contribute to the project. In very general, feedback, bug reports, feature requests and pull-requests are welcome.

## Scope

`pyclesperanto_prototype` is a Python image processing library for processing 2D and 3D fluorescence microscopy imaging data using OpenCL-compatible graphics cards. 
Typical operations include
* image filtering
* spatial transforms
* matrix operations
* image segmentation
* cell neighborhood graph extraction and visualization
* quantitative feature extraction

Feature requests that are out of scope will be dealt with lower priority.

## Procedure

Before making a contribution to the project, please open a github issue and let's have a discussion about your ideas. 
We can then guide you where in the code-base your potential addition would fit.
Also check out the [API reference](https://clesperanto.github.io/pyclesperanto_prototype/docs/_build/html/) to see if there are functions available related to your proposed addition.

## How to develop

For developing the project code locally on your computer, it is recommended to fork the project and clone it using [github desktop](https://desktop.github.com/). 
Alternatively, you can clone your fork from the command line like this:

```
git clone git@github.com:your_github_account/pyclesperanto_prototype.git
cd pyclesperanto_prototype
git submodule init
git submodule update
```

When committing/pushing your changes to github, don't forget to create a branch first.

## Code structure

The project is divided into `tier`s. The lower level the tier is, the closer it is to the GPU driver. 
Higher level tiers implement more complex functionality. 
For example, in `tier1` the Gaussian blur is implemented. Difference-of-Gaussian is implemented in `tier2` and uses the Gaussian blur from `tier1`.

If you program new features, make sure it complies with our coding conventions:
* Your _new function_ comes in a `_new_function.py` and is called `new_function()`.
* Add `new_function` to the `__init__.py` of the tier where it is located.
* If the functions comes with OpenCL code, the corresponding OpenCL file is called `new_function.cl` and contains a function `new_function`. The file is located in the same folder as the corresponding python file.
* If the OpenCL algorithm implementation differs for 2D and 3D, there should be two OpenCL-files named `new_function_2d.cl` and `new_function_3d.cl`. Only one python file should be provided and the differentiation 2D/3D should be done inside `new_function()`.
* Your OpenCL code is image-type agnostic. Do not call OpenCL functions such as `read_imageui()` but `READ_IMAGE` place holders instead. You find a full list of place holders and further explanation [here](https://github.com/clEsperanto/clij-opencl-kernels#why-a-custom-opencl-dialect).

## How to submit pull-requests

When sending a pull-request, please make sure that you added tests for new features. 
For example for your `_my_function.py` add a `test_my_function.py` to the `tests/` folder.
Ideally, the code-coverage does not decrease when merging new functions.

## Related resources

This project is part of the clesperanto project. Read more about the [clesperanto mission](https://clesperanto.github.io).
This project is a descendant of [CLIJ](https://clij.github.io). Read more development hints in the CLIJ documentation:
* [Community guidelines](https://clij.github.io/clij2-docs/community_guidelines)
* [CLIJ's OpenCL dialect](https://github.com/clEsperanto/clij-opencl-kernels#why-a-custom-opencl-dialect)
* [FAQ](https://clij.github.io/clij2-docs/faq)
* [CLIJ plugin template](https://github.com/clij/clij2-plugin-template)

## Support

Feel free to ask questions on [https://image.sc](https://image.sc) or create a github issue.
