# Bonus Question - 1

def isLeapYear(year):
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def noOfDays(mm, yyyy):
    daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isLeapYear(yyyy):
        daysOfMonths[1] = 29
    return daysOfMonths[mm-1]

if __name__ == "__main__":
    mm, yyyy = input("Enter the month and year: ").split()
    print(f"{noOfDays(int(mm), int(yyyy))} Days")