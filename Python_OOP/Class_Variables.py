class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.number_of_people += 1

p1 = Person("Pera")
print(Person.number_of_people)

p2 = Person("Zika")
print(Person.number_of_people)

p3 = Person("Laza")
print(Person.number_of_people)