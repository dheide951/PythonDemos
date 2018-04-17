def square(x):
    return x**2

def printString(string):
    print(string)

def doMath(num1, num2, num3, num4=0, num5=0):
    print(num1+num2+num3+num4+num5)

def divedBy2(num):
    return num /2
def multBy4(num):
    return num *4

num = divedBy2(10)
print (multBy4(num))

def toFloat(string):
    try:
        return float(string)
    except ValueError:
        print("not possible")

print(toFloat("4.0"))
