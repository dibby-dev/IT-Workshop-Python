# Bonus Question - 2

def tokenize(expression :str):
    return [str(i) for i in expression]

if __name__ == "__main__":
    expression = input("Enter a mathematical expression: ")
    expression = tokenize(expression.replace(" ",""))
    print( str(expression) )