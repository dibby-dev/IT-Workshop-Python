# Bonus Question - 4

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

def ordinalDate(day, month , year):
    daysOfMonths = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isLeapYear(year):
        daysOfMonths[2] = 29

    for i in range(0, month):
        day += daysOfMonths[i]

    return day

if __name__ == "__main__":
    dd, mm, yy = input("Enter the date (in dd mm yyyy format): ").split()
    print( ordinalDate(int(dd), int(mm), int(yy)) )