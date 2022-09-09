# Question - 4
from re import T
from ProperDivisors import generateProperDivisors

def isProperDivisor(n):
    proper_divisors = generateProperDivisors(n)
    sum = 0
    for i in proper_divisors: sum += i
    return True if sum == n else False

def generatePerfectIntegers():
   return [i for i in range(1, 10001) if isProperDivisor(i)]

if __name__ == "__main__":
    print(f"Perfect Integers between 1 & 10000: ", end="")
    print( str(generatePerfectIntegers()) )