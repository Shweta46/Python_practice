# *********************************************************************************************************************************************
# You’ll find that you have a growing list of attributes and methods and that your files are becoming lengthy.
# In these situations, you might recognize that part of one class can be written as a separate class. You can break your large class into smaller classes that work together.

class Car:
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

class Battery:
    # When we see this happening, we can stop and move those attributes and methods to a separate class called Battery. Then we can use a Battery instance as an attribute in the ElectricCar class:
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size
    def describe_battery(self):
        print('This car has a ' + str(self.battery_size) + '-kWh battery.')
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

print('Example of Instances as attributes')
my_tesla = ElectricCar('tesla', 'model X', 2016)
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
