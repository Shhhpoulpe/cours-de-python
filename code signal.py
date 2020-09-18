def adjacentElementsProduct(inputArray):
    res = -1000
    for i in range(len(inputArray)):
        print(i)
        if i + 1 < len(inputArray):
            if inputArray[i] * inputArray[i+1] > res:
                res = inputArray[i] * inputArray[i+1]
    return(res)


def checkPalindrome(inputString):
    if (inputString==inputString[::-1]):
        return True
    else:
        return False

def centuryFromYear(year):
    if year % 100 != 0:
        return year // 100 +1
    else:
        return year // 100

def add(param1, param2):
    return param1+param2

def shapeArea(n):
    if n<0:
        return False
    return (n*n)+((n-1)*(n-1))
