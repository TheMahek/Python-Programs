import threading
import time

def task(name,delay):
    print(f"[{time.strftime('%H:%M:%S')}]Task {name}sleeping for {delay}second")
    time.sleep(delay)
    print(f"[{time.strftime('%H:%M:%S')}]Task {name} finished")
    
def sequential_execution():
    print("\n===Sequential_excution===")
    start=time.time()
    task('A',3)
    task('B',2)
    task('C',1)
    end=time.time()
    print(f"Total time(Sequential):{end-start:2f}seconds")
    
def multithreaded_execution():
    print("\n===MultiThreaded_excution===")
    start=time.time()
    threads = [
        threading.Thread(target=task, args=("A",3),name="Thread-A"),
        threading.Thread(target=task, args=("B",2),name="Thread-B"),
        threading.Thread(target=task, args=("C",1),name="Thread-C"),
    ]
    
    for t in threads:
        t.start()
        
    for t in threads:
        t.join()
    end=time.time()
    print(f"Total time(MultiThreaded):{end-start:2f}seconds")
        

sequential_execution()    
multithreaded_execution()       
    