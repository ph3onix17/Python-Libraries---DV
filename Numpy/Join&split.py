import numpy as np

arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[4,5,6],[7,8,9]])

new_arr = np.concatenate((arr1,arr2),axis=0)
print(new_arr)

