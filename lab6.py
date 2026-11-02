'''
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(item, "inserted")

    def dequeue(self):
        if not self.queue:
            print("Queue is empty")
        else:
            print(self.queue.pop(0), "removed")

    def peek(self):
        if not self.queue:
            print("Queue is empty")
        else:
            print("Front element:", self.queue[0])

    def display(self):
        print("Queue:", self.queue)


q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
q.peek()
q.dequeue()
q.display()
'''
'''
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, item):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full")
            return

        if self.front == -1:
            self.front = 0

        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item
        print(item, "inserted")

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty")
            return

        print(self.queue[self.front], "removed")

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

    def peek(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            print("Front:", self.queue[self.front])

    def display(self):
        if self.front == -1:
            print("Queue is empty")
            return

        i = self.front
        print("Queue:", end=" ")

        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size

        print()


q = CircularQueue(5)

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.dequeue()
q.enqueue(40)
q.enqueue(50)
q.enqueue(60)
q.display()
q.peek()
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, item):
        new_node = Node(item)

        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        print(item, "inserted")

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
        else:
            print(self.front.data, "removed")
            self.front = self.front.next

            if self.front is None:
                self.rear = None

    def peek(self):
        if self.front is None:
            print("Queue is empty")
        else:
            print("Front element:", self.front.data)

    def display(self):
        temp = self.front

        if temp is None:
            print("Queue is empty")
            return

        print("Queue:", end=" ")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
q.peek()
q.dequeue()
q.display()
