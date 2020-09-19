class Parent1:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def func1(self):
        print("I am a function 1.")

class Parent2:
    def __init__(self, name, surname, profession):
        self.name = name
        self.surname = surname
        self.profession = profession

    def func2(self):
        print("I am a function 2.")

class Child(Parent1, Parent2):
    def __init__(self, name, surname, age, profession):
        Parent1.__init__(self, name, surname, age)
        Parent2.__init__(self, name, surname, profession)

ch1 = Child("Jovan","Jovanovic", 18, "Lawyer")
ch1.func1()
ch1.func2()
print(ch1.name, ch1.surname, ch1.age, ch1.profession)