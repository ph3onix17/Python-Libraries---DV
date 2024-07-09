import numpy as np

x = np.array([1,2,3,4,5])
y = x.view()
z = x.copy()

x[0] = 99

print(y.base)
print(z.base)

#original wens kroth wens wenwa view eke
#copy eke wens wenne na whutto
# base eken base wela thiyana eka balagann puluwan
