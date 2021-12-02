'''
Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.

For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.
'''



def sum_two_smallest_numbers(numbers):
    val1 = min(numbers)
    numbers.remove(val1)
    val2 = min(numbers)
    return val1 +val2


print(sum_two_smallest([5, 8, 12, 18, 22]))
print(sum_two_smallest([25, 42, 12, 18, 22]))


# Test.assert_equals(sum_two_smallest_numbers([5, 8, 12, 18, 22]), 13)
# Test.assert_equals(sum_two_smallest_numbers([7, 15, 12, 18, 22]), 19)
# Test.assert_equals(sum_two_smallest_numbers([25, 42, 12, 18, 22]), 30)