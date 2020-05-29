def sigma_to_kernel_size(sigma):
    n = int(float(sigma) * 8.0)
    if (n % 2 == 0):
        n = n + 1
    return n