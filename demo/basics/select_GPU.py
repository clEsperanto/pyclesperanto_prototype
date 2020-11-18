import pyclesperanto_prototype as cle

# list names of all available OpenCL-devices
print("Available OpenCL devices:" + str(cle.available_device_names()))

# selecting an Nvidia RTX
cle.select_device("RTX")
print("Using OpenCL device " + cle.get_device().name)

# selecting an Nvidia GTX
cle.select_device("GTX")
print("Using OpenCL device " + cle.get_device().name)

# selecting an Intel UHD GPU
cle.select_device("Intel")
print("Using OpenCL device " + cle.get_device().name)

# selecting an AMD Vega GPU
cle.select_device("904")
print("Using OpenCL device " + cle.get_device().name)

# selecting an AMD Vega GPU
cle.select_device("902")
print("Using OpenCL device " + cle.get_device().name)

