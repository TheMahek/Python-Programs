from concurrent.futures import ThreadPoolExecutor

def fibonacci_list(n):
    seq = []
    a,b = 0,1
    
    for i in range(n):
        seq.append(a)
        a,b = b,a+b
    return seq

# Thread pool with 3 Workers

with ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(fibonacci_list, [5,7,10]))    
    
for i, seq in enumerate(results,1):
    print(f"Task {i} is: {seq}")


