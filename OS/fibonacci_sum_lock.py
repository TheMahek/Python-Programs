import threading
lock = threading.Lock()
shared_sum = 0
def add_fibonacci_sum(n):
    global shared_sum
    a,b = 0,1
    for i in range(n):
        with lock:  #ensure only one thread updates at a time
            shared_sum += a
        a, b = b, a + b 
threads = []

for i in range(3):
    t = threading.Thread(target=add_fibonacci_sum, args=(5,))
    threads.append(t)
    t.start()
for t in threads:
    t.join()
print("Total sum of Fibonacci numbers(shared:)",shared_sum)            
