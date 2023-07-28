def getRemainder(num, divisor):
    while (num >= divisor):
        num -= divisor
    return num

num = 100
divisor = 10
print(getRemainder(num, divisor))