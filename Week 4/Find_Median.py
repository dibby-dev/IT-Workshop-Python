# Question - 5

def findMedian(a, b, c):
    if (b<a<c) or (c<a<b):
        return a
    elif (a<b<c) or (c<b<a):
        return b
    else:
        return c

if __name__ == "__main__":
    a, b, c = input("Enter three numbers in a line: ").split()
    print(f"Median: {findMedian(int(a), int(b), int(c))}")
