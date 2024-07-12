import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,10,0.1)
y1 = x
y2 = np.sqrt(x)
y3 = np.power(x,2)
y4 = np.power(x,3)
plt.figure()

plt.subplot(2,2,1)
plt.plot(x,y1,'k*-')
plt.title('y1 = x')

plt.subplot(2,2,2)
plt.plot(x,y2,'r*:')
plt.title('$y1 = \sqrt{x}$')

plt.subplot(2,2,3)
plt.plot(x,y3,'b*:')
plt.title('$y1 = {x^2}$')

plt.subplot(2,2,4)
plt.plot(x,y4,'g*:')
plt.title('$y1 = {x^3}$')

plt.show()