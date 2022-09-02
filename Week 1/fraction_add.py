frac_1, frac_2 = input("Enter two fractions: ").split()
n1, d1 = [int(i) for i in frac_1.split("/")]
n2, d2 = [int(i) for i in frac_2.split("/")]
numerator = str((n1*d2) + (n2*d1))
denominator = str(d1*d2)
print(f"{numerator}/{denominator}")