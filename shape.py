class Shape:
    def __init__(self, shape_type, sides):
        self.shape_type = shape_type
        self.sides = sides

    def area(self):
        print(f"{self.shape_type}'s Area is not defined")


class Square(Shape):
    def __init__(self, side_length):
        super().__init__("Square", 4)
        self.side_length = side_length

    def area(self):
        area = self.side_length ** 2
        print(f"The area of the square is {area}")


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle", 4)
        self.length = length
        self.width = width

    def area(self):
        area = self.length * self.width
        print(f"The area of the rectangle is {area}")


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle", 3)  # Corrected shape type to "Triangle"
        self.base = base
        self.height = height

    def area(self):
        area = 0.5 * self.base * self.height  # Corrected the area formula for triangle
        print(f"The area of the triangle is {area}")


class Trapezium(Shape):
    def __init__(self, base1, base2, height):
        super().__init__("Trapezium", 4)  # Trapezium has 4 sides
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def area(self):
        area = 0.5 * (self.base1 + self.base2) * self.height  # Correct area formula for trapezium
        print(f"The area of the trapezium is {area}")


square = Square(5)
square.area()

rectangle = Rectangle(4, 6)
rectangle.area()  

triangle = Triangle(3, 4)
triangle.area()  

trapezium = Trapezium(3, 4, 5)
trapezium.area()
