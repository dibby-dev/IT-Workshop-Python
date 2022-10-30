# Question - 2
from random import randint

def diceRoll() -> dict:
    result = {}
    for i in range(1000):
        num = randint(1, 6) + randint(1, 6)
        if num in result:
            result[num] += 1
        else:
            result[num] = 1
    return result

def displayTable():
    simulatedResult = diceRoll()
    expPercent = [2.78, 5.56, 8.33, 11.11, 13.89, 16.67, 13.89, 11.11, 8.33, 5.56, 2.78]
    print("Total\tSimulated\tExpected")
    print("\tPercent\t\tPercent")
    for i in range(2,13):
        sPercent = simulatedResult[i]/10
        print(f"{i}\t{sPercent}\t\t{expPercent[i-2]}")
    
displayTable()