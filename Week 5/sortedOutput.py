# Question - 5

def acceptIntegers():
    intList = []
    print("Enter Integers (enter blank to stop): ")
    while True:
        num = input()
        if num == '':
            return sorted(intList)
        intList.append(int(num))

intList = acceptIntegers()
for i in intList: print(i)