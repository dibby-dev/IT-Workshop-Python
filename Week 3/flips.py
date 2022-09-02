import random

def toss():
    Hcount, Tcount = 0, 0
    count = 0
    while Hcount!=3 and Tcount!=3:
        count += 1
        val = random.randint(0,1)
        if val == 0: 
            print("H", end=" ")
            Hcount += 1
            Tcount = 0
        else: 
            print("T", end=" ")
            Tcount += 1
            Hcount = 0
    print(f"({count} flips)", end="")
    return count

sum = 0
for i in range(10):
    sum += toss()
    print()

print(f"On average, {sum/10} flips were needed.")