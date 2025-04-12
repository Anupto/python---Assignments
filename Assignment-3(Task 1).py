
def fact_whileloop(n):
    counter = 1
    factorial = 1
    while n >= counter:
        factorial = factorial * counter
        counter += 1
    print(f'Factorial of {n} is: {factorial}')

def fact_forloop(n):
    a = 1
    for i in range (1, n+1):
        a = i * a
    print(f'Factorial of {n} is: {a}')


x = int(input("Enter a number: "))
#fact_whileloop(x)
fact_forloop(x)
