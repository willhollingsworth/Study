# https://www.codewars.com/kata/55983863da40caa2c900004e/train/python


# too slow
from itertools import permutations
def next_bigger(n) -> int:
    perms = permutations(str(n))
    perms = [int(''.join(n)) for n in perms]
    perms = sorted(perms)
    next = perms.index(n)+1
    if next > len(perms)-1:
        return -1
    while perms[next] == n:
        if next > len(perms)-2:
            break
        next += 1
    if perms[next] <= n:
        return -1
    else:
        return perms[next]




print(next_bigger(  12),   21)
print(next_bigger(  21),   -1)
print(next_bigger( 513),  531)
print(next_bigger(2017), 2071)
print(next_bigger( 414),  441)
print(next_bigger(9999999999), )
print(next_bigger( 144),  414)