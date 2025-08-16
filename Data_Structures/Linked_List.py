class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self,data):
        self.head = None
        self.data = None

    def insert(self,newnode):
        if self.head is None:
            self.head = newnode
        else:
            lastnode = self.head
            while lastnode.next is not None:
                lastnode = lastnode.next
            lastnode.next = newnode

    def delete(self,value):
        current = self.head
        previous = None

        if current is not None and current.data == value:
            self.head = current.next
            current = None
            return
        
        while current is not None and current.data != value:
            previous = current
            current = current.next


        if current is None:
            print("Value not found in the List")
            return
        
        previous.next = current.next 
        current = None

    def printlist(self):
        currentnode = self.head
        while currentnode is not None:
            print(currentnode.data)
            currentnode = currentnode.next 


fnode = Node(1)
snode = Node(2)
tnode = Node(3)

LinkedList = LinkedList(None)

LinkedList.insert(fnode)
LinkedList.insert(snode)
LinkedList.insert(tnode)

print("List Before Deletion: ")
LinkedList.printlist()

LinkedList.delete(2)

print("List after deleting Value 2: ")
LinkedList.printlist()

