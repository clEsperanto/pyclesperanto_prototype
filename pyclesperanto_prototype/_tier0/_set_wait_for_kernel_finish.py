def set_wait_for_kernel_finish(wait_for_kernel_finish : bool = None):
    from ._program import OCLProgram
    OCLProgram._wait_for_kernel_finish = wait_for_kernel_finish