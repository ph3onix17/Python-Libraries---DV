import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5])
plt.plot(x, np.power(x,2),'ko:',x, np.power(x,3),'bo:') #color point line style # linewidth = 2

plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Style')

plt.show()

'''
color codes >>>>>>>>>>>>>>>>>
'b' blue
'g' green
r - red
c - cyan
m - magenta
y - yellow
w - white k - black

points marks
. point marker
o circle marker
x x marker
D diamond
H hexagon
s square
+ plus


Line style
- solid line
_ dashed line
-. dash dot line
: dotted line
'''