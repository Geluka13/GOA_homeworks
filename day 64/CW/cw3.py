class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def print_name_and_surname(self):
        print(f"მე მქვია {self.name}, ჩემი გვარია {self.surname}")

    def print_age(self):
        return f"მე ვარ {self.age} წლის"


person = Human("გელა", "გენებაშვილი", 25)


person.print_name_and_surname()
print(person.print_age())