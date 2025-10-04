import threading 
import time 
import random 
 
BUFFER_SIZE = 5 
buffer = [] 
mutex = threading.Lock() 
empty = threading.Semaphore(BUFFER_SIZE) 
full = threading.Semaphore(0) 
running = True    #Stop Flag

def producer(): 
    global running 
    while running: 
        item = random.randint(1, 100) 
        empty.acquire() 
        with mutex: 
            buffer.append(item) 
            print(f"Produced: {item}, Buffer: {buffer}") 
        full.release() 
        time.sleep(random.random())   
 
def consumer(): 
    global running 
    while running: 
        full.acquire() 
        with mutex: 
            if buffer: 
                item = buffer.pop(0) 
                print(f"Consumed: {item}, Buffer: {buffer}") 
            empty.release() 
        time.sleep(random.random())   
 
if __name__ == "__main__": 
    t1 = threading.Thread(target=producer) 
    t2 = threading.Thread(target=consumer) 
    t1.start() 
    t2.start() 
    time.sleep(10) 
    running = False 
    empty.release() 
    full.release() 
    t1.join() 
t2.join() 
print("Simulation Finished") 
