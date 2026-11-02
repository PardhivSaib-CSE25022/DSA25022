'''
# Sttck implementation using Array

stack = []

# Push operation
def push(item):
    stack.append(item)
    print(item, "pushed into stack")

# Pop operation
def pop():
    if isempty():
        print("Stack Underflow")
    else:
        print("Popped element:", stack.pop())

# Peek operation
def peek():
    if isempty():
        print("Stack is empty")
    else:
        print("Top element:", stack[-1])

# Display operation
def display():
    if isempty():
        print("Stack is empty")
    else:
        print("Stack elements:", stack[::-1])

# IsEmpty operation
def isempty():
    return len(stack) == 0


# Main program
while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. IsEmpty")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = int(input("Enter element: "))
        push(item)

    elif choice == 2:
        pop()

    elif choice == 3:
        peek()

    elif choice == 4:
        display()

    elif choice == 5:
        print("Stack is empty" if isempty()
              else "Stack is not empty")

    elif choice == 6:
        break

    else:
        print("Invalid choice")

'''

# Stack implementation using Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    # Push operation
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        print(item, "pushed into stack")

    # Pop operation
    def pop(self):
        if self.isempty():
            print("Stack Underflow")
        else:
            print("Popped element:", self.top.data)
            self.top = self.top.next

    # Peek operation
    def peek(self):
        if self.isempty():
            print("Stack is empty")
        else:
            print("Top element:", self.top.data)

    # Display operation
    def display(self):
        if self.isempty():
            print("Stack is empty")
        else:
            temp = self.top
            print("Stack elements:", end=" ")
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
            print()

    # IsEmpty operation
    def isempty(self):
        return self.top is None


# Main program


s = Stack()

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. IsEmpty")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = int(input("Enter element: "))
        s.push(item)

    elif choice == 2:
        s.pop()

    elif choice == 3:
        s.peek()

    elif choice == 4:
        s.display()

    elif choice == 5:
        print("Stack is empty" if s.isempty()
              else "Stack is not empty")

    elif choice == 6:
        break

    else:
        print("Invalid choice")

