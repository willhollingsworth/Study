from codewars_test import test_framework as Test
from collections import Counter

def first_non_repeating_letter(string):

    o = Counter(string.lower())
    for x in string:
        if o[x.lower()] == 1:
            return x    
    return ''
    
# first_non_repeating_letter('stress')

Test.describe('Basic Tests')
Test.it('should handle simple tests')
Test.assert_equals(first_non_repeating_letter('a'), 'a')
Test.assert_equals(first_non_repeating_letter('stress'), 't')
Test.assert_equals(first_non_repeating_letter('moonmen'), 'e')

Test.it('should handle empty strings')
Test.assert_equals(first_non_repeating_letter(''), '')

Test.it('should handle all repeating strings') 
Test.assert_equals(first_non_repeating_letter('abba'), '')
Test.assert_equals(first_non_repeating_letter('aa'), '')

Test.it('should handle odd characters')
Test.assert_equals(first_non_repeating_letter('~><#~><'), '#')
Test.assert_equals(first_non_repeating_letter('hello world, eh?'), 'w')

Test.it('should handle letter cases')
Test.assert_equals(first_non_repeating_letter('sTreSS'), 'T')
Test.assert_equals(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!'), ',')