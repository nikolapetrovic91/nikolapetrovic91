class Student:
    number_of_students = 0

    def __init__(self, name):
        self.name = name
        Student.add_person()

    @classmethod
    def get_number_of_students(cls):
        return cls.number_of_students
    
    @classmethod
    def add_person(cls):
        cls.number_of_students += 1

s1 = Student("Nikola")
s2 = Student("Mladen")
print(Student.get_number_of_students())        