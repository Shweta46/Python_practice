
markdict = {"Tom": 67, "Tina": 54, "Akbar": 87, "Kane": 43, "Divya": 73}

# CONVERT THE DICTIONARY TO LIST OF LIST
marklist = list(markdict.items())

print(marklist)
l = len(marklist)

# SORT THE LIST OF LIST USING MATRIX OPERATION ON EVERY B ELEMENT OF THE (MARKLIST[A][B])
for i in range(l):
    for j in range(0, l-i-1):
        if marklist[j+1][1] < marklist[j][1]:
            marklist[j+1], marklist[j] = marklist[j], marklist[j+1]
sortdict = dict(marklist)
print(sortdict)
