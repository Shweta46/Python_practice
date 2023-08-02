class Dog:
    def __init__(self, name, age):
    # Any variable prefixed with self: It is available to every method in the class, and we’ll also be able to access these variables through any instance created from the class.
        self.name = name
        self.age = age

    # Self: Every method call associated with a class automatically passes self, which is a reference to the instance itself; it gives the individual instance access to the attributes and methods in the class.
    def sit(self):
        print(self.name.title() + ' is now sitting.')

    def roll_over(self):
        print(self.name.title() + ' rolled over!')

my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()

# RESTAURANT CLASS:
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('The R ' + self.restaurant_name + ' is worth the price. The cuisines ' + self.cuisine_type + ' available are all great.')

    def open_R(self):
        print('The R ' + self.restaurant_name + ' is now open!.')

restaurant = Restaurant('Raddison', 'Korean')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_R()
restaurant2 = Restaurant('Flamingo', 'Indian')
restaurant3 = Restaurant('Punjabi Chic Inn', 'Punjabi')
restaurant2.describe_restaurant()
restaurant2.open_R()
restaurant3.describe_restaurant()
restaurant3.open_R()

# CREATING A CHILD CLASS:

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("Fill the tank!")

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
    # The super() function at x is a special function that helps Python make connections between the parent and child class. This line tells Python to call the __init__() method from ElectricCar’s parent class, which gives an ElectricCar instance all the attributes of its parent class. The name super comes from a convention of calling the parent class a superclass and the child class a subclass
#     Then initialize attributes specific to an electric car.
        self.battery_size = 70

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def fill_gas_tank(self):
        print('This car doesnt need a gas tank!')
#     You can override any method from the parent class that doesn’t what you’re trying to model with the child class. To do this, you define a method in the child class with the same name as the method you want to override in the parent class. Python will disregard the parent class method and only pay attention to the method you define in the child class. Say the class Car had a method called fill_gas_tank(). This method is meaningless for an all-electric vehicle, so you might want to override this method.

my_tesla = ElectricCar('tesla', 'model S', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()
