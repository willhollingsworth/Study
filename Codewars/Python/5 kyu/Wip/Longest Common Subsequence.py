# https://www.codewars.com/kata/52756e5ad454534f220001ef/train/python

def lcs(x, y):
    i2 = 0
    output  = ''
    for i in y:
        if i2+1 > len(x):
            break
        if i == x[i2]:
            output += i
            i2 += 1
    return output

print(lcs("abcde", "ace"), "ace")
print(lcs("a", "b"), "")
print(lcs("a", "a"), "a")
print(lcs("abc", "ac"), "ac")
print(lcs("abcdef", "abc"), "abc")
print(lcs("abcdef", "acf"), "acf")        
print(lcs("anothertest", "notatest"), "nottest")
print(lcs("132535365", "123456789"), "12356")
print(lcs("finaltest", "zzzfinallyzzz"), "final")