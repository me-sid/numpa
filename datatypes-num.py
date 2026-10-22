import numpy as np 

# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )


arr = np.array([1, 2, 3, 4])

print(arr.dtype) 

arr2 = np.array([1, 2, 3, 4], dtype='S')

# we can assign size too 

a = np.array([111, 123, 4, 10000000, 58], dtype="i4") # 4 byte integer

# best way to change datatype of array is to copy it
b = a.astype("f")

# bool type casting
c = np.array([-2,-1, 0, 1, 3])
d = c.astype('b')

print(arr2)
print(arr2.dtype)
print(a.dtype)
print(b.dtype)
print(d)
print(d.dtype)