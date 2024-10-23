def add(num1 ,num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2 

def multiply(num1, num2):
    return num1 * num2 

def divide(num1, num2):
    return num1 / num2

print("Select your operation -\n" \
      "1. Add\n"\
      "2. Subtract\n"\
      "3. Multiply\n"\
      "4. Divide\n")

select = int(input("Select operations based on corresponding numerical input: 1 = addition, 2 = subtraction, 3 = multiplication, 4 = division:"))

numb1 = int(input("Enter your first number:"))
numb2 = int(input("Enter your second number:"))

if select == 1: 
    print(numb1, "+", numb2, "=", add(numb1, numb2))

elif select == 2:
    print(numb1, "-", numb2, "=", subtract(numb1, numb2))

elif select == 3:
    print(numb1, "*", numb2, "=", multiply(numb1, numb2))

elif select == 4:
    print(numb1, "/", numb2, "=", divide(numb1, numb2))

else: 
    print("Invalid input, please enter the number 1, 2, 3, or 4")
