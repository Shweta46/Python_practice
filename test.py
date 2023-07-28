a = [1,7,7,9,10,11]
# max = a[0]
# min = a[0]
# peek = a[0]
# print(max)
# for i in range(0, len(a), 1):
#     if max > a[i-1]
#             and max > a[i+1] and a[i-1] < a[i+1]:
#         print(max)

def findPeakElement(nums):
    low = 0
    high = len(nums)-1
    while low<high:
        mid = low + (high - low+1)//2
        if (mid-1>=0 and nums[mid-1]<=nums[mid]):
            low = mid
        else:
            high = mid-1
    return nums[low+1]
l = [15,35,85,96,5,6,8,12]
print(findPeakElement(l))




