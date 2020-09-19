class Student:
    def __init__(self, name, age, avg_grade):
        self.name = name
        self.age = age
        self.avg_grade = avg_grade

    def get_grade(self):
        return self.avg_grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_students(self):
        return self.students
    
    def course_average_grade(self):
        average_grade = 0
        for student in self.students:
            average_grade += student.get_grade()
        return average_grade / len(self.students)


s1 = Student("Tim", 17, 75)
s2 = Student("Bill", 18, 80)
s3 = Student("Jill", 19, 90)
course1 = Course("Mathematics", 2)
course1.add_student(s1)
print(course1.get_students()[0].get_grade())
print(f"Average grade on the course is {course1.course_average_grade()}")