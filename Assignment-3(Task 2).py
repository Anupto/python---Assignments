import math

def calculation(n):
    a = math.sqrt(n)
    print("Square root: ", a)
    b = math.log(n)
    print("Logarithm: ",b)
    c = math.sin(n)
    print("Sine: ",c)


x = int(input("Enter a number: "))
calculation(x)


