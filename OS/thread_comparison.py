import threading
import time

def task(name, delay):
    print(f"[{time.strftime('%H:%M:%S')}] Task {name} started")
    time.sleep(delay)
    print(f"[{time.strftime('%H:%M:%S')}] Task {name} finished")

def sequential_execution():
    print("\n=== Sequential Execution ===")
    start = time.time()
    task("A", 3)
    task("B", 2)
    task("C", 1)
    end = time.time()
    print(f"Total time (Sequential): {end - start:.2f} seconds")

def multithreaded_execution():
    print("\n=== Multithreaded Execution ===")
    start = time.time()
    threads = [
        threading.Thread(target=task, args=("A", 3)),
        threading.Thread(target=task, args=("B", 2)),
        threading.Thread(target=task, args=("C", 1)),
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    end = time.time()
    print(f"Total time (Multithreaded): {end - start:.2f} seconds")

sequential_execution()
multithreaded_execution()
