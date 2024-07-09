import numpy as np

arr = np.array([[1,2,3],[4,5,6]])

'''for i in arr:
    for j in i:
        print(j)
    
    print("one line is over")'''
    
#np.nditer()

for i in np.nditer(arr[:,::2]):
    print(i)
    
print("Enumerate")

for i,j in np.ndenumerate(arr):
    print(i,j)