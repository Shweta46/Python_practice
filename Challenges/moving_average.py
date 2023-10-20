def average(s, w):
    total_sum = 0
    total_averages = []
    for i in range(0, len(s)-w+1):
        for j in range(i, i+w):
            total_sum += s[j]
        total_averages.append(total_sum / w)
        total_sum = 0
    return total_averages

s = [1, 2, 3, 4, 5, 6]
w = 3
print(average(s, w))