# Encapsulation:
# The key benefits of encapsulation is that it provides a level of protection and control over how data is accessed and modified.
# By using access modifiers like public, private, and protected, you can specify which parts of a class are exposed to the outside world and which should remain internal to the class.

# Control and Access:
# Encapsulation aims to control access to an object's internal details. By specifying access modifiers,
# you decide how other parts of the program can interact with attributes and methods.
#
# Access Modifiers:
# Python uses naming conventions for access control:
#
# 1. Public: No modifications needed. Attributes and methods without any leading underscores are considered public and can be accessed from anywhere.
#
# 2. Protected: Attributes and methods with a single leading underscore (e.g., _protected_attribute) are considered protected. While Python doesn't enforce strict protection, this convention indicates that they're intended for internal use within the class or its subclasses.
#
# 3. Private: Attributes and methods with a double leading underscore (e.g., __private_method) are considered private. Python applies name mangling to make them less accessible from outside the class. Although not entirely private, they are meant to be used only within the class that defines them.

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

# In this instance, __account_number and __balance are encapsulated within the BankAccount class. They're accessible and modifiable only through class methods.

class MyClass:
    def __init__(self):
        self.public_attribute = "I am public."
        self._protected_attribute = "I am protected."
        self.__private_attribute = "I am private."

object1 = MyClass()

print(object1.public_attribute)
print(object1._protected_attribute)
# print(object1.__private_attribute)
# Directly accessing the private attribute using the code lines above gives error. To access the private attribute, name mangling needs to be done.

# For example, if you have a class MyClass with a private attribute __private_attribute, Python will internally rename it to _MyClass__private_attribute.
# This name mangling makes the attribute slightly less straightforward to access from outside the class.

print(object1._MyClass__private_attribute)

# In this example, the deposit() and withdraw() methods are authorized methods that are allowed to modify the balance attribute.
# The get_balance() method is also authorized, but only for retrieving the balance without changing it.

class BankAccount1:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

my_acc = BankAccount1("Shrey", 909, 10000000)
print(my_acc._BankAccount1__balance)
print(my_acc.name)

class TemperatureConverter:
    def __init__(self, celcius):
        self._celcius = celcius

    def set_celcius(self, celcius):
        self._celcius = celcius

    def set_fahrenheit(self, fahrenheit):
        self._celcius = (fahrenheit - 32) * 5/9

    def get_celcius(self):
        return self._celcius

    def get_fahrenheit(self):
        return self._celcius * 9/5 + 32

temp_converter = TemperatureConverter(0)

temp_converter.set_celcius(25)
print("Celcius:", temp_converter.get_celcius())

temp_converter.set_fahrenheit(77)
print("Celcius ")



