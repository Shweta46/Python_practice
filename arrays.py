# r_num = int(input("Input number of rows: "))
# c_num = int(input("Enter the number of columns: "))
# two_D_array = [[0 for col in range(c_num)] for row in range(r_num)]
# for row in range(r_num):
#     for col in range(c_num):
#         two_D_array[row][col] = row*col
# print(two_D_array)

print(end='Enter the size of array: ')
tot = int(input())

arr = []
print(end='Enter ' + str(tot) + ' Elements: ')

for i in range(tot):
    arr.append(input())

print(end='Enter the value to delete: ')
val = input()

if val in arr:
    arr.remove(val)
    print('\nThe new array is: ')
    for i in range(tot-1):
        print(end=arr[i]+' ')
else:
    print('Element doesnt exist in the array.')