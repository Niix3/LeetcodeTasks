# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.
#
# Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".
#
# Please note that using encode is considered cheating.

def rot13(message):
    alphabet =   "abcdefghijklmnopqrstuvwxyz"
    alphabet_big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_message = ""
    for char in message:
        try:
            new_message += alphabet[(alphabet.index(char)+13)%26]
        except ValueError:
            try:
                new_message += alphabet_big[(alphabet_big.index(char) + 13) % 26]
            except ValueError:
                new_message += char
    return new_message
print(rot13("Test"))