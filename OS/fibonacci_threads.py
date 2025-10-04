import threading
def fibonacci(n,name):
    a,b=0,1
    print(f"{name} generating {n} Fibonacci numbers:")
    for i in range(n):
        print(f"{name}:{a}")
        a,b=b,a+b
        
#Create thread for two fibonacci sequences
t1=threading.Thread(target=fibonacci,args=(5,"Thread-1"))
t2=threading.Thread(target=fibonacci,args=(7,"Thread-2"))
t1.start()
t2.start()
t1.join()
t1.join()
print("\n All Fibonacci threads finished:")

