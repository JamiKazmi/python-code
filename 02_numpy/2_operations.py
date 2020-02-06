import sys
import time
import numpy as np

my_array = np.array([1, 2, 3])
second_array = np.array([
    (1, 2, 3, 4),
    (5, 6, 7, 8),
    (9, 10, 11, 12)
])

# returns the type of array
print(my_array.ndim)

# returns the byte size
print(my_array.itemsize)

# returns datatype
print(my_array.dtype)

# return size of array
print(second_array.size)

# return the shape of array
print(second_array.shape)

"""
    this was disturbing me!

# before reshape
# print(second_array)
# reshape the array
# second_array = second_array.reshape(3, 4)
# print(second_array)
"""

# slicing
# first index is for row and second for column
print(second_array[0, 3])

# it means from first row till end second indxes are columns
print(second_array[0:, 3])

# it will include the rows from 0 to -1
print(second_array[0:2, 2])

"""
   line space give us the values between two numbers
   # first value is start index
   # second value is end index
   # third value is the numbers of values you want between
   # first and second
"""
a = np.linspace(1, 3, 20)
print(a)

# max() returns the maximum value in array
print(my_array.max())

# min() returns the minimum value in array
print(my_array.min())
