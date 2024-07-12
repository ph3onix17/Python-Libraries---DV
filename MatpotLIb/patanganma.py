import matplotlib.pyplot as plt
import numpy as np

'''x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()'''

x = np.array([1,2,3,4])
y = np.array([2,4,6,8])
plt.plot(x,y)


plt.xlabel("x side")
plt.ylabel("y side")
plt.title("plot chart")
plt.show()