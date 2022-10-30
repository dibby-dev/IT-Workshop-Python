# Question - 3
import math

def nextPrime(num):
    i = num + 1
    while i>num:
        if isPrime(i):
            return i
        i += 1

def isPrime(num):
    sqrt = int(math.sqrt(num))
    for i in range(2, sqrt):
        if num%i == 0:
            return False
    return True

if __name__ == "__main__":
    n = int(input("Enter a positive number: "))
    print(f"Next Prime Number: {nextPrime(n)}")