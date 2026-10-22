import numpy as np

arr = np.array([1, 2, 3])
for x in arr:
    print(x)


d2 = np.array([[1, 2, 3], [4, 5, 6]])
print(d2)
for row in d2:
    for col in row:
        print(col)

# if we iterate n dim array we get n-1 dim array


# nditer can give us scalars can do deep
d3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(d3):
    print(x)

e2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for i in np.nditer(e2[:, ::2]):  #all rows, every second col
    print(i)


# NDENUMERATED - gives us index and item

f = np.array([1, 2, 3])
for idx, x in np.ndenumerate(f):
    print(idx, x)


g = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(g):
    print(idx, x)