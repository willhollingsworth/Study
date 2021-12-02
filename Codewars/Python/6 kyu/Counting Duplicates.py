# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1
# Write a function that will return the count of distinct case-insensitive 
# alphabetic characters and numeric digits that occur more than once in the 
# input string. The input string can be assumed to contain only alphabets 
# (both uppercase and lowercase) and numeric digits.


from codewars_test import test_framework as test

def duplicate_count(in_string):
    in_string = in_string.lower()
    count = 0
    counted = ''
    for x in in_string:
        occurences = in_string.count(x)
        if occurences > 1 and x not in counted:
            count += 1
            counted += x
    return count




# print(duplicate_count(''),0)
# print(duplicate_count('abcde'),0)
# print(duplicate_count('abcdeaa'),1)
# print(duplicate_count('abcdeaB'),2)
# print(duplicate_count('Indivisibilities'),2)


test.assert_equals(duplicate_count(""), 0)
test.assert_equals(duplicate_count("abcde"), 0)
test.assert_equals(duplicate_count("abcdeaa"), 1)
test.assert_equals(duplicate_count("abcdeaB"), 2)
test.assert_equals(duplicate_count("Indivisibilities"), 2)