import threading
import time
import random

# Semaphores
mutex = threading.Semaphore(1)         # Protects rc (read count)
db = threading.Semaphore(1)            # Controls access to shared data
serviceQueue = threading.Semaphore(1)  # Fairness: queue for both readers/writers
# Shared resource and counters
shared_data = 0
rc = 0
running = True  # Stop flag

def reader(reader_id):
    global rc, shared_data, running
    while running:
        # Fairness: wait in queue
        serviceQueue.acquire()
        mutex.acquire()
        rc += 1
        if rc == 1:
            db.acquire()  # First reader locks db
        mutex.release()
        serviceQueue.release()

        # Critical section
        print(f"[Reader] {reader_id} reads {shared_data}")
        time.sleep(random.uniform(0.2, 0.5))
        # Exit section
        mutex.acquire()
        rc -= 1
        if rc == 0:
            db.release()  # Last reader unlocks db
        mutex.release()
        time.sleep(random.uniform(0.5, 1.0))

def writer(writer_id):
    global shared_data, running
    while running:
        # Fairness: wait in queue
        serviceQueue.acquire()
        db.acquire()   # Exclusive access
        serviceQueue.release()

        # Critical section
        shared_data += 1
        print(f"[Writer] {writer_id} writes {shared_data}")
        time.sleep(random.uniform(0.3, 0.6))
        db.release()
time.sleep(random.uniform(0.8, 1.5))

if __name__ == "__main__":
    readers = [threading.Thread(target=reader, args=(i,)) for i in range(3)]
    writers = [threading.Thread(target=writer, args=(i,)) for i in range(2)]

    for t in readers + writers:
        t.start()
    time.sleep(10)   # Run simulation for 10 sec
    running = False  # Stop all threads
    for t in readers + writers:
        t.join()
    print("Simulation finished.")
