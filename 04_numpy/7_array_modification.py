#array modification 

#insert----> 

#  np.insert(array,index,value,axis=none)
#array-original array
#index-
#axis- 0 row wise, 1 column wise 

#1d
import numpy as np

arr=np.array([1,2,3,4,5,6,7,8,9])
new_arr=np.insert(arr,2,100)
print(new_arr)

#2d
import numpy as np

arr_2d=np.array([[2,3,4],[4,5,6]])
new_arr=np.insert(arr_2d,1,[5,6,7],axis=0)
print(new_arr)

#--------------------------------------------------

#append()
 