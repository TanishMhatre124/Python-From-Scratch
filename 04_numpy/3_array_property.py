#array shape 

import numpy as np
ar_2d=np.array([[1,2,3],
               [4,5,6],
               [7,8,9]])
print(ar_2d.shape)

# array size

import numpy as np
ar_2d=np.array([[1,2,3],
               [4,5,6],
               [7,8,9]])
print(ar_2d.size)



#ndim

import numpy as np

arr_1d=np.array([1,2,3])
arr_2d=np.array([[1,2,3],[4,5,6]])
arr_3d=np.array([[[1,2,3],[4,5,6],[7,8,9]]])

print("array dimession :",arr_1d.ndim)
print("array dimession :",arr_2d.ndim)
print("array dimession :",arr_3d.ndim)

#data type in array 

import numpy as np
arr=np.array([1,2,3,4])
print(arr.dtype)

#astype 
import numpy as np
arr=np.array([1.5,2,3,4,5,6,7,8.2,9])
int_arr=arr.astype(int)

print(int_arr)
print(int_arr.dtype)



