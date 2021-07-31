import pyclesperanto_prototype as cle
import numpy as np
import time



def test_multi_gpu_threading():
    import threading
    import time

    class myThread(threading.Thread):
        def __init__(self, threadID, name, counter, image):
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.name = name
            self.counter = counter
            self.device = cle.new_device(name)
            self.image = cle.push(image, device=self.device)

        def run(self):
            print("Starting " + self.name)
            self.print_time()
            print("Exiting " + self.name)

        def print_time(self):
            while self.counter:
                self.image = cle.gaussian_blur(self.image, sigma_x=15, sigma_y=15, sigma_z=15, device=self.device)
                time.sleep(0.1)
                print("%s: %s gaussian blur" % (self.name, time.ctime(time.time())))
                self.counter -= 1

    image = np.random.random((100, 100, 10))

    # Create new threads
    thread1 = myThread(1, "RTX", 15, image) # RTX gpu
    thread2 = myThread(2, "gfx", 12, image) # AMD gpu
    thread3 = myThread(3, "Intel", 11, image) # Intel gpu

    # Start new Threads
    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()

    print("Exiting Main Thread")

def test_slinge_gpu_multi_threading():
    import threading
    import time

    class myThread(threading.Thread):
        def __init__(self, threadID, name, counter, image):
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.name = "T" + str(threadID)
            self.counter = counter
            self.device = cle.new_device(name)
            self.image = cle.push(image, device=self.device)

        def run(self):
            #print("Starting " + self.name)
            self.print_time()
            #print("Exiting " + self.name)

        def print_time(self):
            while self.counter:
                self.image = cle.gaussian_blur(self.image, sigma_x=25, sigma_y=25, sigma_z=25, device=self.device)
                time.sleep(0.1) # this is important; other threads can use this time better
                #print("%s: %s gaussian blur" % (self.name, time.ctime(time.time())))
                self.counter -= 1

    image = np.random.random((100, 100, 10))

    num_tasks = 10
    gpu_name = "RTX"

    start_time = time.time()
    # Create new threads
    threads = [myThread(i + 1, gpu_name, 15, image) for i in range(num_tasks)]

    # Start new Threads
    for thread in threads:
        thread.start()

    # wait for finish
    for thread in threads:
        thread.join()
    print("Parallel all done after ", time.time() - start_time, "s")

    # Create new threads
    start_time = time.time()
    threads = [myThread(i + 1, gpu_name, 15, image) for i in range(num_tasks)]

    for thread in threads:
        # Start new Threads
        thread.start()
        # wait for finish
        thread.join()

    print("Sequential all done after ", time.time() - start_time, "s")


    assert False

