import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyclesperanto_prototype-haesleinhuepf", # Replace with your own username
    version="0.0.1",
    author="haesleinhuepf",
    author_email="rhaase@mpi-cbg.de",
    description="OpenCL GPU accelerated image processing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/clEsperanto/pyclesperanto_prototype",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)