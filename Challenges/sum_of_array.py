def sum_of_array(l):
    sum1 = 0
    new_l = l[::2]
    for i in range(len(new_l)):
        sum1 = new_l[i] + sum1
    return sum1

def sum_(l):
    new_l = l[::2]
    sum1 = sum(new_l)
    return sum1

def dictionary_of_word_frequency(l):
    dict1 = {}
    for i in l:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    return dict1

def threshold(l):
    p = []
    for i in l:
        if len(i) > 5:
            p.append(i)
    return p

def anagram_from_list(l):
    k = []
    for i in l:
        j = sorted(i)
        print(j)
        k.append(j)
    return k
    # print(k[1])
    # p = []
    # for o in range(len(k)):
    #     for r in range(o, len(k)):
    #         if o == r:
    #             p.append(k[o])
    # return p



l = [3, 8, 12, 5, 6, 10, 7]
l1 = ["apple", "banana", "apple", "orange", "banana", "apple"]
l2 = ["listen", "silent", "the", "hit", "ith", "hello"]

print(sum_of_array(l))
print(dictionary_of_word_frequency(l1))
print(threshold(l1))
print(anagram_from_list(l2))