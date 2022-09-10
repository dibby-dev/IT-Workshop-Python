# Question - 5

def charFreq(word):
    chars = {}
    for i in word:
        if i in chars:
            chars[i] += 1
        else:
            chars[i] = 1
    return chars

def isAnagram(word_1, word_2):
    if len(word_1) != len(word_2):
        return False
    word_1 = charFreq(word_1)
    word_2 = charFreq(word_2)
    if word_1 == word_2:
        return "Anagrams"
    return "not Anagrams"

word_1, word_2 = input("Enter two words (<w1><space><w2>): ").split()
print(f"They are {isAnagram(word_1, word_2)}")