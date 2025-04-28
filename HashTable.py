from linked_list import SinglyLinkedList


class HashTable:
    def __init__(self, size = 10):
        self.size = size
        self.table = [SinglyLinkedList() for space in range(size)]

    def _hash(self, key) -> int:
        return hash(key) % self.size

    def insert(self, key, value):
        current_list = self.table[self._hash(key)]
        node = current_list.find(key, key=lambda pair: pair[0])
        if node:
            node.data = (key, value)
        else:
            current_list.insert((key, value))

    def search(self, key):
        current_list = self.table[self._hash(key)]
        node = current_list.find(key, key=lambda pair: pair[0])
        if node:
            return node.data[1]
        raise KeyError(f"Key '{key}' not found")

    def delete(self, key):
        index = self._hash(key)
        current_list = self.table[index]
        for i, (k, v) in enumerate(current_list):
            if k == key:
                current_list.delete(key, key=lambda pair: pair[0])
                return
        raise KeyError(f"Key '{key}' not found")

    def knuth(self, key, value):
        num_key = sum(ord(ch) for ch in key)
        return self.table[int(self.size * ((num_key * 0.6180339887 ) % 1))].append((key, value))


    def _XORhash(self,key, value):
        hashfunc = 0
        for ch in key:
            hashfunc ^= ord(ch) # se usa ^= pa usar el XOR, comparando uno a uno en binarios

        return hashfunc % self.size

    def PersonalicedHash(self, key, value):
        pass

    def __str__(self):
        return "\n".join(f"{i}: {list(bucket)}" for i, bucket in enumerate(self.table))