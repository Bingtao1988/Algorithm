# Implementation of insertion in a dynamic array:

"""
def insert(self, k, value):
    if self._n == self._capacity:
        self._resize(2 * self._capacity)
    for j in range(self._n, k, -1):
        self._A[j] = self._A[j - 1]
    self._A[k] = value
    self._n += 1
"""
"""
def remove(self, value):
    for cnt in range(self._n):
        if self._A[cnt] == value:
            for cnt_inner in range(cnt, self._n - 1):
                self._A[cnt_inner] = self._a[cnt_inner + 1]
            self._A[cnt_inner + 1] = None
            self._n -= 1
            return
        raise ValueError('value not found')
"""
"""
# Faster way to build a string:

def pickupAlphaBet(string):
    resultArray = []
    for char in string:
        if char.isAlpha():
            resultArray.append(char)
    return ''.join(resultArray)
"""
