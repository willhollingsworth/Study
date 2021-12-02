def find_outlier(integers):
    odds = sum([x%2 for x in integers]) >= 2
    for x in integers:
        if x%2 != odds:
            return x

'''
0 0 0 even
1 0 0 even
1 1 0 odd
1 1 1 odd
'''

print(find_outlier([2,4,8]))
print(find_outlier([1,10,8]))
print(find_outlier([1,3,2]))
print(find_outlier([7,5,3]))


# print(find_outlier([2, 4, 6, 8, 10, 3]), 3)
# print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11)
# print(find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)