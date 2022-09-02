def isPascalFraction(a, b, c, d):
    if a*d == c*b:
        print("Pascal's Fractions")
    else:
        print("Not Pascal's Fractions")

frac_1, frac_2 = input("Enter two fractions: ").split()
a, b = list(map(int, frac_1.split("/")))
c, d = list(map(int, frac_2.split("/")))
isPascalFraction(a, b, c, d)