
import threading

def calc_fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return calc_fibonacci(n-1) + calc_fibonacci(n-2)

threads = []

for i in range(4): 
    t = threading.Thread (target=calc_fibonacci, args=(30,)) 
    threads.append(t)

    print (f"Starting thread {i + 1}") 
    t.start()
for t in threads:
    t.join()