"""
    numpy is an efficient module in python for different
    operations on lists and arrays (there lists and arrays
    are not like simple arrays and lists)
"""
import sys
import time
import numpy as np

my_array = np.array([
    (1, 2, 3),
    (4, 5, 6)
])
print(my_array)

"""
    it will give the space that is occupied by the list
    because sys.getsizeof() give the memory of 1 element
    and multiplying with the length of list will return entire
    memory space
"""
S = range(1000)
print(sys.getsizeof(5) * len(S))

# it will do the same for numpy arange function
D = np.arange(1000)
print(D.size * D.itemsize)

"""
    operations on simple lists and numpy arrays
    we do operations faster on numpy arrays than simple
    arrays
    here is an example
"""
size = 1000000
# simple lists
l1 = range(size)
l2 = range(size)
# numpy arrays
a1 = np.arange(size)
a2 = np.arange(size)

# calculating sum for simple lists
start = time.time()
result = [(x, y) for x, y in zip(l1, l2)]
print((time.time() - start) * 1000)

# calculating sum of numpy arrays
start = time.time()
result = a1 + a2
print((time.time() - start) * 1000)
