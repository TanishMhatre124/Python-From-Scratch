
# 1-D array

import numpy as np
ar_1d=np.array([1,2,3,4,5,6,7,8,9,10])
print(ar_1d)

# 2-D array

import numpy as np
ar_2d=np.array([[1,2,3],
               [4,5,6],
               [7,8,9]])
print(ar_2d)

# multi dimessional array  --- matrix 

import numpy as np
matrix=np.array([[[1, 2, 3],
                   [4, 5, 6]],
                     [[1, 2, 3],
                       [4, 5, 6]]])
print(matrix)


# array with default values
#np.zeros(shape) [3] for 1d,(3,3) 2d

import numpy as np
zeroes_array=np.zeros(3)
print(zeroes_array)

#ones shape 

import numpy as np
ones_array=np.ones((2,3))
print(ones_array)

#full (shape,value)

import numpy as np
filled_array=np.full((2,2),7)
print(filled_array)


#creating sequence of numbers in numpy
#arange()
#arange (start,stop,step)

import numpy as np
arr=np.arange(1,10,2)
print(arr)

#identity matrix
#eye(size)

import numpy as np
identity_matrix=np.eye(4)
print(identity_matrix)
