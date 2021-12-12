'''
https://www.codewars.com/kata/55c6126177c9441a570000cc
https://docs.python.org/3/howto/sorting.html
https://www.w3schools.com/python/python_lists_comprehension.asp
'''


def order_weight(s):
    s = sorted(s.split())
    return ' '.join(sorted(s,key=lambda i : sum([int(x) for x in i])))


# summed = [sum([int(n) for n in c]) for c in s.split()]  # build list of summed digits
# sdupes = [c for i,c in enumerate(summed) if c in summed[:i]] # filter out non duplicates
# if len(sdupes) >= 1 : print('dupes detected',summed)


# print(order_weight("123 11 13 21 2 3 11111111"))
print(order_weight("103 123 4444 99 2000"), "2000 103 123 4444 99")
print(order_weight("4 103 123 4444 99 202 2000"), "2000 103 123 4444 99")
print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"), "11 11 2000 10003 22 123 1234000 44444444 9999")
print(order_weight(""), "")
        
