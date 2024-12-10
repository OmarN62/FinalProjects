#define a function named Fibonacci meant to go through 
def Fibonacci(n):
    #check if input is 0 and if it is then 
    #print that the input is incorrect
    if n < 0:
        print("Incorrect input")

    #check if n is equal to 0
    #if it is, then return 0
    elif n == 0:
        return 0
    
    #check is n is equal to 1 or if n is equal to 2
    #if it is then return 1
    elif n == 1 or n == 2:
        return 1
    
    #if input is equal to anything else, return
    #fibonacci n (n is input) - 1 plus fibonacci n - 2
    else: 
        return Fibonacci(n-1) + Fibonacci(n-2)
    
#this is called a driver program. a driver program
#takes a function and 
print(Fibonacci(10))


#how this works: 
#Fibonacci 10 print 10 + 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 = 55