import math


class Circle:
    def __init__(self, radius=1):
        self.__radius = radius

    def get_perimeter(self):
        return 2 * math.pi * self.__radius

    def get_area(self):
        return math.pi * self.__radius ** 2

    def set_radius(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius


def main():
    circle1 = Circle()
    print(f"The area of the circle of radius {circle1.get_radius()} is {circle1.get_area() : .3f}")

    circle2 = Circle(25)
    print(f"The area of the circle of radius {circle2.get_radius()} is {circle2.get_area() : .3f}")

    circle3 = Circle(125)
    print(f"The area of the circle of radius {circle3.get_radius()} is {circle3.get_area() : .3f}")

    circle2.set_radius(100)
    print(f"The area of the circle of radius {circle2.get_radius()} is {circle2.get_area() : .3f}")

main()