# Bonus Question - 3

def detectUnaryOps(tokens :list):
    for i in range(len(tokens)):
        if tokens[i] in ['+', '-']:
            if i==0 or tokens[i-1] in ['*',"/","-","+","(",")"]:
                tokens[i] = 'u'+tokens[i]
    return tokens

if __name__ == "__main__":
    expression = input("Enter a mathematical expression: ")
    expression = [ str(i) for i in expression]
    expression = detectUnaryOps(expression)
    for i in expression: print(i, end="")
    