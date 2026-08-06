import numpy as np
# #1d array
# arr1 = np.array([10,20,30])
# #2d array
# arr2 = np.array([[1,2,3],
#                  [4,5,6],
#                  [2,2,1]])
# print(arr1)
# print(arr2)
# #matrix
# matrix  =np.array([
#   [2,3,2],
#   [8,3,2]
# ])
# print(matrix)
# #deafult array
# zeros = np.zeros(3)
# print(zeros)

# ones = np.ones(3)
# print(ones)

# ones = np.ones((2,3))
# print(ones)

# #full function 
# filled_array = np.full((2,2),7)
# print(filled_array)

# #arange function
# arrangee = np.arange(1,10,3)
# print(arrangee)

# #creating identoty matrices
# identity_matrix = np.eye(4)
# print(identity_matrix)

#--------------------------------------------------------------
#shape size type of array
arr = np.array([[1,2,3,'jjj',4],
               [233,2,3,2.2,2]])
print(arr.shape)
print(arr.size)
print(arr.ndim)
print(arr.dtype)