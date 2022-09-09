# Question - 2

from store_int import acceptNums

def removeElementsFromEnds(intList, n):
    intList = sorted(intList)
    for i in range(n):
        intList.pop(0)
        intList.pop()
    return intList

if __name__ == "__main__":
    intList = acceptNums()
    n = int(input("Enter the number of elements to be removed from both ends: "))
    newIntList = removeElementsFromEnds(intList, n)
    print( str(intList),"\n",str(newIntList) )