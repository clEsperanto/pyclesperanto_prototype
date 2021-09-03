import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyclesperanto_prototype",
    version="0.10.0",
    author="haesleinhuepf",
    author_email="robert.haase@tu-dresden.de",
    description="GPU-accelerated image processing in python using OpenCL",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/clEsperanto/pyclesperanto_prototype",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        "numpy!=1.19.4",
        "pyopencl",
        "toolz",
        "scikit-image>=0.18.0",
        "matplotlib",
        "transforms3d",
        "reikna",
    ],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Development Status :: 3 - Alpha",
    ],
)
