def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return(number // 2)
    elif number % 2 == 1:
        result = (3 * number +1)
        return result
n = input("What's your number:")
while n != 1:
    n = collatz(int(n))