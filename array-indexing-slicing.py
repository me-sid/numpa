import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print("Second element on first row", arr[0,1])
print("Second row fifth col", arr[1, 4])


# accessing 3d array

b = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(b[0, 1, 2])
