# Node class for SLL
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class to manage tasks
class TaskList:
    def __init__(self):
        self.head = None

    def add_task(self, task):
        """Add a new task to the end of the list"""
        new_node = Node(task)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def remove_task(self, task):
        """Remove the first occurrence of a task without using prev"""
        if self.head is None:
            return False  # list is empty

        if self.head.data == task:
            self.head = self.head.next  # Remove head Node
            return True

        curr = self.head
        while curr.next:
            if curr.next.data == task:
                curr.next = curr.next.next  # Bypass the value
                return True
            curr = curr.next
        return False  # task not found

    def display_tasks(self):
        """Display all tasks in the list"""
        if not self.head:
            print("Task list is Empty.")
            return

        print("Task List:")
        curr = self.head
        while curr:
            print("-", curr.data)
            curr = curr.next

    def search_task(self, keyword):
        """Search for a task in the list"""
        curr = self.head
        found = False
        keyword = keyword.lower()
        while curr:
            if keyword in curr.data.lower():
                print(f"Found: {curr.data}")
                found = True
            curr = curr.next
        if not found:
            print("Task not found in the list")


# Create a task list
todo = TaskList()

# Add Tasks
todo.add_task("Buy Milk")
todo.add_task("Practice coding")
todo.add_task("Complete Assignment")
todo.add_task("Do Project")

# Display tasks
todo.display_tasks()

# Remove a task
print("\nRemoving a task 'Buy Milk':")
todo.remove_task("Buy Milk")

# Display Updated list
todo.display_tasks()

# Search for a task
print("\nSearching for a task 'Project':")
todo.search_task("Project")
