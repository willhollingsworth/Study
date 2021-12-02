import codewars_test as test


## simple method
# def sum_pairs(list,sum):
#     iter = 0
#     for x in range(len(list)):
#         for y in range(x+1,len(list)):
#             if list[x] + list[y] == sum :
#                 print( [list[x], list[y]])
#                 return [list[x], list[y]]
        
#     return None
def sum_pairs(list,sum):
    # mlength = 1 #match length
    iter = 0
    lis_len = len(list)
    for x in range(1,lis_len): # vary the match length from 1 to 
        for y in range(len(list)-x): #item matcher
            if list[y] + list[y+x] == sum :
                return [list[y], list[x+y]]
            # return [list[x], list[y]]



l1= [1, 4, 8, 7, 3, 15]
l2= [1, -2, 3, 0, -6, 1]
l3= [20, -13, 40]
l4= [1, 2, 3, 4, 1, 0]
l5= [10, 5, 2, 3, 7, 5]
l6= [4, -2, 3, 3, 4]
l7= [0, 2, 0]
l8= [5, 9, 13, -3]






test.describe("Testing For Sum of Pairs")
test.expect(sum_pairs(l1, 8) == [1, 7], "Basic: %s should return [1, 7] for sum = 8" % l1)
test.expect(sum_pairs(l2, -6) == [0, -6], "Negatives: %s should return [0, -6] for sum = -6" % l2)
test.expect(sum_pairs(l3, -7) == None, "No Match: %s should return None for sum = -7" % l3)
test.expect(sum_pairs(l4, 2) == [1, 1], "First Match From Left: %s should return [1, 1] for sum = 2 " % l4)
test.expect(sum_pairs(l5, 10) == [3, 7], "First Match From Left REDUX!: %s should return [3, 7] for sum = 10 " % l5)
test.expect(sum_pairs(l6, 8) == [4, 4], "Duplicates: %s should return [4, 4] for sum = 8" % l6)
test.expect(sum_pairs(l7, 0) == [0, 0], "Zeroes: %s should return [0, 0] for sum = 0" % l7)
test.expect(sum_pairs(l8, 10) == [13, -3], "Subtraction: %s should return [13, -3] for sum = 10" % l8)
