class Hashtable:
    def __init__(self, size):
        self.size = size
        self.data = [None] * self.size
        
    def __str__(self):
        return str(self.__dict__)
    
    def _hash(self, key):
        hash = 0
        for i in range(0, len(key)):
            hash = (hash + ord(key[i]) * i) % len(self.data)
        return hash
    
    def get(self, key):
        hash = self._hash(key)
        if self.data[hash]:
            for i in range(len(self.data[hash])):
                if self.data[hash][i][0] == key:
                    return self.data[hash][i][1]
        return None
    def set(self, key, value):
        hash = self._hash(key)
        if not self.data[hash]:
            self.data[hash] = [[key, value]]
        else:
            self.data[hash].append([key, value])
        
        print(self.data)
    
    def keys(self):
        keys_list = []
        for i in range(self.size):
            if self.data[i]:
                if len(self.data[i] > 1):
                    for j in range(self.data[i]):
                        keys_list.append(self.data[i][j][0])
                else:
                    keys_list.append(self.data[0][0][0])
        return keys_list
    
    def values(self):
        values_list = []
        for i in range(self.size):
            if self.data[i]:
                if len(self.data[i] > 1):
                    for j in range(self.data[i]):
                        values_list.append(self.data[i][j][1])
                else:
                    values_list.append(self.data[0][0][1])
        return values_list
    
# hash = Hashtable(5)
# hash.set("pig", 2)
# hash.set("dog", 4)
# hash.set("snake", 1)
# hash.set("cow", 3)
# hash.set("owl", 5)
# hash.set("donkey", 6)
# print(hash.get("owl"))