import time 

def print_number(number):
    print(number)
print_number(100)

time.sleep(5)

def print_number_input(number):
    number = int(input("enter your number: "))
    print("your number is:" + number)
    return print_number_input()
print_number_input()