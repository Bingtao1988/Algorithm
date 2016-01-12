# When declare a low-level array, the size must be declared so that a
# consecutive chunk of memory is given.

# For dynamic array, at first, the dynamic array should have larger size than
# needed. Then, when the size is approaching its limit, it copies all of its
# elements into a new, larger array.

# This will test whether python's list is dynamic array
import sys
test_array = []
print(sys.getsizeof(test_array))
for cnt in range(50):
    test_array.append(cnt)
    print(len(test_array),"\t",sys.getsizeof(test_array))

# Experiment 2 -> implementation of a dynamic array
import ctypes
class DynamicArray:
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)
        
    def _make_array(capacity, c):
        return (c * ctypes.py_object)()

    def __getitem__(self, k):
        if not 0 < k <= self._n:
            raise IndexError
        else:
            return self._A[k]

    def __len__(self):
        return self._capacity

    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c
    
    def append(value):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
            self._A[self._n] = value
            self._n += 1

# For dynamic array, the operation of n appending will be O(n) if we increase
# the array size using a geometric way
# If we increase array size using an arithmetic way, it could be O(n^2)

# Measure of the append operation using Python's list append
from time import time
def compute_average(n):
    data = []
    start = time()
    for k in range(n):
        data.append(None)
    end = time()
    print((end - start) / n)

compute_average(100)
compute_average(1000)
compute_average(10000)
compute_average(100000)
