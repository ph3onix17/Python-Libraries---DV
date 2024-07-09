#integer i
#boolean b
#complex c

import numpy as np

x = np.array([1,2,3,4],dtype = 'U')
y = np.array(['python','c++','c','c#','Typescript'])

#convert data type
z = np.array([1,2,3,0])
aa = z.astype('f')
ab = z.astype(bool) # 0 ; false 

print(x)
print(z.dtype) #<U10 = unicode data type
print(aa.dtype)
print(ab)