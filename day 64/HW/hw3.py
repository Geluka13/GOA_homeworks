class Dog:
    def __init__(self, name , age):
        self.name = name
        self.age = age
    def dog_name_age(self):
        return f"{self.name} , {self.age}"
    def bark(self):
        return "Woof!"
dog = Dog("Gocha" , 2)
print(dog.dog_name_age())
print(dog.bark())