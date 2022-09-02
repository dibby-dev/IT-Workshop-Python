def gcd(m, n):
    d = n if m>n else m
    while m%d!=0 or n%d!=0:
        d -= 1
    print(f"Greatest Common Divisor: {d}")
m, n = input("Enter two numbers: ").split()
gcd(int(m), int(n))