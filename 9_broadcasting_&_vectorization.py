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
