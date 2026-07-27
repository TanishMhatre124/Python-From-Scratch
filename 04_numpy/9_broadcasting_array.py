# #broadcasting 

# #by using loops 
prices = [100, 200, 300]

discount = 10
final_prices = []

for price in prices:
    discounted_price = price - (price * discount / 100)
    final_prices.append(discounted_price)

print(final_prices)

#===========================
#  by using broadcasting 

import numpy as np
prices=np.array([100,200,300])
discount=10

final_prices= prices - (prices * discount / 100)
print(final_prices)

#============================================
import numpy as np 
arr=np.array([10,20,30])
result=arr *2
print(result)


#=====================================================
#broadcasting from 1d to 2d array

import numpy as np 
matrix=np.array([[10,20,30],[1,2,3]])
vector=np.array([4,5,6])

result=matrix + vector
print(result)

#=========================================
#error 

import numpy as np 
arr1=np.array([[10,20,30],[1,2,3]])
arr2=np.array([4,5])

result=arr1 + arr2
print(result)

