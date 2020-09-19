class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print("bark")
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def set_age(self, age):
        self.age = age

dog1 = Dog("Tim", 8)
dog2 = Dog("Bill", 9)
print(dog1.get_name())
print(dog1.get_age())
dog1.bark()
print(dog2.get_name())
print(dog2.get_age())
dog2.bark()
dog1.set_age(34)
print(f"Tim's age revised: {dog1.get_age()}")