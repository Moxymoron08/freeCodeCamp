class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, parameter):
        key = 0
        for i in parameter:
            key += ord(i) 
        return key
    
    def add(self, key, value):
        hash_val = self.hash(key)
        if hash_val not in self.collection:
            self.collection[hash_val] = {key:value}
        else :
            self.collection[hash_val][key] = value 

    def remove(self, key):
        hash_val = self.hash(key)
        if hash_val in self.collection:
            if key in self.collection[hash_val]:
                if len(self.collection[hash_val]) < 2:
                    del self.collection[hash_val]
                else:
                    del self.collection[hash_val][key]
        return

    def lookup(self, key):
        hash_val = self.hash(key)
        if hash_val in self.collection:
            if key in self.collection[hash_val]:
                return self.collection[hash_val][key]
        return None

