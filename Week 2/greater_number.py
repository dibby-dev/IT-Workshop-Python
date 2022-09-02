def findGreaterNumber(number1, number2):
    if number1 > number2:
        print(f"{number1} is greater.")
    else:
        print(f"{number2} is greater.")

num1, num2 = input("Enter two numbers: ").split()
findGreaterNumber(int(num1), int(num2))