# In Python, functions can be treated as objects, and decorators are a way to modify or extend the behavior of functions. They're like a seasoning that you sprinkle on top of a function to enhance it.
#
# How do decorators work?
#
# Decorators are functions that take another function as an argument and return a modified version of that function. They allow you to wrap or modify the behavior of a function before or after it's executed.

def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        return result
    return wrapper

@log_function
def add(a, b):
    return a + b

# is same as
def add(a, b):
    return a + b
add = log_function(add)

# When you call add(3, 5), it's actually calling the modified version of add, which logs the function call before and after executing the original add function.

result = add(3, 5)
print(result)

# TYPES OF DECORATORS:
# 1. Function decorators
# 2. Class decorators
# 3. Method decorators
# 4. Decorator factories
# 5. Built-in decorators
# 6. Chaining decorators

# One example of built-in decorators is @staticmethod
# 1. A static method operates at the class level rather than at the instance level. It can only access other static attributes and methods of the class, not the instance-specific attributes or methods that vary from one object to another.

# In this example, the MathUtils class defines a static method add using the @staticmethod decorator. This static method doesn't require an instance of the class to be called; you can directly use the class name MathUtils.add(3, 5) to call it.

# A static method operates independently of any instance's data or behavior. When you create an instance of a class, you can access its attributes and methods using that instance. However, a static method is not tied to any specific instance, so it doesn't have access to instance-specific data.

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print("\nSTATIC METHOD:")
result = MathUtils.add(3, 5)
print(result)

class MyClass:
    static_var = "Static variable"
    def __init__(self, name, class1):
        self.name = name
        self.class1 = class1

    @staticmethod
    def static_method():
        print("This is a static method.")
        # print(self.name)
# Here, the above code line will give error as its a static method and cannot access the instance variable. These are created when you want to create a method thats independent of the instance variables.

obj1 = MyClass(12, 45)
obj2 = MyClass(9, 89)

print(obj1.static_var)
obj1.static_method()

print(obj2.static_var)
obj2.static_method()

# If you want to define a method that is not tied to any specific instance of the class and can be called using the class itself, you can use a static method along with the @staticmethod decorator.

# 2. Classmethod: A class method is a method that is bound to the class itself rather than to any instance of the class. It takes the class as its first parameter, often named cls. Class methods can access and modify class-level attributes but don't have access to instance-specific attributes.

class MyClass:
    class_var = "Class variable"

    def __init__(self, instance_var):
        self.instance_var = instance_var

    @classmethod
    def class_method(cls):
        print("This is a class method.")
        print(f"Class variable: {cls.class_var}")

MyClass.class_method()

# 3. @property decorator: The @property decorator is used to create a special method that acts like a getter for a class attribute.
# This allows you to access the attribute as if it were a property, providing a more intuitive and convenient way to retrieve the attribute value.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius

    def diameter2(self):
        return 2 * self.radius

    @property
    def area(self):
        return 3.14 * self.radius ** 2

circle = Circle(5)
print("Diameter:", circle.diameter2())
print("Radius:", circle.radius)
print("Radius:", circle.diameter)
print("Radius:", circle.area)

# A getter is a method that allows you to retrieve the value of a private or protected attribute of a class. It provides controlled access to the attribute's value, usually implementing some logic before returning the value. Getters are used to encapsulate attribute access and provide a clean and consistent way to retrieve attribute values.

# Example of getter:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

person = Person("Alice", 30)
print("Name:", person.get_name())
print("Age:", person.get_age())

# Setters: setters are methods that are used to modify or set the values of private or protected attributes (also known as properties) of a class. They provide a controlled way to update the values of these attributes while potentially enforcing validation or applying certain rules.

# Setters are important for maintaining data integrity and encapsulation. By using setters, you can ensure that the attributes of a class are modified in a controlled manner, adhering to specific conditions or constraints. This prevents accidental or unauthorized modifications to the internal state of an object.

class Student:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def set_name(self):
        if isinstance(name, str):
            self._name = name
        else:
            print("Name should be a string.")
student = Student("Alice", 20)

student.set_name("Bob")