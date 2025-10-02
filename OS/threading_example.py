import threading
import time

def task(name, delay):
    print(f"Task {name} started")
    time.sleep(delay)
    print(f"Task {name} finished after {delay} seconds.")

def single_threaded():
    start_time = time.time()
    task("A", 2)
    task("B", 2)
    end_time = time.time()
    print(f"Single-threaded execution time: {end_time - start_time} seconds")

def multi_threaded():
    start_time = time.time()

    t1 = threading.Thread(target=task, args=("A", 2))
    t2 = threading.Thread(target=task, args=("B", 2))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    end_time = time.time()
    print(f"Multi-threaded execution time: {end_time - start_time} seconds")

if __name__ == "__main__":
    print("Running single-threaded version")
    single_threaded()

    print("Running multi-threaded version")
    multi_threaded()
