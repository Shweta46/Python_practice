#**************************************************************************************************************************************
# 1. Bubble sort:

list1=[9,16,6,26,0]
print(list1)

print("unsorted list1 is", list1)
for j in range(len(list1)-1):
    for i in range(len(list1)-1):
        if list1[i]>list1[i+1]:
            list1[i],list1[i+1]=list1[i+1],list1[i]
            print(list1)
        else:
            print(list1)
    print( )
print("sorted list is",list1)

# Methods that requires less iterations and steps:
list1=[9,16,6,26,0]
print("unsorted list1 is", list1)
for j in range(len(list1)-1,0,-1):
    for i in range(j):
        if list1[i]>list1[i+1]:
            list1[i],list1[i+1]=list1[i+1],list1[i]
            print(list1)
        else:
            print(list1)
        print( )
print("sorted list is",list1)

# Steps:
# [9, 16, 6, 26, 0]
# [9, 6, 16, 26, 0]
# [9, 6, 16, 26, 0]
# [9, 6, 16, 0, 26]

# [6, 9, 16, 0, 26]
# [6, 9, 16, 0, 26]
# [6, 9, 0, 16, 26]

# [6, 9, 0, 16, 26]
# [6, 0, 9, 16, 26]

# [0, 6, 9, 16, 26]
# sorted list is [0, 6, 9, 16, 26]

# Program to give input from the user to sort the elements
# list1=[]
# num=int(input("enter how many numbers:"))
# print("enter values")
# for k in range(num):
#     list1.append(int(input()))
# print("unsorted list1 is", list1)
# for j in range(len(list1)-1):
#     for i in range(len(list1)-1):
#         if list1[i]>list1[i+1]:
#             list1[i],list1[i+1]=list1[i+1],list1[i]
#             print(list1)
#         else:
#             print(list1)
#     print( )
# print("sorted list is",list1)

#Selection sort
# def selection_sort(num):
#     size = len(num)
#     for i in range(size):
#         min = num[i]
#
#
#
#
#
#
#
# numbers = int(input('Enter the numbers:'))
# Selection_sort(numbers)

# min = 0
list1=[9,16,6,26,0]
def selection_sort2(list1):
    min = list1[0]
    for i in range(len(list1)-1):
        print('i is:',i)
        print('min right now is:', min)
        for j in range(i+1, len(list1)-1,1):
            if min > list1[j]: list1[i], list1[j] = list1[j], list1[i]
        print(list1)

selection_sort2(list1)
# ***********************************************************************************************************************************88
# Finding the smallest number from a list
# min = list[0]
# for j in range(0,len(list)-1,1):
#     if min > list[j]:
#         min = list[j]
# print(min)

#***********************************************************************************************





