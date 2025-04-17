class Rectangle:
    def __init__(self, width , lenght):
        self.width = width
        self.lenght = lenght
    def area(self):
        return self.lenght * self.width

rectangle = Rectangle(3 , 4)
print(rectangle.area())