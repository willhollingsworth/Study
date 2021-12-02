import codewars_test as Test

def valid_parentheses(in_string):
    opens = (in_string.count('('))
    closes = (in_string.count(')'))

    if opens != closes : return False
    current_close = 0
    current_iter = 0
    matched_closes = []

    for x in in_string:
        if x == '(':
            current_close = current_iter
            for y in in_string[current_iter:]:
                if y == ')' and current_close not in matched_closes:
                    matched_closes.append(current_close)
                    break
                elif current_close == len(in_string)-1:
                    return False
                current_close += 1    
        current_iter += 1
    return True

Test.assert_equals(valid_parentheses("(()"),False)
Test.assert_equals(valid_parentheses("))((()"),False)

# Test.assert_equals(valid_parentheses("  ("),False)
# Test.assert_equals(valid_parentheses(")test"),False)
# Test.assert_equals(valid_parentheses(""),True)
# Test.assert_equals(valid_parentheses("hi())("),False)
# Test.assert_equals(valid_parentheses("hi(hi)()"),True)
