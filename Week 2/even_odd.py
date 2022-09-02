def evenOrOdd(number):
    if (number&1) == 1:
        print("Number is Odd.")
    else:
        print("Number is Even")

num = int(input("Enter a number: "))
evenOrOdd(num)