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

# returns data type
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

# sum() calculates the sum of array
print(second_array.sum())
# axis attribute for rows and columns
# axis=0 means column wise sum
print(second_array.sum(axis=0))
# axis=1 means row wise sum
print(second_array.sum(axis=1))

# sqrt() square root of each element in np array
print(np.sqrt(second_array))

# std() standard deviation
print(np.std(second_array))

"""
    mathematical operations on arrays
    plus +, minus -, multiplication *, division /
    these operations performed like on matrix
    # in simple lists the + will concatenate each other
    # in numpy arrays + will add elements
"""
a = np.array([
    (1, 2, 3),
    (3, 4, 5)
])
b = np.array([
    (4, 5, 6),
    (6, 7, 8)
])

# plus + it will add corresponding elements
"""
    its like
    [1 2 3]  +  [4 5 6]
    [3 4 5]     [5 6 7]
"""
print(a + b)

# minus - it will subtract corresponding elements
"""
    its like
    [1 2 3]  -  [4 5 6]
    [3 4 5]     [5 6 7]
"""
print(a - b)

# multiplication * it will multiply each element
"""
    its like
    [1 2 3]  *  [4 5 6]
    [3 4 5]     [5 6 7]
"""
print(a * b)

# division / it will divide each element
"""
    its like
    [1 2 3]  /  [4 5 6]
    [3 4 5]     [5 6 7]
"""
print(a / b)

"""
    for np arrays concatenation there are some operations
    which are vertical stack and horizontal stack
    the box and box or box on box
"""
print(np.vstack((a, b)))
print(np.hstack((a, b)))

# convert 2d array into 1d
print(a.ravel())
