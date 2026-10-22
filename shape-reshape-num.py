import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)


a = np.array([1, 2, 3, 4], ndmin=5)
print(a.shape)

#   RESHAPING
# note: reshaping makes a view not a copy



# 1D to 2D
b = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
c = b.reshape(4, 3)  # 4 array of 3 elements or 4 rows of 3 col
print(b)
print(c)

# 1d to 3d
d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
e = d.reshape(2, 3, 2) # first array will have 2 array then each array will have 3 array of 2 elements
print(d)
print(e)
print(e.base)


# UNKNOWN DIMENSION
# specify -1 and numpy will calculate that for u

f = np.array([1, 2, 3, 4, 5, 6, 7, 8])
g = f.reshape(2, 2, -1)
print(g)

# Flattening the arrays - making any array 1d
h = np.array([[1, 2, 3], [4, 5, 6]])
i = h.reshape(-1)
print(i)
