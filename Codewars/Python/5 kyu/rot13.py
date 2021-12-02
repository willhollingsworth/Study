'''https://www.codewars.com/kata/530e15517bc88ac656000716/train/python
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.


'''
# print(ord('A'))
# for x in range(26):
#     print(chr(x+97))

def rot13(message):
    out_string = ''
    for letter in message:
        if letter.isalpha():
            value = ord(letter) + 13
            if letter.islower() and value > 122 : value -= 26
            if letter.isupper() and value > 90 : value -= 26
            out_string += (chr(value))
        else: 
            out_string += letter
    return out_string



print(rot13("test"),"grfg")
print(rot13("Test"),"Grfg")
print(rot13("zaza"),"Grfg")
print(rot13("Pbqrjnef"),'Codewars')
print(rot13("abcdefghijklmnopqrstuvwxyz"))
print(rot13("abcdefghijklmnopqrstuvwxyz".upper()))
# print(rot13("abcdefghijklmnopqrstuvwxyz"))


