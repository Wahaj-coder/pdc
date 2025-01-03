import multiprocessing
import time

# Function that each process will run
def foo():
    # Get the name of the current process
    process_name = multiprocessing.current_process().name
    print(f"Starting process: {process_name}")

    if process_name == 'background_process':
        # Behavior specific to the background process
        for i in range(0, 5):
            print(f"{process_name} ---> {i}")
            time.sleep(1)
    else:
        # Behavior specific to the non-background process
        for i in range(5, 9):
            print(f"{process_name} ---> {i}")
            time.sleep(1)

    print(f"Exiting process: {process_name}")


if __name__ == '__main__':
    background_process = multiprocessing.Process(
        name='background_process',
        target=foo
    )
    background_process.daemon = True

    non_background_process = multiprocessing.Process(
        name='non_background_process',
        target=foo
    )
    non_background_process.daemon = False

    # Start the processes
    background_process.start()
    non_background_process.start()

    # Wait for the non-daemon process to complete
    #on_background_process.join()

    # Adding this delay will allow the daemon process to run briefly
    time.sleep(2)
