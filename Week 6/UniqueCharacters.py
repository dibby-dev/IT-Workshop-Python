# Question - 4 

def determineUniqueChars(text):
    unique_char = {}
    for i in text:
        unique_char[i] = ""
    print(unique_char.keys())

text = input("Enter a sentence: ")
determineUniqueChars(text)