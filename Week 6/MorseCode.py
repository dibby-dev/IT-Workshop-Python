# Question - 3

def encode(text :str):
    morse_code = {
        'A' : '.-', 'B' : '-...', 'C' : '-.-.', 'D' : '-..', 'E' : '.',
        'F' : '..-.', 'G' : '--.', 'H' : '....', 'I' : '..', 'J' : '.---', 
        'K' : '-.-', 'L' : '.-..', 'M' : '--', 'N' : '-.', 'O' : '---',
        'P' : '.--.', 'Q' : '--.-', 'R' : '.-.', 'S' : '...', 'T' : '-', 
        'U' : '..-', 'V' : '...-', 'W' : '.--', 'X' : '-..-', 'Y' : '-.--',
        'Z' : '--..', '0' : '-----', '1' : '.----', '2' : '..---', '3' : '...--',
        '4' : '....-', '5' : '.....', '6' : '-....', '7' : '--...', '8' : '---..',
        '9' : '----.'
    }
    newText = ''
    for i in text:
        newText += (morse_code[i] if i in morse_code else i) + ' '
    return newText

if __name__ == "__main__":
    text = input('Enter the message: ')
    print( str(encode(text)) )