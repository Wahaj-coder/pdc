import threading
import time

balance = 100
lock = threading.Lock()

def deposit(amount):
    global balance
    start_time = time.time()  # Start timing
    with lock:
        balance += amount
        print(f"Deposited: {amount}, New Balance: {balance}")
    end_time = time.time()  # End timing
    print(f"Deposit Execution Time: {end_time - start_time:.6f} seconds")

def withdraw(amount):
    global balance
    start_time = time.time()  # Start timing
    with lock:
        balance -= amount
        print(f"Withdrawn: {amount}, New Balance: {balance}")
    end_time = time.time()  # End timing
    print(f"Withdraw Execution Time: {end_time - start_time:.6f} seconds")

start_time = time.time()  # Start overall timing

t1 = threading.Thread(target=deposit, args=(50,))
t2 = threading.Thread(target=withdraw, args=(30,))

t1.start()
t2.start()

t1.join()
t2.join()

end_time = time.time()  # End overall timing

print(f"Final Balance: {balance}")
print(f"Total Execution Time: {end_time - start_time:.6f} seconds")
