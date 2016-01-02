# expr1 if condition else expr2
value = 0
x = 100 if value == 0 else 200
print(x)

# List comprehension
values = [1,2,3,4,5]
values_square = [x * x for x in values]
print(values_square)

# Simutaniously assignment
def fibnum(upperlimit):
    a = 1
    b = 1
    while(a < upperlimit):
        yield a
        a, b = b, a + b

print(list(fibnum(1000)))
