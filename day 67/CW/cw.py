class Person:
  def __init__(self, name, surname, fathername):
    self.name = name
    self.surname = surname
    self.fathername = fathername

  def __str__(self):
    return f"ჩემი სახელია {self.name}, ჩემი გვარია {self.surname}. მამაჩემს ჰქვია {self.fathername}"

p1 = Person("ლაშა", "ტოტოღაშვილი", "ნუგზარი")

print(p1)