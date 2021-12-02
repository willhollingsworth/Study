def array_diff(a, b):
    if a == [] : return []
    for x in b: #find duplicates a to b
        while x in a:
            a.remove(x)
    return a
    
    
    
    
    # for y in b:
    #     while y in a:
    #         a.remove(y)
    # return a + b
print(array_diff([1,2], [1]), [2])
print(array_diff([1,2,2], [1]), [2,2])
print(array_diff([20, 16, -16, -3, 3, 20, 19, 19], [-20, 15, -6, 1]), [20, 16, -16, -3, 3, 20, 19, 19])

import codewars_test as test

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(array_diff([1,2], [1]), [2], "a was [1,2], b was [1], expected [2]")
        test.assert_equals(array_diff([1,2,2], [1]), [2,2], "a was [1,2,2], b was [1], expected [2,2]")
        test.assert_equals(array_diff([1,2,2], [2]), [1], "a was [1,2,2], b was [2], expected [1]")
        test.assert_equals(array_diff([1,2,2], []), [1,2,2], "a was [1,2,2], b was [], expected [1,2,2]")
        test.assert_equals(array_diff([], [1,2]), [], "a was [], b was [1,2], expected []")
        test.assert_equals(array_diff([1,2,3], [1, 2]), [3], "a was [1,2,3], b was [1, 2], expected [3]")