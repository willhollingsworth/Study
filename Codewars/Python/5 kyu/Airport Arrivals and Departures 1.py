def flap_display(display, rotors):
    output = display
    rotors = rotors[0]
    # if isinstance(rotors[0],list):
    for i,offset in enumerate(rotors):
        output = offset_display(output,i,offset)
    return output


def offset_display(display,character,offset):
    output = ''
    string_key = r'ABCDEFGHIJKLMNOPQRSTUVWXYZ ?!@#&()|<>.:=-+*/0123456789'
    for i,c in enumerate(display):
        if i < character:
            output += c
        else:
            current = string_key.find(c)
            new_value = (current + offset) % len(string_key)
            output += str(string_key[new_value])
    return output

print(flap_display('RED',[[1,1,1]]),'SGG')
print(flap_display('RED',[[1,1,1]]),'SGG')
print(flap_display('CAT',[[1, 13, 27]]),'DOG')
print(flap_display('HELLO ',[[15, 49, 50, 48, 43, 13]]),'WORLD!')
print(flap_display('CODE',[[20,20,28,0]]),'WARS')

# import codewars_test as test
# def BEFORE(a):
#     print("Before:");
#     return print(a);

# def AFTER(a):
#     print("After:");
#     return print(a);

# test.it('CAT => DOG')
# before = BEFORE(["CAT"])
# rotors = [[1, 13, 27]];
# after = AFTER(flap_display(before, rotors))
# expected = ["DOG"]
# test.assert_equals(after, expected)

# test.it('HELLO => WORLD!')
# before = BEFORE(["HELLO "])
# rotors = [[15, 49, 50, 48, 43, 13]]
# after = AFTER(flap_display(before, rotors))
# expected = ["WORLD!"]
# test.assert_equals(after, expected)
      
# test.it('CODE => WARS')
# before = BEFORE(["CODE"])
# rotors = [[20,20,28,0]]
# after = AFTER(flap_display(before, rotors))
# expected = ["WARS"]
# test.assert_equals(after, expected)

