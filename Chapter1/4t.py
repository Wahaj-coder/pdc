import threading
import time
from concurrent.futures import ThreadPoolExecutor
# Define two simple tasks
def task_1():
    print("Task 1 executed")
def task_2():
    print("Task 2 executed")
# Measure time using ThreadPoolExecutor
start_time_executor = time.time()

with ThreadPoolExecutor() as executor:
    future1 = executor.submit(task_1)
    future2 = executor.submit(task_2)

end_time_executor = time.time()
execution_time_executor = end_time_executor - start_time_executor
print(f"Execution time with ThreadPoolExecutor: {execution_time_executor:.4f} seconds")

# Measure time using threading library directly
start_time_threading = time.time()

thread1 = threading.Thread(target=task_1)
thread2 = threading.Thread(target=task_2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

end_time_threading = time.time()
execution_time_threading = end_time_threading - start_time_threading
print(f"Execution time with threading library: {execution_time_threading:.4f} seconds")
