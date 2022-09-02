def moneyGiveaway(greeting):
    if greeting == "hello":
        print("$0")
    elif greeting[0] == 'h':
        print("$20")
    else:
        print("$100")

greeting = input("Enter the greeting by the bank: ")
moneyGiveaway(greeting.replace(" ","").lower())