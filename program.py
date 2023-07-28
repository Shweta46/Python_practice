class Employee:
    raise_amount = 1.04
    num_of_emps = 0
    no_of_leaves = 8

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@hollywood.com'

        Employee.num_of_emps += 1

    #regular method takes instance as the first argument, to change that and use class as the first argument
    #classmethod is a decorator
    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    #to accept a string and parse it, this is an example of using classmethods as alternative constructors
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    #simply making a function to check if the date given was a work day or not. This is related to the class but not
    # necessarily needs the class or the instance as the argument. One tell is if while writing the method, you dont need the cls keyword, then it is static
    #for this, we can directly pass the argument we want to the output of
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):
    pass

emp_1 = Employee('Corey', 'Schafter', 500000)
emp_2 = Employee('Hunter', 'Schafer', 700000)

emp_1.fullname()

print(Employee.fullname(emp_1))

print(emp_1.pay)
print(emp_2.raise_amount)

emp_1.apply_raise()
print(emp_1.pay)

print(emp_1.__dict__)
print(Employee.__dict__)
print(Employee.num_of_emps) #shows that the class was initiated twice

#class methods

Employee.change_leaves(10) #here we dont have to write class as an argument as it takes that by itself
#the above statement is same as Employee.no_of_leaves = 10
print(emp_1.no_of_leaves)

#passing the instances as a string instead of individual objects
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Kristen-Stewart-10000000'
emp_str_3 = 'Robert-Patinson-1000000'
first, last, pay = emp_str_1.split('-')

new_emp_1 = Employee(first, last, pay)
# new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)

#*************************************************************************************************************************

#instead of writing the above method again and again, classmethod can be created to directly take the string and parse it

new_emp_2 = Employee.from_string(emp_str_2)
print(new_emp_2.email)

#staticmethods VS classmethods: static methods dont pass the instance or the class automatically unlike classmethod

import datetime
my_date = datetime.date(2016, 8, 10)
print(Employee.is_workday(my_date))