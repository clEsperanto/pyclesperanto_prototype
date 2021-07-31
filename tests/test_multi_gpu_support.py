import numpy as np
import pyclesperanto_prototype as cle
def test_single_gpu_support():
    dev1 = cle.new_device("RTX")

    print(dev1)

    image = np.random.random((2048,2048,10))
    gpu_input1 = cle.push(image, device=dev1)

    gpu_output1 = cle.create_like(gpu_input1, device=dev1)

    cle.gaussian_blur(gpu_input1, gpu_output1, sigma_x=1, sigma_y=1, device=dev1)

    output1 = cle.pull(gpu_output1)
    assert not np.allclose(output1, image)

def test_multi_gpu_support():
    dev1 = cle.new_device("RTX")
    dev2 = cle.new_device("gfx")

    print(dev1)
    print(dev2)

    image = np.random.random((2048,2048,10))
    gpu_input1 = cle.push(image, device=dev1)
    gpu_input2 = cle.push(image, device=dev2)

    gpu_output1 = cle.create_like(gpu_input1, device=dev1)
    gpu_output2 = cle.create_like(gpu_input2, device=dev2)

    cle.gaussian_blur(gpu_input1, gpu_output1, sigma_x=1, sigma_y=1, device=dev1)
    cle.gaussian_blur(gpu_input2, gpu_output2, sigma_x=1, sigma_y=1, device=dev2)

    output1 = cle.pull(gpu_output1)
    output2 = cle.pull(gpu_output2)

    assert(np.allclose(output1, output2))
