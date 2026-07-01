class Student:

    class_year = 2026
    num_students = 0

    def __init__(self,name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        Student.num_students += 1


student1 = Student("Sami", 20, "A")


print(student1.name)
print(Student.class_year)
print(Student.num_students)