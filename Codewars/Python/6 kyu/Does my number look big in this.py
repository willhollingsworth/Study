def narcissistic( value ):
    s = str(value)
    res = [int(n) ** len(s) for n in s]
    return value == sum(res)



print(narcissistic(7), True, '7 is narcissistic')
print(narcissistic(371), True, '371 is narcissistic')
print(narcissistic(122), False, '122 is not narcissistic')
print(narcissistic(4887), False, '4887 is not narcissistic')