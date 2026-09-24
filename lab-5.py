class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # 1. Create a circular linked list
    def create(self):
        n = int(input("Enter number of nodes: "))

        for i in range(n):
            data = int(input("Enter value: "))
            new_node = Node(data)

            if self.head is None:
                self.head = new_node
                new_node.next = self.head
            else:
                temp = self.head

                while temp.next != self.head:
                    temp = temp.next

                temp.next = new_node
                new_node.next = self.head

    # 2. Insert at beginning
    def insert_beginning(self):
        data = int(input("Enter value: "))
        new_node = Node(data)

        # Empty list
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        # Find last node
        temp = self.head

        while temp.next != self.head:
            temp = temp.next

        new_node.next = self.head
        temp.next = new_node
        self.head = new_node

    # 3. Insert at end
    def insert_end(self):
        data = int(input("Enter value: "))
        new_node = Node(data)

        # Empty list
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        # Find last node
        temp = self.head

        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

    # 4. Insert at a specific index
    def insert_index(self):
        data = int(input("Enter value: "))
        index = int(input("Enter index: "))

        new_node = Node(data)

        # Insert at beginning
        if index == 0:
            if self.head is None:
                self.head = new_node
                new_node.next = self.head
                return

            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            new_node.next = self.head
            temp.next = new_node
            self.head = new_node
            return

        # Empty list
        if self.head is None:
            print("Invalid index")
            return

        temp = self.head
        count = 0

        # Move to node before required index
        while count < index - 1:
            temp = temp.next
            count += 1

            if temp == self.head:
                print("Invalid index")
                return

        new_node.next = temp.next
        temp.next = new_node

    # 5. Delete at a specific index
    def delete_index(self):
        index = int(input("Enter index to delete: "))

        if self.head is None:
            print("List is empty")
            return

        # Delete first node
        if index == 0:
            self.delete_first()
            return

        temp = self.head
        count = 0

        # Find node before the node to delete
        while count < index - 1:
            temp = temp.next
            count += 1

            if temp == self.head:
                print("Invalid index")
                return

        # If next node is head, index is invalid
        if temp.next == self.head:
            print("Invalid index")
            return

        temp.next = temp.next.next

    # 6. Delete first node
    def delete_first(self):
        if self.head is None:
            print("List is empty")
            return

        # Only one node
        if self.head.next == self.head:
            self.head = None
            return

        # Find last node
        temp = self.head

        while temp.next != self.head:
            temp = temp.next

        temp.next = self.head.next
        self.head = self.head.next

    # 7. Delete last node
    def delete_last(self):
        if self.head is None:
            print("List is empty")
            return

        # Only one node
        if self.head.next == self.head:
            self.head = None
            return

        temp = self.head

        # Find second-last node
        while temp.next.next != self.head:
            temp = temp.next

        temp.next = self.head

    # 8. Count number of nodes
    def count_nodes(self):
        if self.head is None:
            print("Number of nodes: 0")
            return

        count = 0
        temp = self.head

        while True:
            count += 1
            temp = temp.next

            if temp == self.head:
                break

        print("Number of nodes:", count)

    # 9. Display / Traverse
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while True:
            print(temp.data, end=" -> ")
            temp = temp.next

            if temp == self.head:
                break

        print("(head)")


# Main program
circular_list = CircularLinkedList()

while True:
    print("\n----- CIRCULAR LINKED LIST -----")
    print("1. Create a circular linked list")
    print("2. Insert at beginning")
    print("3. Insert at end")
    print("4. Insert at a specific index")
    print("5. Delete at a specific index")
    print("6. Delete first node")
    print("7. Delete last node")
    print("8. Count number of nodes")
    print("9. Display / Traverse")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        circular_list.create()

    elif choice == 2:
        circular_list.insert_beginning()

    elif choice == 3:
        circular_list.insert_end()

    elif choice == 4:
        circular_list.insert_index()

    elif choice == 5:
        circular_list.delete_index()

    elif choice == 6:
        circular_list.delete_first()

    elif choice == 7:
        circular_list.delete_last()

    elif choice == 8:
        circular_list.count_nodes()

    elif choice == 9:
        circular_list.display()

    elif choice == 10:
        print("Exiting...")
        break

    else:
        print("Invalid choice")
