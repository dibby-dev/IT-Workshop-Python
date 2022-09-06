# Question - 4

def isTriangle(a, b, c):
    if a >= b+c:
        return False
    if b >= a+c:
        return False
    if c >= a+b:
        return False
    return True

print("Enter the three sides of the triangle: ")
a, b, c = input().split()
print(isTriangle(int(a), int(b), int(c)))