class Stack:
    def __init__(self):
        # Initialize an empty list to store stack elements
        self.items = []

    def push(self, item):
        # Push an item onto the stack by appending it to the list
        self.items.append(item)

    def pop(self):
        # Pop an item from the stack if it's not empty, otherwise, raise an error
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Pop from an empty stack")

    def print_stack(self):
        # Print the elements of the stack
        print(self.items)

    def size(self):
        # Return the size (number of elements) of the stack
        return len(self.items)

    def top(self):
        # Return the top item of the stack if it's not empty, otherwise, return None
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        # Check if the stack is empty
        return len(self.items) == 0

# Create a stack
stack = Stack()

while True:
    print("\nOptions:")
    print("1. Push an item")
    print("2. Pop an item")
    print("3. Print the stack")
    print("4. Check the size of the stack")
    print("5. Check the top item")
    print("6. Check if the stack is empty")
    print("7. Quit")

    choice = input("Enter your choice (1/2/3/4/5/6/7): ")

    if choice == '1':
        item = input("Enter the item to push: ")
        stack.push(item)
        print(f"{item} has been pushed onto the stack.")
    elif choice == '2':
        if not stack.is_empty():
            popped_item = stack.pop()
            print(f"Popped item: {popped_item}")
        else:
            print("Stack is empty. Cannot pop.")
    elif choice == '3':
        stack.print_stack()
    elif choice == '4':
        print(f"Size of stack: {stack.size()}")
    elif choice == '5':
        top_item = stack.top()
        if top_item is not None:
            print(f"Top item: {top_item}")
        else:
            print("Stack is empty.")
    elif choice == '6':
        if stack.is_empty():
            print("Stack is empty.")
        else:
            print("Stack is not empty.")
    elif choice == '7':
        break
    else:
        print("Invalid choice. Please select a valid option.")
