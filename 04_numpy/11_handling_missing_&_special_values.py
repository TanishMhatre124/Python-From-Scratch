#missing and special values 

#np.isnan(array)

import numpy as np

arr=np.array([1,2,np.nan,4,np.nan,6])
print(np.isnan(arr))

#output----------->true means missisng value , false means value is there 
#[False False  True False  True False]

#==================================

#np.nan_to_num(array,nan=value)   default =0


import numpy as np

arr=np.array([1,2,np.nan,4,np.nan,6])
cleaned_arr=np.nan_to_num(arr,nan=100)
print(cleaned_arr)

#output->[  1.   2. 100.   4. 100.   6.]

#==========================================================

#np.isinf()     -----------check if infinite value is there 

import numpy as np
arr=np.array([1,2,np.inf,4, -np.inf,6])

print(np.isinf(arr))

cleaned_arr=np.nan_to_num(arr,posinf=1000,neginf=-1000)
print(cleaned_arr) 
