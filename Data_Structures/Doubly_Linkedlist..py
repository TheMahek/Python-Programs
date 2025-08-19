# Node class
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

# Doubly Linked List class
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Insert at the beginning
    def insert_from_head(self, data):
        if not self.head:
            self.head = self.tail = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    # Insert at the end
    def insert_from_tail(self, data):
        if not self.tail:
            self.head = self.tail = Node(data)
        else:
            new_node = Node(data)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    # Insert at a specific position
    def insert_at_position(self, data, position):
        if position <= 0:
            self.insert_from_head(data)
        elif position >= self.size:
            self.insert_from_tail(data)
        else:
            new_node = Node(data)
            current = self.head
            for _ in range(position):
                current = current.next
            previous = current.prev
            previous.next = new_node
            new_node.prev = previous
            new_node.next = current
            current.prev = new_node
            self.size += 1

    # Insert values using sorted insertion
    def insert_sorted(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        elif data <= self.head.data:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        elif data >= self.tail.data:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            current = self.head
            while current and current.data < data:
                current = current.next
            prev_node = current.prev
            prev_node.next = new_node
            new_node.prev = prev_node
            new_node.next = current
            current.prev = new_node
        self.size += 1

    # Delete from beginning
    def delete_from_head(self):
        if self.head:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            self.size -= 1

    # Delete from end
    def delete_from_tail(self):
        if self.tail:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
            self.size -= 1

    # Delete from a specific position
    def delete_at_position(self, position):
        if self.size == 0:
            print("List is empty.")
            return
        if position <= 0:
            self.delete_from_head()
        elif position >= self.size - 1:
            self.delete_from_tail()
        else:
            temp = self.head
            for _ in range(position):
                temp = temp.next
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            self.size -= 1

    # Print list from head to tail
    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data, end=" ")
            cur = cur.next
        print()

    # Print list from tail to head
    def print_list_reverse(self):
        cur = self.tail
        while cur:
            print(cur.data, end=" ")
            cur = cur.prev
        print()

    # Traverse the list (same as print_list)
    def traverse(self):
        self.print_list()

# Main function
def main():
    dll = DoublyLinkedList()
    
    # Insert at head
    dll.insert_from_head(10)
    dll.insert_from_head(20)

    # Insert at tail
    dll.insert_from_tail(30)
    dll.insert_from_tail(40)

    print("Initial list:")
    dll.print_list()  # 20 10 30 40

    # Insert at middle (position 2)
    dll.insert_at_position(25, 2)
    print("List after inserting 25 at position 2:")
    dll.print_list()  # 20 10 25 30 40

    # Insert values using sorted insertion
    dll.insert_sorted(10)
    dll.insert_sorted(20)
    dll.insert_sorted(30)
    dll.insert_sorted(40)
    dll.insert_sorted(25)

    print("List after sorted insertions:")
    dll.print_list()  # Expected sorted list with duplicates

    # Delete node at position 2 (one of the 20s or 25s depending on the list)
    dll.delete_at_position(2)
    print("List after deleting from position 2:")
    dll.print_list()

    # Reverse print
    print("Reverse list:")
    dll.print_list_reverse()

# Run the main function
main()
