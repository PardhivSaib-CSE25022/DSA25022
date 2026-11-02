'''
class AVLTree:
    def __init__(self, size=100):
        self.nodes = [None] * size
        self.root = None
        self.size = size

    def height(self, i):
        if i is None:
            return 0
        return self.nodes[i]["height"]

    def balance(self, i):
        if i is None:
            return 0

        node = self.nodes[i]
        return self.height(node["left"]) - self.height(node["right"])

    def update_height(self, i):
        node = self.nodes[i]
        node["height"] = 1 + max(
            self.height(node["left"]),
            self.height(node["right"])
        )

    def allocate(self, value):
        for i in range(self.size):
            if self.nodes[i] is None:
                self.nodes[i] = {
                    "data": value,
                    "left": None,
                    "right": None,
                    "height": 1
                }
                return i

        raise OverflowError("Array is full")

    def right_rotate(self, y):
        x = self.nodes[y]["left"]
        t2 = self.nodes[x]["right"]

        self.nodes[x]["right"] = y
        self.nodes[y]["left"] = t2

        self.update_height(y)
        self.update_height(x)

        return x

    def left_rotate(self, x):
        y = self.nodes[x]["right"]
        t2 = self.nodes[y]["left"]

        self.nodes[y]["left"] = x
        self.nodes[x]["right"] = t2

        self.update_height(x)
        self.update_height(y)

        return y

    def rebalance(self, i):
        self.update_height(i)
        bf = self.balance(i)

        # LL Case
        if bf > 1 and self.balance(self.nodes[i]["left"]) >= 0:
            return self.right_rotate(i)

        # LR Case
        if bf > 1 and self.balance(self.nodes[i]["left"]) < 0:
            self.nodes[i]["left"] = self.left_rotate(
                self.nodes[i]["left"]
            )
            return self.right_rotate(i)

        # RR Case
        if bf < -1 and self.balance(self.nodes[i]["right"]) <= 0:
            return self.left_rotate(i)

        # RL Case
        if bf < -1 and self.balance(self.nodes[i]["right"]) > 0:
            self.nodes[i]["right"] = self.right_rotate(
                self.nodes[i]["right"]
            )
            return self.left_rotate(i)

        return i

    def insert_node(self, i, value):
        if i is None:
            return self.allocate(value)

        if value < self.nodes[i]["data"]:
            self.nodes[i]["left"] = self.insert_node(
                self.nodes[i]["left"], value
            )

        elif value > self.nodes[i]["data"]:
            self.nodes[i]["right"] = self.insert_node(
                self.nodes[i]["right"], value
            )

        else:
            print("Duplicate value")
            return i

        return self.rebalance(i)

    def insert(self, value):
        self.root = self.insert_node(self.root, value)
        print(value, "inserted")

    def search(self, i, value):
        if i is None:
            return False

        if self.nodes[i]["data"] == value:
            return True

        if value < self.nodes[i]["data"]:
            return self.search(self.nodes[i]["left"], value)

        return self.search(self.nodes[i]["right"], value)

    def find_min(self, i):
        while self.nodes[i]["left"] is not None:
            i = self.nodes[i]["left"]
        return i

    def delete_node(self, i, value):
        if i is None:
            return None

        if value < self.nodes[i]["data"]:
            self.nodes[i]["left"] = self.delete_node(
                self.nodes[i]["left"], value
            )

        elif value > self.nodes[i]["data"]:
            self.nodes[i]["right"] = self.delete_node(
                self.nodes[i]["right"], value
            )

        else:
            left = self.nodes[i]["left"]
            right = self.nodes[i]["right"]

            # Zero or one child
            if left is None or right is None:
                child = left if left is not None else right
                self.nodes[i] = None
                return child

            # Two children
            successor = self.find_min(right)
            self.nodes[i]["data"] = self.nodes[successor]["data"]

            self.nodes[i]["right"] = self.delete_node(
                right, self.nodes[successor]["data"]
            )

        return self.rebalance(i)

    def delete(self, value):
        if not self.search(self.root, value):
            print("Element not found")
            return

        self.root = self.delete_node(self.root, value)
        print(value, "deleted")

    def inorder(self, i):
        if i is not None:
            self.inorder(self.nodes[i]["left"])
            print(self.nodes[i]["data"], end=" ")
            self.inorder(self.nodes[i]["right"])

    def preorder(self, i):
        if i is not None:
            print(self.nodes[i]["data"], end=" ")
            self.preorder(self.nodes[i]["left"])
            self.preorder(self.nodes[i]["right"])

    def postorder(self, i):
        if i is not None:
            self.postorder(self.nodes[i]["left"])
            self.postorder(self.nodes[i]["right"])
            print(self.nodes[i]["data"], end=" ")

    def display(self):
        print("Array representation:")
        for i, node in enumerate(self.nodes):
            if node is not None:
                print(i, ":", node)


# Main program
avl = AVLTree()

values = [30, 20, 10, 25, 40, 50]

for value in values:
    avl.insert(value)

print("\nInorder:")
avl.inorder(avl.root)

print("\nPreorder:")
avl.preorder(avl.root)

print("\nPostorder:")
avl.postorder(avl.root)

print("\n")
if avl.search(avl.root, 25):
    print("Element found")
else:
    print("Element not found")

avl.delete(20)

print("\nAfter deletion:")
print("Inorder:")
avl.inorder(avl.root)

print("\n")
avl.display()
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:

    def height(self, root):
        if root is None:
            return 0
        return root.height

    def balance(self, root):
        if root is None:
            return 0

        return self.height(root.left) - self.height(root.right)

    def right_rotate(self, y):
        x = y.left
        t2 = x.right

        x.right = y
        y.left = t2

        y.height = 1 + max(
            self.height(y.left),
            self.height(y.right)
        )

        x.height = 1 + max(
            self.height(x.left),
            self.height(x.right)
        )

        return x

    def left_rotate(self, x):
        y = x.right
        t2 = y.left

        y.left = x
        x.right = t2

        x.height = 1 + max(
            self.height(x.left),
            self.height(x.right)
        )

        y.height = 1 + max(
            self.height(y.left),
            self.height(y.right)
        )

        return y

    def insert(self, root, value):

        if root is None:
            return Node(value)

        if value < root.data:
            root.left = self.insert(root.left, value)

        elif value > root.data:
            root.right = self.insert(root.right, value)

        else:
            return root

        root.height = 1 + max(
            self.height(root.left),
            self.height(root.right)
        )

        bf = self.balance(root)

        # LL Case
        if bf > 1 and value < root.left.data:
            return self.right_rotate(root)

        # RR Case
        if bf < -1 and value > root.right.data:
            return self.left_rotate(root)

        # LR Case
        if bf > 1 and value > root.left.data:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # RL Case
        if bf < -1 and value < root.right.data:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def search(self, root, value):
        if root is None or root.data == value:
            return root

        if value < root.data:
            return self.search(root.left, value)

        return self.search(root.right, value)

    def find_min(self, root):
        while root.left is not None:
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

        if root is None:
            return None

        root.height = 1 + max(
            self.height(root.left),
            self.height(root.right)
        )

        bf = self.balance(root)

        # LL Case
        if bf > 1 and self.balance(root.left) >= 0:
            return self.right_rotate(root)

        # LR Case
        if bf > 1 and self.balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # RR Case
        if bf < -1 and self.balance(root.right) <= 0:
            return self.left_rotate(root)

        # RL Case
        if bf < -1 and self.balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

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

    def display(self, root):
        print("Inorder:", end=" ")
        self.inorder(root)
        print()


# Main program
avl = AVLTree()
root = None

values = [30, 20, 10, 25, 40, 50]

for value in values:
    root = avl.insert(root, value)
    print(value, "inserted")

print("\nInorder:")
avl.inorder(root)

print("\nPreorder:")
avl.preorder(root)

print("\nPostorder:")
avl.postorder(root)

print("\n")

if avl.search(root, 25):
    print("Element found")
else:
    print("Element not found")

root = avl.delete(root, 20)

print("\nAfter deletion:")
avl.display(root)
