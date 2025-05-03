class Cat:
    def __init__(self, name):
        self.name = name

    def meow(self):
        print(f"{self.name} Meow!")

class Dog(Cat):
    def __init__(self, name, breed):
        super().__init__(name) 
        self.breed = breed

    def bark(self):
        print(f"{self.name} ({self.breed}) Woof!")


cat = Cat("თუთუ")
dog = Dog("ბობი", "ლაბრადორი")

print("კატა:")
cat.meow()

print("\nძაღლი:")
dog.bark()

print("\nძაღლს ასევე შეუძლია კნავილიც:")
dog.meow()