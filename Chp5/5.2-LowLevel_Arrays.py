# This is the notes for low level array including some explainations and
# examples.

# 8 bits -> byte

# Each byte has a memory address (expressed as binary number) often associated
# with the actual physical memory.

# RAM -> Random access memory. Accessing efficiency is O(1)

# The interpreter of programming language can track the relationship between
# identifier and the memory address

# String -> saved using Unicode (2 bytes / 16 bits)
# Each cell of an array should have the same size (bytes) which make accessing
# each cell with only constant time.

# Referential array -> we don't know how many bytes we need for each cell
# (For example, strings), so array could only save references (still memory
# address).
# If the elements are immutable, there would be no trouble (integer). Since
# changing the value only change the reference to a new immutable element.

# Compact Array: string (array of characters)
# This kind of array could increase computing efficiency since it doesn't need
# to save reference (64 bits each) and also, since data is side by side
# (Consecutive), it is much easier to access using cach.

# Compact array:
import array
our_array = array.array('i', [1,2,3,4,5])
print(our_array)

# Two modules for compact array:
# array -> mainly for primary data types
# ctype -> more low level, for user defined types






















