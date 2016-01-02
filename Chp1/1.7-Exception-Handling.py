# Exception -- Base class for most error types
# AttributeError -- obj.foo, if obj has no member named foo
# EOFError -- end of file reached for console or file
# IOError -- failure of I/O operation
# IndexError -- index to sequence is out of bounds
# KeyError -- nonexistent key requested for a set of dictionary
# KeyboardInterrupt -- ctrl-c
# NameError -- no variable is found
# StopIteration -- next(iterator) if no element
# TypeError -- type of parameter is wrong
# ValueError -- value of parameter is wrong
# ZeroDivisionError -- division operator used with 0

# Test:

age = -1
while(age < 0):
    try:
        age = int(input("Input your age please"))
        if age <= 0:
            print("Your age should be positive")
    except(ValueError):
        print("The value should be integer")
    except(EOFError):
        print("There is an error when you handle your input")


