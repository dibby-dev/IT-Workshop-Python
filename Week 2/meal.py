def convert(time):
    h, m = [float(i) for i in time.split(":")]
    m /= 60
    return h + m

def main():
    time_str = input("Enter time (HH:MM):")
    time = convert(time_str)
    
    if 7 <= time <= 8:
        print("Breakfast time.")
    elif 12 <= time <= 13:
        print("Lunch time")
    elif 18 <= time <= 19:
        print("Dinner time")

main()