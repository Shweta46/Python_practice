test_str = "Geeks for Geeks"
all_freq = {}

for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
print(all_freq)
# print("Count: " + str(all_freq))

marklist = sorted(all_freq.items(), key=lambda x:x[1])
sortdict = dict(marklist)
print(sortdict)