class Student:
    def __init__(self, name , age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def is_passing(self):
        if self.grade > 5:
            return True
        else:
            return False
student = Student("Gela" , "Genebashvili" , 4)
student.is_passing()
print(student.is_passing())