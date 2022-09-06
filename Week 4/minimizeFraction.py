# Question - 6

def minimize(num_1, num_2):
    factor = num_2 if num_1 > num_2 else num_1
    while factor>1:
        if num_1%factor == 0 and num_2%factor == 0:
            num_1 /= factor
            num_2 /= factor
        else:
            factor -= 1
    return int(num_1), int(num_2)

num_1, num_2 = input("Enter two positive integers: ").split()
num_1, num_2 = minimize(int(num_1), int(num_2))
print(f"{num_1} {num_2}")
