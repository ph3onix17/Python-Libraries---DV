import numpy as np

arr = np.array([[1,2,3,4,5,6],[1,2,3,4,5,6]])

#if we want to find number 4
x = np.where(arr==6)
x = np.where(arr%2 ==0)
#print(x)

#search sorted

arr2 = np.array([1,3,5,7])
g = np.searchsorted(arr2,9) #sort krama dann ona index eka print krnwa <))><
gg = np.searchsorted(arr2,[0,4,9])
g = np.searchsorted(arr2,9,side='right')
print(g)

#kalin left eke idanne baluwe (default) right eke idan index eka >>
