'''
Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible, containing distinct letters,

each taken only once - coming from s1 or s2.
Examples:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
'''

a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"

def longest(s1, s2):
    temp = []
    for x in range(len([s1,s2])):
        s[x]  = sorted(s[x] )
        for char in s[x] :
            if char.isalpha():
                temp.append(char)
        print(type(temp))
        print(type(s[x]))
        print(temp)
        s[x]  = temp
        temp = []
    print(s1,s2)
longest(a,b)
# print(sorted('red'))