def dispSeq(num):
    while num != 1:
        print(num, end=" ")
        if num&1 == 0:
            num = num//2
        else:
            num = (num*3)+1
    print(num)

print("Enter numbers: ")
while True:
    num = int(input())
    if num <= 0: exit()
    dispSeq(num)