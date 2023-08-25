def prime(a):
    flag = 0
    if a > 1:
        for i in range(2, int(a/2)+1):
            if a % i == 0:
                flag = 1
                break
        if flag == 0:
            return True
        else:
            return False
    else:
        return False

a = 11
print(prime(a))






























