'''
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.

eg:

validate_pin("1234") == True
validate_pin("12345") == False
validate_pin("a234") == False
https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/train/python
'''

import re
def validate_pin(pin):
    return bool(re.match('^\d{6}(?!\n)$|^\d{4}(?!\n)$', pin))

# best solution is
def best_validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()



print(validate_pin("12345") == False)
print(validate_pin("a234\n") == False)
print(validate_pin("1234") == True)
print(validate_pin("4534") == True)
print(validate_pin("1"))
print(validate_pin("123"))
print(validate_pin("123456"))
