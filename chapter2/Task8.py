from multiprocessing import Process

def print_square(num):
    print("Square: "{num * num})
def print_cube(num):
    print(f"Cube: {num * num * num}")

if __name__ == '__main__':

    pl = Process (target=print_square, args=(10,)) 
    p2 = Process (target=print_cube, args=(10,))
    pl.start()
    p2.start()

    pl.join()
    p2.join()

    print("Processes finished executing")