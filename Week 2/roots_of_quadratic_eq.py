from cmath import sqrt

def quadraticRoots(a, b, c):
    d = sqrt((b ** 2) - 4 * a * c)
    r_1 = (- b + d) / (2 * a)
    r_2 = (- b - d) / (2 * a)
    print(f"Roots are {r_1}, {r_2}")

a, b, c = list(map(int, input("Enter a, b and c: ").split()))
quadraticRoots(a, b, c)