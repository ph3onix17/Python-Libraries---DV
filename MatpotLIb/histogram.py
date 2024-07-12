import matplotlib.pyplot as plt

marks = [65,34,74,87,39,34,65,87,67]

#plt.hist(marks,4)
plt.hist(marks,bins=[0,50,75,100],rwidth=0.9,color='k')
plt.show()
