class Queue:
    def __init__(self):
        self.queue = []

    # Enqueue - Add element
    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")

    # Dequeue - Remove element
    def dequeue(self):
        if not self.is_empty():
            removed = self.queue.pop(0)
            print(f"Dequeued: {removed}")
            return removed
        else:
            print("Queue is empty!")

    # Peek - Show front element
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            print("Queue is empty!")

    # Check if queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Display the queue
    def display(self):
        print("Queue:", self.queue)


# Example usage
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
q.dequeue()
q.display()
print("Front element:", q.peek())
