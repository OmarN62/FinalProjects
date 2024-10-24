#define a function named fib that works on the fibonacci
#function that takes a variable n 
# and for variable a and b
#while the variable a is less than n (n = input)
#print a to n's input
#a
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
        print()
fib(1000)