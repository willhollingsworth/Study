'''
https://www.hackerrank.com/challenges/diagonal-difference/
'''
import math
import random

def rand(max):
    return random.randint(0,max)

def build_random_grid(size):
    arr = []
    for x in range(size):
        arr.append([])
        for y in range(size):
            arr[x].append(rand(10))
    return arr

# print(build_random_grid(3))
# print(build_random_grid(4))

def diagonalDifference(arr):   
    d1 = 0
    d2 = 0 
    for x in range(len(arr)):
        t1 = arr[0+x][0+x]
        t2 = arr[-1-x][0+x]
        d1 += t1
        d2 += t2
    #     print(t1,'    ',t2)
    # print(d1,'    ',d2)
    result = d1-d2
    return result if result>0 else result*-1


arr1 = [[11,4,10],[2,5,8],[4,6,-12]]
# print(diagonalDifference(arr1))
print(diagonalDifference(build_random_grid(5)))



