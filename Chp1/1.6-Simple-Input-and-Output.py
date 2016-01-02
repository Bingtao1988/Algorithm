print("maroon", 5)
# print "maroon 5\n"
print('maroon', 5, "new album", sep=",")
# print "maroon,5,new album\n"
print('maroon', 5, end="")
# print "maroon 5"


# Test Input
theYear = int(input("What is the year this year?"))
print(theYear)
print(type(theYear))

# Combine with existing string functions:
parameter = input("print x and y, separated by \":\"")
paras = parameter.split(":")
x = float(paras[0])
y = float(paras[1])
print(x,y)

# Operating files:

# inputfile = open("")
# lines = inputfile.readlines()
# print("", file=inputfile)
