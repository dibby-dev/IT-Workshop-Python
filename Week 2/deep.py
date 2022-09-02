def isCorrect(answer):
    
    if answer in ['42', 'forty-two', 'forty two']: 
        print("Yes")
    else: 
        print("No")

answer = input("What is answer to the Life, the Universe and Everything? ")
isCorrect(answer.lower())