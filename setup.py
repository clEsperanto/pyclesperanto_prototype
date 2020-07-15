from setuptools import setup, find_packages

setup(
    name="pyclesperanto_prototype",
    description='OpenCL kernels for GPU-accelerated image procesing.',
    author='Robert Haase',
    url='https://github.com/clEsperanto/pyclesperanto_prototype',
    packages=find_packages(),
    version="0.1.0",  # note: there are better tools for single-source version management
    install_requires=["numpy", "pyopencl", "toolz"]
)