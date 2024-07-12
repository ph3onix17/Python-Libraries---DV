import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4])
y = np.array([1,2,2.5,4])

plt.plot(x,y,'ko:')
plt.xlabel('Count X')
plt.ylabel('Count Y')
plt.title('Limit of axis')
left,right = plt.xlim(0.9,4.3) #only right, [right = 5]
bottom,top = plt.ylim(0.9,4.3)
print(bottom,top)
print(left,right)
plt.show()