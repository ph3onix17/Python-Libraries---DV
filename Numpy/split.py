import numpy as np

arr = np.array([1,2,3,4,5,6])

newarr = np.array_split(arr,2) # kotas dekkta kdnwa
newarr = np.array_split(arr,3) #kotas  3kta kdnwa

print(newarr)