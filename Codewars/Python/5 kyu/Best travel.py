from codewars_test import test_framework as Test
import itertools as it

def choose_best_sum(distance, towns, in_list):
    tlist = []
    combos = it.combinations(in_list,towns) #create list with all combinations
    for x in combos:
        tlist.append([x,sum(x)])    #create list with the sum of those combinations
    tlist = list(filter(lambda x : x[1] <= distance,tlist)) # filter the list, removing invalid entries
    tlist.sort(key=lambda x:x[1])  # sort the list by the second element
    return tlist[-1][1] if tlist else None # return the last element if tlist is not empty



# choose_best_sum(10,2,[5,8,3,4])

Test.it("Bigger numbers")
xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
Test.assert_equals(choose_best_sum(230, 4, xs), 230)
Test.assert_equals(choose_best_sum(430, 5, xs), 430)
Test.assert_equals(choose_best_sum(430, 8, xs), None)
