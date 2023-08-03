# # OOPS: Generality to specificity.
#
# # Class: It is a blueprint.
#
# #Methods: Functions written inside a class. L.append(L)
# #So, whatever like this: object.method()
#
# #Constructor: It is a special fu nction which is called when an object of the class is created.
#
# #Special methods: These are automatically triggered, you dont have to exclusively call it. E.g., some functionns we want the program to execute itself and not ask user's permission.
#
#
# class Atm:
#     def __init__(self):
#         self.pin = ''
#         self.balance = 0
#
#         self.menu()
#
#     def menu(self):
#         user_input = input("""
#         Hello, how would you like to proceed?
#         1. Enter 1 to create pin
#         2. Enter 2 to deposit
#         3. Enter 3 to withdraw
#         4. Enter 4 to check the balance""")
#
#         if user_input == '1':
#             print('Create pin')
#             self.create_pin()
#         elif user_input == '2':
#             self.deposit()
#         elif user_input == '3':
#             self.withdraw()
#         elif user_input == '4':
#             print('Your remaining balance is:')
#             self.check_balance()
#         else:
#             print('Bye')
#
#     def create_pin(self):
#         self.pin = input('Enter your pin')
#         print('Pin set successfully')
#
#     def deposit(self):
#         temp = input("Enter your pin")
#         if temp == self.pin:
#             amount = int(input('Enter the amount'))
#             self.balance = self.balance + amount
#             print('Deposit successful')
#         else:
#             print('Invalid pin')
#
#     def withdraw(self):
#         temp = input('Enter your pin')
#         if temp == self.pin:
#             amount = int(input("Enter the amount"))
#             if amount < self.balance:
#                 self.balance = self.balance - amount
#                 print("Operation successful")
#             else:
#                 print('Insufficient balance')
#         else:
#             print("Invalid pin")
#
#     def check_balance(self):
#         temp = input('Enter your pin')
#         if temp == self.pin:
#             print(self.balance)
#         else:
#             print("Invalid pin")
#
# sbi = Atm()
print( 'Welcome to the GPA calculator. ')
print( 'Please enter all your letter grades, one per line. ')
print( 'Enter a blank line to designate the end. ')
# map from letter grade to point value
points = {'A+':4.0, 'A':4.0, 'A-':3.67, 'B+':3.33, 'B':3.0, 'B-':2.67,
'C+':2.33, 'C':2.0, 'C':1.67, 'D+':1.33, 'D':1.0, 'F':0.0}
num_courses = 0
total_points = 0
done = False
while not done:
    grade = input()
# read line from user
# empty line was entered
    if grade == '':
        done = True
    elif grade not in points:
# unrecognized grade entered
        print("Unknown grade {0} being ignored".format(grade))
    else:
        num_courses += 1
        total_points += points[grade]
# avoid division by zero
if num_courses > 0:
    print( 'Your GPA is {0:.3}' .format(total_points / num_courses))