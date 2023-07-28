def power(num):
    if ((num & (num-1)) == 0):
        print('yes')
    else:
        print('no')
power(32)