class HashTable:
    def __init__(self, size = 10):
        self.size = size
        self.table = [[] for space in range(size)]

    def _hash(self, key) -> int:
        return hash(key) % self.size

    def insert(self, key, value):
        self.table[self._hash(key)].append((key, value))
        pass

    def search(self, key):
        return self.table[self._hash(key)]


    def delete(self, key):
        self.table[self._hash(key)] = []
        pass

    def knuth(self, key, value):
        self.table[int(self.size * ((key * 0.6180339887 ) % 1))].append((key, value))
        pass

    def _XORhash(self,key, value):
        hashfunc = 0
        for ch in key:
            pass
        pass

    def PersonalicedHash(self, key, value):
        pass

    def __str__(self):
        return f"{self.table}"



tabla = HashTable(10)
tabla.insert("perro", "dog")


print(tabla)


