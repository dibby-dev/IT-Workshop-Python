# Question - 1

if __name__ == "__main__":
    distance = float(input("Enter the distance travelled (in m): "))
    distance = distance/140
    BASE_FARE = 4.00
    total_fare = BASE_FARE + (distance*0.25)
    print(f"Total Fare = ${total_fare}")