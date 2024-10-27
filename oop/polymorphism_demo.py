import math

class Shape:
    #A base class representing a general shape.#

    def area(self):
        #Raises an error, requiring derived classes to override this method.#
        raise NotImplementedError("Subclasses must implement the area method")


class Rectangle(Shape):
    #Represents a rectangle shape, with methods to calculate area.#

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        #Calculates and returns the area of the rectangle.#
        return self.length * self.width


class Circle(Shape):
    #Represents a circle shape, with methods to calculate area.#

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        #Calculates and returns the area of the circle.#
        return math.pi * (self.radius ** 2)
