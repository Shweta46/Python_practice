class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

circle = Circle(5)
rectangle = Rectangle(4,6)

shapes = [circle, rectangle]

for shape in shapes:
    print(shape.area())

# ***********************************************************************************************************************************************

# SUPER(): When you use super() in a subclass, you can call methods from the superclass and utilize or extend their functionality. This is particularly useful when you want to keep the behavior of the superclass's method while adding additional functionality in the subclass.
class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        print("Some generic animal sound")

class Cat(Animal):
    def __init__(self, species, name):
        super().__init__(species)
        self.name = name

    def make_sound(self):
        super().make_sound() #comment this out to see what effect it does to the output
        print(self.name)

generic_animal = Animal("Unknown")
my_cat = Cat("Felis catus", "Whiskers")

# generic_animal.make_sound()
# my_cat.make_sound()

# Using super() in a subclass doesn't require that both the superclass and the subclass have methods with the same name. In fact, the purpose of using super() is to call methods from the superclass, regardless of whether the subclass has a method with the same name.

class Animal:
    def speak(self):
        print("Some generic animal sound. ")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Woof")

class Cat(Animal):
    # def meow(self):
    def speak(self):
        super().speak()
        print("Meow")

dog = Dog()
cat = Cat()

# print("Dog says:")
# dog.speak()
#
# print("Cat says:")
# cat.speak()

# Another way to access the method of parent class in OOPS
class Animal:
    def speak(self):
        print("Some generic animal sound.")

class Dog(Animal):
    def speak(self):
        Animal.speak(self)
        print("Woof")

class Cat:
    def speak(self):
        Animal.speak(self)
        print("Meow.")

dog = Dog()
cat = Cat()
cat.speak()

