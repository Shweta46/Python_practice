def name_matching(str, word):
    i = j = 0
    index = -1
    while j < len(word):
        while i < len(str):
            if str[i] == word[j]:
                j += 1
                index = i
            else:
                i = j
                j = 0
    return index

# KMP and LPS algorithm

string = "ashish is string"
word = "string"

print(name_matching(string, word))




