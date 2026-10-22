import numpy as np


# copy makes a new copy
arr = np.array([1, 2, 3, 4])
a = arr.copy()
arr[0] = 100
print(arr)
print(a)


# view is just viewing only, changes made to original will be affected in view

b = np.array([5, 6, 7, 8])
v = b.view()
b[0] = 88
print(b)
print(v)
# changes to view changes the original

v[-1] = 90
print(b)
print(v)

# to check if array owns the data
# copy return none, view return original array
print(arr.base)
print(a.base)
print(b.base)
print(v.base)


