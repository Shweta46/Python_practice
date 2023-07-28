# 1st method
x = ('Mock', 'Night', 'Tight', 'Okay')
y = enumerate(x)
print(list(y))

# 2nd method
enumerate1 = enumerate(x, 10)
print(list(enumerate1))

# 3rd method
for i in enumerate(x):
    print(i)

# 4th method
for count, item in enumerate(x, 100):
    print(count, item)

