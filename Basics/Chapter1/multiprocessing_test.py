import time
import multiprocessing
import threading
def do_something(size, out_list):
    for i in range(size):
        out_list.append(i + i) 
if __name__ == "__main__":
    size = 2000000
    procs = 4  # Number of processes
    jobs = []
    # Multiprocessing
    start_time = time.time()
    for i in range(procs):
        out_list = list()
        process = multiprocessing.Process(target=do_something, args=(size, out_list))
        jobs.append(process) 
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
    print("List processing complete")
    end_time = time.time()
    print("Multiprocessing time =", end_time - start_time)
    # Reset jobs list for threading
    jobs = []
    threads = 4  # Number of threads
    start_time = time.time()
    for k in range(threads):
        out_list = list()
        thread = threading.Thread(target=do_something, args=(size, out_list))
        jobs.append(thread)
    for l in jobs:
        l.start()
    for l in jobs:
        l.join()
    print("List processing complete")
    end_time = time.time()
    print("Multithreading time =", end_time - start_time)
