# Question - 3
import math

def generateProperDivisors(n):
    return [i for i in range(1, int(n/2+1)) if n%i==0]

if __name__ == "__main__":
    n = int(input("Enter a number to generate proper divisiors: "))
    print( str(generateProperDivisors(n)) )          