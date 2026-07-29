#array modification 
#=============================
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

import numpy as np

arr=np.array([1,2,3,4,5,6,7,8,9])
new_arr=np.append(arr,[10,20,3,0])
print(new_arr)

#-----------------------------------

#concatenate
#np.concanatenate((array1,array2),axis=0)


import numpy as np

arr_1=np.array([1,2,3,4,5,6,7,8,9])
arr_2=np.array([11,22,33,0])

new_arr=np.concatenate((arr_1,arr_2,),axis=0)
print(new_arr)

#=======================================

#removing array
#np.delete(array,index,axis=none)

#1d
import numpy as np

arr=np.array([1,2,3,4,5,6,7,8,9])
new_arr=np.delete(arr,2)
print(new_arr)

#2d
import numpy as np

arr_2d=np.array([[2,3,4],[4,5,6]])
new_arr=np.delete(arr_2d,1,axis=0)
print(new_arr)

