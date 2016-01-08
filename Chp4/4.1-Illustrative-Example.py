# This is a recursively way to implement factorial function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def binarySearch(arrayParameter, targetValue):
    if len(arrayParameter) == 1 and arrayParameter[0] == targetValue:
        return True
    elif len(arrayParameter) == 1 and arrayParameter[0] != targetValue:
        return False
    elif len(arrayParameter) > 1 and arrayParameter[len(arrayParameter) // 2] <= targetValue:
        print(arrayParameter[len(arrayParameter) // 2 :])
        return binarySearch(arrayParameter[len(arrayParameter) // 2 :], targetValue)
    elif len(arrayParameter) > 1 and arrayParameter[len(arrayParameter) // 2] > targetValue:
        print(arrayParameter[:len(arrayParameter) // 2])
        return binarySearch(arrayParameter[:len(arrayParameter) // 2], targetValue)



    
if __name__ == "__main__":
    print(factorial(5))
    array_para = [1,2,3,4,5]
    print(binarySearch(array_para, 2))
