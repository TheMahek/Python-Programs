import threading
import time

# Shared Memory variable
CAPACITY = 10
buffer = [-1 for _ in range(CAPACITY)]
in_index = 0
out_index = 0

# Declaring Semaphores
mutex = threading.Semaphore(1)  # Only 1 thread can access the buffer at a time
empty = threading.Semaphore(CAPACITY)  # Initially, all slots are empty
full = threading.Semaphore(0)  # No slots are full initially

counter = 0

# Producer Thread Class
class Producer(threading.Thread):
    def run(self):
        global CAPACITY, buffer, in_index, counter, mutex, empty, full

        items_produced = 0
        while items_produced < 20:
            empty.acquire()
            mutex.acquire()

            counter += 1
            buffer[in_index] = counter
            print("Producer produced:", counter)
            in_index = (in_index + 1) % CAPACITY

            mutex.release()
            full.release()

            time.sleep(1)
            items_produced += 1

# Consumer Thread Class
class Consumer(threading.Thread):
    def run(self):
        global CAPACITY, buffer, out_index, mutex, empty, full

        items_consumed = 0
        while items_consumed < 20:
            full.acquire()
            mutex.acquire()

            item = buffer[out_index]
            print("Consumer consumed item:", item)
            out_index = (out_index + 1) % CAPACITY

            mutex.release()
            empty.release()

            time.sleep(2.5)
            items_consumed += 1

# Creating Threads
producer = Producer()
consumer = Consumer()

# Starting Threads
producer.start()
consumer.start()

# Waiting for threads to complete
producer.join()
consumer.join()