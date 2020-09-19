class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")
    
    def speak(self):
        print("I don't know what I say.")

class Dog(Pet):
    def speak(self):
        print("Bark")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and {self.color} color.")
    
pet1 = Pet("Tim",19)
pet1.show()
pet1.speak()
cat1 = Cat("Bill", 8, "yellow")
cat1.show()
cat1.speak()
dog1 = Dog("Jacky",10)
dog1.show()
dog1.speak()