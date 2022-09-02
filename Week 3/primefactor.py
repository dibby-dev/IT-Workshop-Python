def primeFactorization(num):
    factor = 2
    print(f"The prime factors of {num} are:")
    while factor<=num:
        if num%factor==0:
            print(factor)
            num /= factor
        else:
            factor += 1

num = int(input("Enter a number:"))
if num<2:
    print("Entered number is less than 2.")
else: 
    primeFactorization(num)