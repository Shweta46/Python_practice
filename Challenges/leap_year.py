def leap_year(n):
    if n % 4 ==0 and n % 100 == 0 and n % 400 == 0:
        return True
    else:
        return False

n = 2000
print(leap_year(n))