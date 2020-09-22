class Hash_Table:
    def __init__(self):
        self.MAX = 100
        self.array = [None for i in range(self.MAX)]

    def get_hash(self, key):
        x = 0
        for c in key:
            x = x + ord(c)
        return x % self.MAX
    
    def add_to_hashmap(self, key, value):
        h = self.get_hash(key)
        self.array[h]=value
    
    def get_value(self, key):
        h = self.get_hash(key)
        return self.array[h]



table1 = Hash_Table()
#print(table1.get_hash("march 6"))
table1.add_to_hashmap("march 6", 310.00)
table1.add_to_hashmap("march 7", 313.00)
table1.add_to_hashmap("march 8", 306.00)
table1.add_to_hashmap("march 9", 310.00)
#print(table1.array)
print(table1.get_value("march 8"))