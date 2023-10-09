# Abstraction:
# Abstraction is the concept of simplifying complex reality by modeling classes based on their essential attributes and behaviors. It involves hiding the complex implementation details and showing only the necessary features of an object.
#
# In Python, abstraction is achieved through abstract classes and abstract methods.
# 1. Abstract Classes:
# An abstract class is a class that cannot be instantiated on its own and is meant to serve as a blueprint for other classes. It defines common methods that its subclasses should implement.

# 2. Abstract Methods:
# Abstract methods are methods declared in an abstract class without an implementation. Subclasses of the abstract class must provide an implementation for these methods.
# In summary, abstraction allows you to create a blueprint for classes, ensuring that certain methods are defined while hiding the complexities of implementation. This helps in designing more modular and maintainable code.

# The sentence "An abstract class is a class that cannot be instantiated on its own" means that you cannot create objects directly from an abstract class. In other words, you cannot use the abstract class to create instances or objects like you would with a regular class. Instead, the abstract class serves as a template or a blueprint for other classes to inherit from.
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):

    def calculate_area(self):
        return 3.14 * self.radius ** 2

    def __init__(self, radius):
        self.radius = radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

circle = Circle(5)
rectangle = Rectangle(4, 6)
