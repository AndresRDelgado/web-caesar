def encrypt(text, rot):
    # Your code here
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    caesar = ""
    for char in text:
        caesar += rotate_character(char, rot)
    return caesar

def alphabet_position(letter):
    #returns the index alphabet position of a single char
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return alphabet.find(letter.lower())
    
def rotate_character(char, rot):
    #returns the letter after rotating specified number to the right, preserving case
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    #if alphabet.find(char.lower())==alphabet.find(char) and alphabet.find(char) != -1:
    if char.lower()==char and alphabet.find(char) != -1:
        return(alphabet[(alphabet_position(char)+rot) % 26])
    elif alphabet.find(char.lower())!= -1:
        return(alphabet[(alphabet_position(char)+rot) % 26]).upper()
    else:
        return(char)