'''https://www.codewars.com/kata/526571aae218b8ee490006f4/train/python

Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
'''
from datetime import datetime




def count_bits(n):
    print('attempting',n, end='  ')
    start_bit = 256
    bits = 0
    while not n < 1 :
        if n > start_bit*2:
            start_bit *= 4
            continue
        if n >= start_bit:
            bits += 1
            n -= start_bit
        start_bit /= 2
    return bits


print(count_bits(0), 0)
print(count_bits(4), 1)
print(count_bits(7), 3)
print(count_bits(9), 2)
print(count_bits(10), 2)    
print(count_bits(256), 2)    
print(count_bits(4521), 2)    
print(count_bits(999999), 2)    
print(count_bits(11331230), 2)    
print(count_bits(10), 2)    
print(count_bits(10), 2)    
print(count_bits(10), 2)    


