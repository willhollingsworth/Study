
def count_occurences(list):
    # build a dictionary
    occurences = {}
    for x in list:
        occurences[x] = int(occurences.get(x) or 0) + 1
    return occurences

def find_uneven(dict):
    for x,y in dict.items():
        if y%2:
            return x

def find_it(seq):
    occurences = count_occurences(seq)
    return find_uneven(occurences)
print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))
# from codewars_test import test_framework as test
# def sample_tests():
    
#     @test.it("find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]) should return 5 (because it appears 3 times)")
#     def _():
#         test.assert_equals(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)
        
#     @test.it("find_it([1,1,2,-2,5,2,4,4,-1,-2,5]) should return -1 (because it appears 1 time)")
#     def _():
#         test.assert_equals(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]), -1);
        
#     @test.it("find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]) should return 5 (because it appears 3 times)")
#     def _():
#         test.assert_equals(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]), 5);
        
#     @test.it("find_it([10]) should return 10 (because it appears 1 time)")
#     def _():
#         test.assert_equals(find_it([10]), 10);

#     @test.it("find_it([10, 10, 10]) should return 10 (because it appears 3 times)")
#     def _():
#         test.assert_equals(find_it([10, 10, 10]), 10);        
        
#     @test.it("find_it([1,1,1,1,1,1,10,1,1,1,1]) should return 10 (because it appears 1 time)")
#     def _():
#         test.assert_equals(find_it([1,1,1,1,1,1,10,1,1,1,1]), 10);

#     @test.it("find_it([5,4,3,2,1,5,4,3,2,10,10]) should return 1 (because it appears 1 time)")
#     def _():
#         test.assert_equals(find_it([5,4,3,2,1,5,4,3,2,10,10]), 1);
        
# sample_tests()
