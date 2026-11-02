'''
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for i in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)

        if key not in self.table[index]:
            self.table[index].append(key)
            print(key, "inserted")
        else:
            print("Duplicate key")

    def search(self, key):
        index = self.hash_function(key)

        if key in self.table[index]:
            print("Element found")
        else:
            print("Element not found")

    def delete(self, key):
        index = self.hash_function(key)

        if key in self.table[index]:
            self.table[index].remove(key)
            print(key, "deleted")
        else:
            print("Element not found")

    def display(self):
        for i in range(self.size):
            print(i, ":", self.table[i])


# Main program
ht = HashTable(7)

ht.insert(10)
ht.insert(20)
ht.insert(15)
ht.insert(25)
ht.insert(30)

print("\nHash Table:")
ht.display()

print("\nSearching:")
ht.search(25)

print("\nDeleting:")
ht.delete(20)

print("\nUpdated Hash Table:")
ht.display()
'''
'''
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)

        for i in range(self.size):
            new_index = (index + i) % self.size

            if self.table[new_index] is None:
                self.table[new_index] = key
                print(key, "inserted at index", new_index)
                return

            if self.table[new_index] == key:
                print("Duplicate key")
                return

        print("Hash table is full")

    def search(self, key):
        index = self.hash_function(key)

        for i in range(self.size):
            new_index = (index + i) % self.size

            if self.table[new_index] is None:
                print("Element not found")
                return

            if self.table[new_index] == key:
                print("Element found at index", new_index)
                return

        print("Element not found")

    def delete(self, key):
        index = self.hash_function(key)

        for i in range(self.size):
            new_index = (index + i) % self.size

            if self.table[new_index] is None:
                print("Element not found")
                return

            if self.table[new_index] == key:
                self.table[new_index] = "DELETED"
                print(key, "deleted")
                return

        print("Element not found")

    def display(self):
        for i in range(self.size):
            print(i, ":", self.table[i])


# Main program
ht = HashTable(7)

ht.insert(10)
ht.insert(20)
ht.insert(15)
ht.insert(25)
ht.insert(30)

print("\nHash Table:")
ht.display()

print("\nSearching:")
ht.search(25)

print("\nDeleting:")
ht.delete(20)

print("\nUpdated Hash Table:")
ht.display()
'''

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)

        for i in range(self.size):
            new_index = (index + i * i) % self.size

            if self.table[new_index] is None:
                self.table[new_index] = key
                print(key, "inserted at index", new_index)
                return

            if self.table[new_index] == key:
                print("Duplicate key")
                return

        print("No available position found")

    def search(self, key):
        index = self.hash_function(key)

        for i in range(self.size):
            new_index = (index + i * i) % self.size

            if self.table[new_index] is None:
                print("Element not found")
                return

            if self.table[new_index] == key:
                print("Element found at index", new_index)
                return

        print("Element not found")

    def delete(self, key):
        index = self.hash_function(key)

        for i in range(self.size):
            new_index = (index + i * i) % self.size

            if self.table[new_index] is None:
                print("Element not found")
                return

            if self.table[new_index] == key:
                self.table[new_index] = "DELETED"
                print(key, "deleted")
                return

        print("Element not found")

    def display(self):
        for i in range(self.size):
            print(i, ":", self.table[i])


# Main program
ht = HashTable(7)

ht.insert(10)
ht.insert(20)
ht.insert(15)
ht.insert(25)
ht.insert(30)

print("\nHash Table:")
ht.display()

print("\nSearching:")
ht.search(25)

print("\nDeleting:")
ht.delete(20)

print("\nUpdated Hash Table:")
ht.display()
