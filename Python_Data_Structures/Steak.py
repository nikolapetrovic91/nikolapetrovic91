from collections import deque

class Steak:
    def __init__(self):
        self.container = deque()
    def push(self, val):
        self.container.append(val)
    def pop(self):
        self.container.pop()
    def peek(self):
        return self.container[-1]
    def size(self):
        return len(self.container)


s1 = Steak()
s1.push(1)
s1.push(2)
s1.push(3)
s1.push(4)
s1.push(5)
print(s1.container)
print(f"the length is {s1.size()}")
s1.pop()
print(s1.container)