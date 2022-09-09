# Question - 1

def acceptNums():
    intList = []
    print("Enter Numbers (enter '0' to stop): ")
    while True:
        num = int(input())
        if num == 0:
            return sorted(intList)
        intList.append(num)

print( str(acceptNums()) )