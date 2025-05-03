class Student:
    def __init__(self, name , grade , subject):
        self.name = name
        self.grade = grade
        self.subject = subject
    def introduce(self):
        return f"My name is {self.name}, i study {self.subject} and my grade is {self.grade}"
    
student1 = Student("Nugzari" , 10 , "Phyisics")
print(student1.introduce())