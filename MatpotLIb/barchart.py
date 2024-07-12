import matplotlib.pyplot as plt

subject = ['Maths','Physics','Chemistry']
marks = [56,65,70]

plt.bar(subject,marks,width=0.3) #add barh to horizontal
plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.ylim(0,100)
plt.show()