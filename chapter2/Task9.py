
from multiprocessing import Process, Queue 

def producer(queue):
    for i in range(5):
        queue.put(i)
        print(f"Produced {i}")

def consumer(queue):
    while not queue.empty(): 
        item = queue.get()
        print(f"Consumed {item}")

if __name__ == '__main__':

    queue = Queue()

    p1 = Process(target=producer, args=(queue,))
    P2 = Process (target=consumer,  args=(queue,))


    p1.start()
    p1.join()

    p2.start()
    p2.join()
    print("Producer and consumer processes finised")