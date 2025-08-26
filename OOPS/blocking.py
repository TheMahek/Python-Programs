import multiprocessing
import time
import random
import queue  # For handling Empty/Full exceptions

def producer(queue_obj, n_items):
    for i in range(n_items):
        item = random.randint(1, 100)
        try:
            queue_obj.put(item)  #blocking put
            print(f"Produced: {item}")
        except queue.Full:
            print("Queue is full. Skipping item.")
        time.sleep(random.uniform(0.1, 0.5))

def consumer(queue_obj, n_items):
    consumed = 0
    while consumed < n_items:
        try:
            item = queue_obj.get()  # blocking get
            print(f"Consumed: {item}")
            consumed += 1
        except queue.Empty:
            print("Queue is empty. Waiting...")
            time.sleep(random.uniform(0.1, 0.5))

if __name__ == "__main__":
    N_ITEMS = 10
    q = multiprocessing.Queue(maxsize=5)

    p = multiprocessing.Process(target=producer, args=(q, N_ITEMS))
    c = multiprocessing.Process(target=consumer, args=(q, N_ITEMS))

    p.start()
    c.start()

    p.join()
    c.join()
