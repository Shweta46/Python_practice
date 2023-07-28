list1=[5,3,7,1,9,6]
print(list1)

# for i in range(len(list1)):
#     min_val=min(list1[i:])
#     min_ind=list1.index(min_val)
#     list1[i],list1[min_ind]=list1[min_ind],list1[i]
#     print(list1)

def merge_sort(list1):
    if len(list1)>1:
        mid = len(list1)//2
        left_list = list1[:mid]
        right_list = list1[mid:]
        merge_sort(left_list)
        merge_sort(right_list)
        i = 0
        j= 0
        k = 0
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                list1[k] = left_list[i]
                i = i+1
                k = k+1
            else:
                list1[k] = right_list[j]
                j = j+1
                k = k+1
        while i < len(left_list):
            list1[k] = left_list[i]
            i = i+1
            k = k+1
        while j < len(right_list):
            list1[k] = right_list[j]
            j = j+1
            k = k+1

merge_sort(list1)
