list_instance = [0, 1, 2]
list_iterator = iter(list_instance)
print(next(list_iterator))
print(next(list_iterator))
print(next(list_iterator))
# Will have a StopIteration exception
# print(next(list_iterator))


# The range() function call will return us a iterable range object
x = range(10000)
print(type(x))


def Fib_num(num):
    a = 1
    b = 1
    while a <= num:
        yield a
        temp = a + b
        a = b
        b = temp
        

for i in Fib_num(100):
    print(i)

        
    
