class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return self.radius * 3,2 ** 2
    
circle = Circle(4)
print(circle.area())