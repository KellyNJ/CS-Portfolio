import math as m
while True:
    print()
    varLoop = input("Enter +, -, *, /, %, **, tan, or q to quit: ")
    if varLoop == '+':
        num1 = float(input("First Number: "))
        num2 = float(input("Second Number: "))
        answer = num1 + num2
        print("Addition: ",answer)
    elif varLoop == '-':
        num1 = float(input("First Number: "))
        num2 = float(input("Second Number: "))
        answer = num1 - num2
        print("Subtraction: ",answer)
    elif varLoop == '*':
        num1 = float(input("First Number: "))
        num2 = float(input("Second Number: "))
        answer = num1 * num2
        print("Multiplication: ",answer)
    elif varLoop == '/':
        num1 = float(input("First Number: "))
        num2 = float(input("Second Number: "))
        answer = num1 / num2
        print("Division: ",answer)
    elif varLoop == '%':
        num1 = float(input("First Number: "))
        num2 = float(input("Second Number: "))
        answer = num1 % num2
        print("Modulo: ",answer)
    elif varLoop == '**':
        num1 = float(input("First Number: "))
        num2 = float(input("Second Number: "))
        answer = num1 ** num2
        print("Exponent: ",answer)
    elif varLoop == 'tan':
        num1 = float(input("Tangent of what number: "))
        print("Tangent:", m.tan(num1))
    else:
        exit()