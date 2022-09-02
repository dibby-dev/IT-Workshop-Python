sum, count = 0, 0
print("Enter numbers: ")
while True:
    value = int(input())
    if value == 0:
        if count == 0: 
            print("Error: First number is 0")
            exit()
        break;
    sum += value
    count += 1
average = sum/count
print(f"Average = {average}")