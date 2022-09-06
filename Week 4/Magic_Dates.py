# Bonus Question - 2

def isMagicDate(dd, mm, yyyy):
    if dd*mm == yyyy - 1900:
        print(f"{dd} {mm} {yyyy}")

def findMagicDates():
    for y in range(1900, 1999):
        daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if y%4 == 0:
            daysOfMonths[1] = 29
        for m in range(1, 12):
            for d in range(1, daysOfMonths[m-1]):
                isMagicDate(d, m, y)

print("Magic Dates of the 20th Century are: ")
findMagicDates()