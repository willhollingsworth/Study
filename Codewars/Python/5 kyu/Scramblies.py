from codewars_test import test_framework as Test


def scramble(s1, s2):
    temp_word = s1
    for char in s2:
        if char in temp_word:
            temp_word = temp_word.replace(char,'',1)
        else:
            return False
    return True



# Test.assert_equals(scramble('rkqodlw', 'world'),  True)
# Test.assert_equals(scramble('cedewaraaossoqqyt', 'codewars'), True)
# Test.assert_equals(scramble('katas', 'steak'), False)
# Test.assert_equals(scramble('scriptjava', 'javascript'), True)
# Test.assert_equals(scramble('scriptingjava', 'javascript'), True)


