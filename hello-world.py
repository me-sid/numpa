import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# check dimension of arr
print(arr_2d.ndim)


# array with 5 dimension
a = np.array([2, 3, 4, 5], ndmin=5)
print(a)
print(a.ndim)

