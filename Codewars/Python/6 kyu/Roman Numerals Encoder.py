'''
https://www.codewars.com/kata/51b62bf6a9c58071c600001b/train/python
Create a function taking a positive integer as its parameter and returning a string containing the Roman Numeral representation of that integer.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

Example:
solution(1000) # should return 'M'

Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000

idea: iterate from largest to smallest

target = 1900
for x in roman numbers:          start at largest
    temp_target = target

    if temp_target/x > .76
            charters = temp_target//x
            add x onto string output
            take x from temp_target


unfinished, giving up as roman numerals are confusing and dont care enough to learn them
'''
roman_dict =   [[1,'I'],
                [5,'V'],
                [10,'X'],
                [50,'L'],
                [100,'C'],
                [500,'D'],
                [1000,'M']] # for x in roman_dict:print(x[0])


def solution(n):
    print('trying to convert',n,end=' ')
    out_string = ''
    for x in range(len(roman_dict)):
        cur_r_val = roman_dict[-1-x][0]
        while n/cur_r_val > .75:
            n -= cur_r_val
            out_string += roman_dict[-1-x][1]
        
        while n < 0:
            n += roman_dict[-2-x][0]
            # out_length = len(out_string)
            # if out_length == 1:
            #     ins = 1
            # else : ins = out_length - 1
            out_string = out_string[:-1] + roman_dict[-2-x][1] + out_string[-1:]

    return out_string    

# print(solution(1),'I')
# print(solution(3),'III')
# print(solution(4),'IV')
# print(solution(6),'VI')
# print(solution(14),'XIV')
# print(solution(21),'XXI')
# print(solution(1000), 'M')
print(solution(1989),'MCMLXXXIX')

'''
print(solution(89),'LXXXIX')
print(solution(91),'XCI')
print(solution(984),'CMLXXXIV')
print(solution(1889),'MDCCCLXXXIX')

'''