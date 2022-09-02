total_cost = 0
print("Enter the age of the guests: ")
while True:
    age = input()
    if age == '': break
    age = int(age)
    if age<=2:
        total_cost += 0
    elif 3<=age<=12:
        total_cost += 14
    elif age>=65:
        total_cost += 18
    else:
        total_cost += 23
print(f"Total Admission Cost: ${total_cost}.00")