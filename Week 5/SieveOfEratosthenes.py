# Bonus Question - 4
import math

def isPrime(num):
    sqrt = int(math.sqrt(num))+1
    for i in range(2, sqrt):
        if num%i==0: return False
    return True

def getPrimeNumbers(n):
    nums = [i for i in range(2,n+1)]
    primeNums = []
    for i in nums:
        if i!=0 and isPrime(i):
            primeNums.append(i)
            # Removing the multiples of i from nums
            for j in range(i-1, n-1):
                if nums[j]%i==0: nums[j]=0
    return primeNums

if __name__ == "__main__":
    n = int(input("Enter the limit: "))
    print( str(getPrimeNumbers(n)) )