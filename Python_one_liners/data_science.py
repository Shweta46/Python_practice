import numpy as np

a = np.array([1,2,3])
print(a)

b = np.array([[1,2],
             [3,4]])
print(b)

c = np.array([[[1,2], [3, 4]],
              [[5,6], [7, 8]]])
print(c)

a = np.array([[1,0,0],
             [1,1,1],
             [2,0,0]])

b = np.array([[1,1,1],
             [1,1,2],
             [1,1,2]])
print(a + b)
print(a - b)
print(a * b)

print(np.max(a))
print(np.min(a))
print(np.average(a))
