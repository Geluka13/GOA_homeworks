class Dog:
    def __init__(self, name , age):
        self.name = name
        self.age = age
    def mydog(self):
        return f"ჩემი ძაღლის სახელია {self.name} ის არის {self.age} წლის"

dog1 = Dog("რეზიკო" , 2)

print(dog1.mydog())