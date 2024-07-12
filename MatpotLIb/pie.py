import matplotlib.pyplot as plt

foods = ['Fried Rice','Kottu','Biriyani','Pizza']
price = [650,800,700,1100]
plt.pie(price, labels = foods, radius=1.5, autopct = '%0.1f%%', explode = [0,0.02,0,0])
plt.show()
