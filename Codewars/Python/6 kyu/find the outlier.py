
import codewars_test as test

def find_outlier(in_list):
    odds = 0
    evens = 0
    for x in range(3):
        if in_list[x] % 2 == 0:
            evens += 1
        else : 
            odds += 1
    if odds > evens : 
        print('yes')
        for x in in_list:
            if x % 2 == 0:
                return x
    else:
        for x in in_list:
            if x % 2 != 0:
                return x
    return

test.assert_equals(find_outlier([2, 4, 6, 8, 10, 3]), 3)
test.assert_equals(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11)
test.assert_equals(find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)