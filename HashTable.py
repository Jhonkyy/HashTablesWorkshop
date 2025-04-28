import random

from linked_list import SinglyLinkedList


class HashTable:

    def __init__(self, size=10, hash_type='knuth'):
        self.size = size
        self.table = [SinglyLinkedList() for _ in range(size)]
        self.hash_type = hash_type

    def _hash(self, key):
        if self.hash_type == 'knuth':
            return self.knuth_hash(key)
        elif self.hash_type == 'xor':
            return self.xor_hash(key)
        elif self.hash_type == 'personalized':
            return self.personalized_hash(key)
        else:
            # Función hash por defecto de Python módulo tamaño
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
        return None

    def delete(self, key):
        index = self._hash(key)
        current_list = self.table[index]
        for i, (k, v) in enumerate(current_list):
            if k == key:
                current_list.delete(key, key=lambda pair: pair[0])
                return
        raise KeyError(f"Key '{key}' not found")

    def knuth_hash(self, key):
        num_key = sum(ord(ch) for ch in key)
        return int(self.size * ((num_key * 0.6180339887) % 1))


    def xor_hash(self,key):
        hashfunc = 0
        for ch in key:
            hashfunc ^= ord(ch) # se usa ^= pa usar el XOR, comparando uno a uno en binarios acumulando el ASCII de cada caracter
        return hashfunc % self.size

    def personalized_hash(self, key):
        encoded_key = key.encode()
        value = 0
        for ch in encoded_key:
            value += ch
        value *= 401
        return value % self.size

    def my_personal(self,key):
        encoded_key = key.encode()
        value = 0
        value_2 = 0
        for ch in encoded_key:
            value += ch
            value_2 ^= ch
        value = int(value_2 // (70/ self.size))
        return value % self.size

    def __str__(self):
        return "\n".join(f"{i}: {list(bucket)}" for i, bucket in enumerate(self.table))

def find_duplicated(arr):
    duplicated = []
    table = HashTable()
    for item in arr:
        if table.search(item) is not None:
            if item not in duplicated:
                duplicated.append(item)
        else:
            table.insert(item, f"{item}")
    return duplicated

def count_frequency(arr):
    frequency_table = HashTable()
    for item in arr:
        if frequency_table.search(item) is not None:
            count = frequency_table.search(item)
            frequency_table.insert(item, count + 1)
        else:
            frequency_table.insert(item, 1)
    return frequency_table

if __name__ == "__main__":
    #Prueba Hash table
    tabla = HashTable(10)


    tabla.insert("perro", "dog")
    tabla.insert("gato", "cat")
    tabla.insert("pajaro", "bird")

    tabla.delete("gato")


    print(tabla)

    print("---Prueba ejercicios duplicados y frecuencia---\n")

    #Prueba ejercicios duplicados y frecuencia
    arr = ["manzana", "pera", "banana", "manzana", "pera", "pera", "kiwi", "banana", "banana"]

    print("Lista original:")
    print(arr)

    # Encontrar duplicados
    duplicados = find_duplicated(arr)
    print("\nDuplicados encontrados:")
    print(duplicados)

    # Contar frecuencia
    frecuencias = count_frequency(arr)
    print("\nFrecuencia de cada elemento:")
    print(frecuencias)