class HashTable:
    def __init__(self):
        self.size = 25
        self.table = [None] * self.size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for item in self.table[index]:
                if item[0] == key:
                    item = (key, value)
                    return
            self.table[index].append((key, value))

    def delete(self, key):
        index = self._hash(key)
        if self.table[index] is None:
            return
        for i, item in enumerate(self.table[index]):
            if item[0] == key:
                del self.table[index][i]
                return

    def search(self, key):
        index = self._hash(key)
        if self.table[index] is None:
            return None
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        return None
    

hash_table = HashTable()

hash_table.insert("key1", "value1")
hash_table.insert("key2", "value2")
hash_table.insert("key3", "value3")

hash_table.delete("key2")

value = hash_table.search("key")
print(value)
# print(hash_table._hash(1))
