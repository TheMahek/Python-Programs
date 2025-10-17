import heapq

# ---- AVL Tree (Short) ----
class Node:
    def __init__(self, k): self.k, self.l, self.r, self.h = k, None, None, 1

def h(n): return n.h if n else 0
def bf(n): return h(n.l)-h(n.r)
def rotR(y):
    x=y.l; y.l=x.r; x.r=y
    y.h=max(h(y.l),h(y.r))+1; x.h=max(h(x.l),h(x.r))+1
    return x
def rotL(x):
    y=x.r; x.r=y.l; y.l=x
    x.h=max(h(x.l),h(x.r))+1; y.h=max(h(y.l),h(y.r))+1
    return y

def insert(r,k):
    if not r: return Node(k)
    if k<r.k: r.l=insert(r.l,k)
    else: r.r=insert(r.r,k)
    r.h=max(h(r.l),h(r.r))+1
    if bf(r)>1 and k<r.l.k: return rotR(r)
    if bf(r)<-1 and k>r.r.k: return rotL(r)
    if bf(r)>1 and k>r.l.k: r.l=rotL(r.l); return rotR(r)
    if bf(r)<-1 and k<r.r.k: r.r=rotR(r.r); return rotL(r)
    return r

def inorder(r):
    if r: inorder(r.l); print(r.k,end=" "); inorder(r.r)

# ---- Priority Queue (Heap) ----
pq=[]  # min-heap
heapq.heappush(pq,(3,"Low Job"))
heapq.heappush(pq,(10,"Emergency"))
heapq.heappush(pq,(5,"Normal"))

# ---- Demo ----
root=None
for x in [10,20,30,25,28]: root=insert(root,x)
print("AVL Inorder:",end=" "); inorder(root); print()
while pq: print("Handling:",heapq.heappop(pq))
