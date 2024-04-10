players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])
players2 = players
print('Players', players2)

# tuples cant be changed but can be overwritten

class Todo():
    def __init__(self, name, car, house, vacations):
        self.name = name
        self.car = car
        self.house = house
        self.vacations = vacations
    
    def things_to_do(self):
        print("I am "+ self.name + ' and i will own this car by the end of 2024 ' + self.car + ' and I will be living in ' + self.house + '. ' + 'Vactions I would go on before I turn 27 are ' + self.vacations)

    def more_vacations(self, one_more):
        self.vacations = one_more

me = Todo('shweta', 'toyota sedan', 'two storey condo', 'europe trip')
me.things_to_do()

# Modifying the car
me.car = 'audi'
me.things_to_do()

# modifying the attribute using class method 
me.more_vacations('Norway')
me.things_to_do()

print('\n\n')

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles
    
    def fill_gas_tank(self):
        print("Fill the gas tank")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70
    
    # overriding the parent class methods
    def fill_gas_tank(self):
        print("This car doesnt need a gas tank.")

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + ' -kwh battery')


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())    
my_tesla.describe_battery()
my_tesla.fill_gas_tank()