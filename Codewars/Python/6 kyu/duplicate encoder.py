'''
The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 
'''

def duplicate_encode(word):
    word = word.lower()
    out_string = ''
    for x in word:
        if word.count(x) == 1:
            out_string += '('
        else:
            out_string += ')'
    return out_string




print(duplicate_encode("din"),"(((")
print(duplicate_encode("recede"),"()()()")
print(duplicate_encode("Success"),")())())","should ignore case")
print(duplicate_encode("(( @"),"))((")