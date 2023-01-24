import codewars_test as test




def persistence(n):
    count = 0 
    result = str(n)
    while len(result) > 1:
        count += 1
        temp_result = 1
        for character in result:
            temp_result *= int(character)
        result = str(temp_result)
    return count

# print(persistence(39), 3)
test.assert_equals(persistence(39), 3)
test.assert_equals(persistence(4), 0)
test.assert_equals(persistence(25), 2)
test.assert_equals(persistence(999), 4)
