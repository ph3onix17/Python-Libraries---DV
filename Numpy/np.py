import numpy as np
#v = np.__version__

d = np.array((1,2,3,4)) #we can use tuple or lists x = np.array([1,2,3,4]) 
print(d[3])

#2D array

dd = np.array([[1,2],[3,4],[3,4]])

ddd = np.array([[[1,2],[3,4],[3,4]],[[9,9],[9,4],[9,9]]])
print(ddd[1][1][1])

#how to know dimension?? >>> ndim
print("\nshow dimensions")
print(d.ndim)
print(dd.ndim)
print(ddd.ndim)

#convert one dimension array to 4 dimension array
dto4 = np.array((1,2,3,4), ndmin=4)

print(f"1D to 4D: {dto4}")