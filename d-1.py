class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        value1 = 3.141 * self.radius * self.radius
        return round(value1, 2)

    def perimeter(self):
        value2 = 2 * self.radius * 3.141
        return round(value2, 2)


# circle1 = Circle(radius=1)
# print(circle1.area())
# print(circle1.perimeter())

# circle3 = Circle(radius=3)
# print(circle3.area())
# print(circle3.perimeter())
