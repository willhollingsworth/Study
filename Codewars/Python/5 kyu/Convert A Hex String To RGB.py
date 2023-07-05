# https://www.codewars.com/kata/5282b48bb70058e4c4000fa7/train/python
import test



def hex_string_to_RGB(hex):
    r = int(hex[1:3],16)
    g = int(hex[3:5],16)
    b = int(hex[5:],16)
    return {'r':r,'g':g,'b':b}

print(hex_string_to_RGB('#beaded'))
print(hex_string_to_RGB('#FF9933'))
hex_string_to_RGB("#beaded"), {'r':190, 'g':173, 'b':237}
hex_string_to_RGB("#FF9933"), {'r':255, 'g':153, 'b':51}
hex_string_to_RGB("#000000"), {'r':0, 'g':0, 'b':0}
hex_string_to_RGB("#111111"), {'r':17, 'g':17, 'b':17}
hex_string_to_RGB("#Fa3456"), {'r':250, 'g':52, 'b':86}