'''
class BST:
    def __init__(self, size):
        self.tree = [None] * size
        self.size = size

    def insert(self, value):
        i = 0

        while i < self.size:
            if self.tree[i] is None:
                self.tree[i] = value
                print(value, "inserted")
                return

            if value == self.tree[i]:
                print("Duplicate value")
                return

            if value < self.tree[i]:
                i = 2 * i + 1
            else:
                i = 2 * i + 2

        print("Tree is full")

    def search(self, value):
        i = 0

        while i < self.size and self.tree[i] is not None:
            if self.tree[i] == value:
                print("Element found")
                return

            if value < self.tree[i]:
                i = 2 * i + 1
            else:
                i = 2 * i + 2

        print("Element not found")

    def inorder(self, i=0):
        if i < self.size and self.tree[i] is not None:
            self.inorder(2 * i + 1)
            print(self.tree[i], end=" ")
            self.inorder(2 * i + 2)

    def preorder(self, i=0):
        if i < self.size and self.tree[i] is not None:
            print(self.tree[i], end=" ")
            self.preorder(2 * i + 1)
            self.preorder(2 * i + 2)

    def postorder(self, i=0):
        if i < self.size and self.tree[i] is not None:
            self.postorder(2 * i + 1)
            self.postorder(2 * i + 2)
            print(self.tree[i], end=" ")

    def delete(self, value):
        if not self.search_index(value):
            print("Element not found")
            return

        elements = []

        def collect(i):
            if i < self.size and self.tree[i] is not None:
                collect(2 * i + 1)
                if self.tree[i] != value:
                    elements.append(self.tree[i])
                collect(2 * i + 2)

        collect(0)

        self.tree = [None] * self.size

        for item in elements:
            self.insert(item)

        print(value, "deleted")

    def search_index(self, value):
        i = 0

        while i < self.size and self.tree[i] is not None:
            if self.tree[i] == value:
                return True
            if value < self.tree[i]:
                i = 2 * i + 1
            else:
                i = 2 * i + 2

        return False

    def display(self):
        print("Array representation:", self.tree)


bst = BST(15)

bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

bst.display()

print("Inorder:")
bst.inorder()

print("\nPreorder:")
bst.preorder()

print("\nPostorder:")
bst.postorder()

print("\n")
bst.search(40)

bst.delete(30)
bst.display()
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, value):
        if root is None:
            return Node(value)

        if value < root.data:
            root.left = self.insert(root.left, value)
        elif value > root.data:
            root.right = self.insert(root.right, value)

        return root

    def search(self, root, value):
        if root is None or root.data == value:
            return root

        if value < root.data:
            return self.search(root.left, value)

        return self.search(root.right, value)

    def find_min(self, root):
        while root.left:
            root = root.left
        return root

    def delete(self, root, value):
        if root is None:
            return None

        if value < root.data:
            root.left = self.delete(root.left, value)

        elif value > root.data:
            root.right = self.delete(root.right, value)

        else:
            if root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            temp = self.find_min(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)

        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

    def display(self):
        print("Inorder:", end=" ")
        self.inorder(self.root)
        print()


bst = BST()

values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    bst.root = bst.insert(bst.root, value)

print("Inorder Traversal:")
bst.inorder(bst.root)

print("\nPreorder Traversal:")
bst.preorder(bst.root)

print("\nPostorder Traversal:")
bst.postorder(bst.root)

print("\n")

if bst.search(bst.root, 40):
    print("Element found")
else:
    print("Element not found")

bst.root = bst.delete(bst.root, 30)

print("After deletion:")
bst.display()
