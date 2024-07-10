#>>>>>>>>>>>>>>>>>>>> reshape
#1D array to 2D array

import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9])
new_arr = arr.reshape(3,3)
new_arr = arr.reshape(9,1)
#new_arr = arr.reshape(2,4)  meka wada krnne na gunithaya elment ganata samana wenna ona
new_arr = arr.reshape(3,-1) #-1 dammoth mu hraiyana eka auto dala ghnnwa :(

print(arr,"\n")
print(new_arr)

#hama ekktama ba 3,3 dann puluwan elements 9k thiyana hinda heh :) <))><

#onama ekk 1d array ekk krnne komtha???
reshaped = new_arr.reshape(-1)
print(reshaped)