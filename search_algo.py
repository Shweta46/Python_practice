def lin_search(list, num):
    n=len(list)
    for i in range(0, n):
        if (num == list[i]): print(i)
    return -1

def binary_search(list, num):
    low = 0
    high = len(list)-1
    mid=0
    while low <= high:
        mid = (high+low)//2
        if list[mid] < num:
            low = mid+1
        elif list[mid] > num:
            high = mid-1
        else:
            print('I am mid:', mid)
            return mid
    return -1



list = [1, 8, 98, 45, 0, 6, 36]
num = int(input('Enter the number to find:'))
# lin_search(list, num)

# list = [1, 8, 98, 45, 0, 6, 36]
print('hi')
low = 0
high = len(list)-1
mid=0
while (low <= high):
    mid = (high+low)//2
    if list[mid] < num:
        low = mid+1
    elif list[mid] > num:
        high = mid-1
    else:
        print('I am mid:', mid)
