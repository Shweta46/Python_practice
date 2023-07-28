lower = 0
upper = 11
for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               if (num % 2) == 1:
                   print(num)
               break
