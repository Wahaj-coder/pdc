
import threading

balance = 100
lock = threading.Lock()

def deposit (amount): 
    global balance
    with lock:
        balance += amount
        print (f"Deposited: {amount}, New Balance: {balance}")

def withdraw (amount):

    global balance
    with lock:
        balance = amount
        print(f"Withdrawn: {amount}, New Balance: {balance}")

t1 = threading. Thread (target=deposit, args=(50,)) 
t2 = threading.Thread(target=withdraw, args=(30,))

t1.start()
t2.start()

t1.join()
t2.join()