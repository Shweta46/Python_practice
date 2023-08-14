# Polymorphism:
#
# Polymorphism is a powerful concept in object-oriented programming that allows objects of different classes to be treated as objects of a common superclass. This means that you can use a single interface to represent various types of objects. Polymorphism enables you to write code that can work with different types of objects in a unified way, without needing to know their specific classes.
#
# Think of it like this: Imagine a music player that can play different types of audio files, like MP3, WAV, and FLAC. Each audio file type has its own specific methods and behaviors. With polymorphism, you can create a common interface for all these audio file types, allowing you to interact with and play them using the same set of methods, regardless of their actual class.
#
# In Python, polymorphism is often achieved through METHOD OVERRIDING. This allows you to define a method in a subclass with the same name as a method in the superclass. When an object of the subclass is used, the overridden method in the subclass gets called instead of the method in the superclass.

# n the example you provided, the base class Shape defines a method called draw(), which is meant to be a common behavior shared by all shapes. By having this method in the base class, you establish an expectation that all subclasses (such as Circle and Rectangle) should have their own implementations of the draw() method.
#
# This practice ensures that every subclass adheres to a certain interface or behavior, even though each subclass may implement the method differently. This concept is a fundamental part of object-oriented programming called "method overriding."

class Shape:
    def draw(self):
        pass
    def calculate_area(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Circle")

    def calculate_area(self):
        print("Circle area.")

class Rectangle(Shape):
    def draw(self):
        print("Rectangle.")

    def calculate_area(self):
        print("Rectangle area.")

shapes = [Circle(), Rectangle()]
for shape in shapes:
    shape.draw()
    shape.calculate_area()
    print("-------------------")

# 88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888

# Method overriding:
# It is a key concept in object-oriented programming that allows a subclass to provide a specific implementation for a method that's already defined in its superclass. This enables the subclass to "override" the behavior of the method inherited from the superclass with its own custom implementation.

# When a subclass overrides a method, it provides a new definition for that method that is more tailored to its specific needs. This allows you to customize or extend the behavior of the superclass's methods in a way that's relevant to the subclass.
#
# The basic rules for method overriding are:
#
# 1. The method in the subclass must have the same name as the method in the superclass.
# 2. The method in the subclass must have the same number and types of parameters as the method in the superclass.
# 3. The method in the subclass must have the same return type as the method in the superclass, or a compatible subtype (covariant return types).
# Here's a simple example to illustrate method overriding:
class Animal:
    def make_sound(self):
        return "Generic animal sound."

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

dog = Dog()
cat = Cat()
print(dog.make_sound())
print(cat.make_sound())

# 88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888

# Duck Typing:
# Duck typing is about focusing on an object's behavior rather than its explicit type. If an object behaves in a certain way, it's treated as if it belongs to a specific type or class.

# In Python, this means you can use an object based on whether it can respond to certain methods or operations, rather than caring about its specific class. For example, you might have different classes representing various animals, and as long as they all have a make_sound() method, you can treat them as "animals" without explicitly checking their class.

class Duck:
    def sound(self):
        return "Quack"

class Dog(Duck):
    def sound(self):
        return "Bark"

def make_sound(animal):
    return animal.sound()

duck = Duck()
dog = Dog()

print("Duck Typing begins: ")
print(make_sound(duck))
print(make_sound(dog))

# Consider you're writing a function that expects an object to have a quack() method. You're not concerned about the actual class of the object, but rather whether it can quack like a duck. If it can, you'll treat it like a duck!

class Duck:
    def quack(self):
        print("Quack!")

class Dog:
    def quack(self):
        print("Woof!")

class Robot:
    def beep(self):
        print("Beep!")

def make_sound(entity):
    entity.quack()
    
print("\nquack method use: ")
duck = Duck()
dog = Dog()
robot = Robot()

make_sound(duck)
make_sound(dog)

