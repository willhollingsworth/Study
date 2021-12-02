'''
https://www.codewars.com/kata/513e08acc600c94f01000001/python
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3

'''


'''
hex to dec
11  = 1X16 +1 = 17
2a = 2x16 + 10 = 42

dec to hex =
42 = (42/16=2.65 rounded 2   42%16 = 10 aka a  = 2a
'''


def rgb(r,g,b):
    out_string = ''
    for x in [r,g,b]:
        x = min(255,max(0,x))
        out_string += dec_to_hex(x)
    return out_string

def dec_to_hex(in_val):
    first_val = hex_char_lookup(in_val//16)
    second_val = hex_char_lookup(in_val%16)
    return f'{first_val}{second_val}'

def hex_char_lookup(in_val):
    # hex_dict = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    # if in_val < 10 : return in_val
    # else : return hex_dict[in_val]
    hex_dict = '0123456789ABCDEF'
    return hex_dict[in_val]



print(rgb(-40, 0, -155))
print(rgb(255, 255, 255))
print(rgb(255, 255, 300))
print(rgb(148, 0, 211))