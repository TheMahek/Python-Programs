# Define the Node class to represent each element of the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to find the maximum and minimum values in the linked list
def find_max_min(head):
    if head is None:
        return None, None

    # Initialize max and min values with the data of the head node
    max_val = head.data
    min_val = head.data

    current = head.next

    while current:
        if current.data > max_val:
            max_val = current.data
        elif current.data < min_val:
            min_val = current.data
        current = current.next

    return max_val, min_val

# Example usage
head = Node(10)
head.next = Node(5)
head.next.next = Node(20)
head.next.next.next = Node(15)

max_val, min_val = find_max_min(head)

print("The Maximum value:", max_val)
print("The Minimum value:", min_val)
print("The Maximum - Minimum:", max_val - min_val)
