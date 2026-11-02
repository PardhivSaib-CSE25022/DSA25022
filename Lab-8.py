'''
class BinaryTree:
    def __init__(self, size):
        self.tree = [None] * size
        self.size = size

    def insert(self, value):
        for i in range(self.size):
            if self.tree[i] is None:
                self.tree[i] = value
                print(value, "inserted")
                return
        print("Tree is full")

    def search(self, value):
        for i in range(self.size):
            if self.tree[i] == value:
                print("Element found")
                return
        print("Element not found")

    def delete(self, value):
        for i in range(self.size):
            if self.tree[i] == value:
                last = -1

                for j in range(self.size - 1, -1, -1):
                    if self.tree[j] is not None:
                        last = j
                        break

                if last != -1:
                    self.tree[i] = self.tree[last]
                    self.tree[last] = None

                print(value, "deleted")
                return

        print("Element not found")

    def preorder(self, i=0):
        if i < self.size and self.tree[i] is not None:
            print(self.tree[i], end=" ")
            self.preorder(2 * i + 1)
            self.preorder(2 * i + 2)

    def inorder(self, i=0):
        if i < self.size and self.tree[i] is not None:
            self.inorder(2 * i + 1)
            print(self.tree[i], end=" ")
            self.inorder(2 * i + 2)

    def postorder(self, i=0):
        if i < self.size and self.tree[i] is not None:
            self.postorder(2 * i + 1)
            self.postorder(2 * i + 2)
            print(self.tree[i], end=" ")

    def display(self):
        print("Array:", self.tree)


bt = BinaryTree(10)

bt.insert(10)
bt.insert(20)
bt.insert(30)
bt.insert(40)
bt.insert(50)

bt.display()

print("Preorder:")
bt.preorder()

print("\nInorder:")
bt.inorder()

print("\nPostorder:")
bt.postorder()

print("\n")
bt.search(30)

bt.delete(20)
bt.display()
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            print(value, "inserted")
            return

        queue = [self.root]

        while queue:
            temp = queue.pop(0)

            if temp.left is None:
                temp.left = new_node
                print(value, "inserted")
                return
            else:
                queue.append(temp.left)

            if temp.right is None:
                temp.right = new_node
                print(value, "inserted")
                return
            else:
                queue.append(temp.right)

    def search(self, root, value):
        if root is None:
            return False

        if root.data == value:
            return True

        return (self.search(root.left, value) or
                self.search(root.right, value))

    def delete(self, value):
        if self.root is None:
            print("Tree is empty")
            return

        queue = [self.root]
        target = None
        last = None
        parent = None
        last_parent = None

        while queue:
            temp = queue.pop(0)

            if temp.data == value:
                target = temp

            if temp.left:
                last_parent = temp
                parent = temp
                queue.append(temp.left)

            if temp.right:
                last_parent = temp
                parent = temp
                queue.append(temp.right)

            last = temp

        if target is None:
            print("Element not found")
            return

        if last == self.root:
            self.root = None
        else:
            target.data = last.data

            if last_parent.left == last:
                last_parent.left = None
            else:
                last_parent.right = None

        print(value, "deleted")

    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

    def display(self):
        print("Level Order:", end=" ")
        if self.root is None:
            print("Tree is empty")
            return

        queue = [self.root]

        while queue:
            temp = queue.pop(0)
            print(temp.data, end=" ")

            if temp.left:
                queue.append(temp.left)

            if temp.right:
                queue.append(temp.right)


bt = BinaryTree()

bt.insert(10)
bt.insert(20)
bt.insert(30)
bt.insert(40)
bt.insert(50)

print("\nPreorder:")
bt.preorder(bt.root)

print("\nInorder:")
bt.inorder(bt.root)

print("\nPostorder:")
bt.postorder(bt.root)

print("\n")
bt.display()

print("\n\nSearching 30:")
if bt.search(bt.root, 30):
    print("Element found")
else:
    print("Element not found")

bt.delete(20)

print("After deletion:")
bt.display()
