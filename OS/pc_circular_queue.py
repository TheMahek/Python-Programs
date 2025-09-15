import time
import random
import queue
import threading

BUFFER_SIZE = 5
buffer = queue.Queue(BUFFER_SIZE)
running = True
SENTINEL = None


def producer():
    global running
    while running:
        item = random.randint(1, 100)
        buffer.put(item)
        print(f"Produced: {item}")
        time.sleep(random.random())
    buffer.put(SENTINEL)


def consumer():
    while True:
        item = buffer.get()
        if item is SENTINEL:
            buffer.task_done()
            break
        print(f"Consumed: {item}")
        buffer.task_done()
        time.sleep(random.random())


if __name__ == "__main__":
    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)

    t1.start()
    t2.start()

    time.sleep(10)
    running = False

    t1.join()
    t2.join()

    print("Simulation Finished")