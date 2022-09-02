def operation(x, y, z):
    if y == '+':
        r = x + z
        print("{:.1f}".format(r))
    elif y == '-':
        r = x - z
        print("{:.1f}",format(r))
    elif y == '*':
        r = x * z
        print("{:.1f}".format(r))
    elif y == '/':
        if z != 0:
            r = x / z
            print("{:.1f}".format(r))
        else:
            print("Can't divide by Zero.")
    else:
        print("Invalid Input.")
        
x, y, z = input("Enter the math problem: ").split()
operation(float(x), y, float(z))