# https://www.codewars.com/kata/54b724efac3d5402db00065e/train/python

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


def decode_morse(morse_code):
    m_dict = {v:k for k,v in MORSE_CODE_DICT.items()}
    output = ''
    for c in morse_code.split(' '):
        print(m_dict.get(c))
        # output += m_dict.get(c)
    return output


# try:
#     from solution import decodeMorse as decode_morse
# except ImportError:
#     from solution import decode_morse

# import codewars_test as test

# @test.describe("Fixed tests")
# def tests():
        
#     @test.it("Should obtain correct decoding of Morse code from the description")
#     def test_morse_hey_jude():
# print(decode_morse('.... . -.--   .--- ..- -.. .'), 'HEY JUDE')

#     @test.it("Should obtain correct decoding of Morse code for basic examples")
#     def test_morse_basic_examples():
print(decode_morse('.-'), 'A')
print(decode_morse('--...'), '7')
print(decode_morse('...-..-'), '$')
print(decode_morse('.'), 'E')
print(decode_morse('..'), 'I')
print(decode_morse('. .'), 'EE')
print(decode_morse('.   .'), 'E E')
print(decode_morse('...-..- ...-..- ...-..-'), '$$$')
print(decode_morse('----- .---- ..--- ---.. ----.'), '01289')
print(decode_morse('.-... ---...   -..-. --...'), '&: /7')
print(decode_morse('...---...'), 'SOS')
print(decode_morse('... --- ...'), 'SOS')
print(decode_morse('...   ---   ...'), 'S O S')
        
#     @test.it("Should obtain correct decoding of Morse code for examples with extra spaces")
#     def test_morse_basic_examples_with_extra_spaces():
# print(decode_morse(' . '), 'E')
# print(decode_morse('   .   . '), 'E E')

#     @test.it("Should obtain correct decoding of Morse code for a complex example, and should ignore leading and trailing whitespace")
#     def test_morse_complex_example():
# print(decode_morse('      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-  '), 'SOS! THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.')