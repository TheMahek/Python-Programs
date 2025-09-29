import threading
import time

# Shared Memory Variables
CAPACITY = 10
buffer = [-1 for _ in range(CAPACITY)]
in_index = 0
out_index = 0

# Declaring Semaphores
mutex = threading.Semaphore(1)   # Only 1 thread (producer/consumer) at a time
empty = threading.Semaphore(CAPACITY)  # Number of empty slots
full = threading.Semaphore(0)          # Number of filled slots

# Producer Thread Class
class Producer(threading.Thread):
    def run(self):
        global CAPACITY, buffer, in_index
        global mutex, empty, full
        items_produced = 0
        counter = 0

        while items_produced < 20:
            empty.acquire()      # Wait for empty slot
            mutex.acquire()      # Lock critical section
            counter += 1
            buffer[in_index] = counter
            in_index = (in_index + 1) % CAPACITY
            print("Producer Produced:", counter)
            mutex.release()      # Unlock
            full.release()       # Signal item added
            time.sleep(1)
            items_produced += 1


# Consumer Thread Class
class Consumer(threading.Thread):
    def run(self):
        global CAPACITY, buffer, out_index
        global mutex, empty, full
        items_consumed = 0

        while items_consumed < 20:
            full.acquire()       # Wait for full slot
            mutex.acquire()      # Lock critical section

            item = buffer[out_index]
            out_index = (out_index + 1) % CAPACITY
            print("Consumer Consumed:", item)

            mutex.release()      # Unlock
            empty.release()      # Signal empty slot available
            time.sleep(2.5)
            items_consumed += 1

# Create Threads
producer = Producer()
consumer = Consumer()

# Start Threads
consumer.start()
producer.start()

# Wait for Threads to Finish
producer.join()
consumer.join()


