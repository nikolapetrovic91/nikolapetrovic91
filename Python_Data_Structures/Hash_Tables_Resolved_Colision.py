class Hash_Table:
    def __init__(self):
        self.MAX = 10
        self.array = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        x = 0
        for c in key:
            x = x + ord(c)
        return x % self.MAX
    
    def add_to_hashmap(self, key, value):
        h = self.get_hash(key)
        for idx, element in enumerate(self.array[h]):
            if element[0] == key:
                self.array[h][idx] = (key,value)
                return
        self.array[h].append((key,value))
    
    def get_value(self, key):
        h = self.get_hash(key)
        for element in self.array[h]:
            if element[0] == key:
                return element[1]



table1 = Hash_Table()
table1.add_to_hashmap("march 6", 310.00)
table1.add_to_hashmap("march 6", 373.00)
table1.add_to_hashmap("march 7", 313.00)
table1.add_to_hashmap("march 8", 306.00)
table1.add_to_hashmap("march 9", 310.00)
table1.add_to_hashmap("march 17", 310.50)
table1.add_to_hashmap("march 17", 324.00)
print(table1.array)
print(table1.get_value("march 17"))