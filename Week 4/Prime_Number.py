# Question - 2

import math

def isPrime(num):
    sqrt = int(math.sqrt(num));
    for i in range(2, sqrt):
        if num%i == 0:
            return "It is not a Prime Number."
    return "It is a Prime Number"

if __name__ == "__main__":
    num = int(input("Enter a positive number: "))
    print(isPrime(num))