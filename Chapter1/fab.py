import threading
import time
# Define the Fibonacci function
def calc_fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return calc_fibonacci(n - 1) + calc_fibonacci(n - 2)
# Function to create and run threads
def run_threads(num_threads, fib_input):
    threads = []
    start_time = time.time()  # Record the start time
    # Creating threads
    for i in range(num_threads):
        t = threading.Thread(target=calc_fibonacci, args=(fib_input,))
        threads.append(t)
        t.start()
    # Joining threads
    for t in threads:
        t.join()
    end_time = time.time()  # Record the end time
    return end_time - start_time
if __name__ == "__main__":
    fib_input = 35  # Fibonacci input for calculation   
    # Measure execution time with 4 threads
    time_4_threads = run_threads(4, fib_input)
    print(f"Execution time with 4 threads: {time_4_threads:.4f} seconds")   
    # Measure execution time with 9 threads
    time_9_threads = run_threads(9, fib_input)
    print(f"Execution time with 9 threads: {time_9_threads:.4f} seconds")
