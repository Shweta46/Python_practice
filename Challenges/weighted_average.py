def average(s, weighted_array):
    total_sum = 0
    total_averages = []
    window_size = len(weighted_array)
    for i in range(0, len(s) - window_size + 1):
        count = 0
        for j in range(i, i + window_size):
            total_sum = total_sum + (s[j] * weighted_array[count])
            count += 1
        total_averages.append(total_sum // window_size)
        total_sum = 0
    return total_averages

s = [1, 2, 3, 4, 5, 6]
weighted_array = [1, 2, 3]
print(average(s, weighted_array))