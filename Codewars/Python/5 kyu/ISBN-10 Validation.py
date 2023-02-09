def valid_ISBN10(isbn):
    if not len(isbn) == 10:
        return False
    sum = 0
    for i,x in enumerate(isbn):
        if i == 9 and x == 'X':
            num = 10
        else:
            num = x
            if not num.isdigit():
                return False
        sum += int(num) * (i+1)
    if sum % 11 == 0:
        return True
    else:
        return False

# print(valid_ISBN10('1112223339'))
print(valid_ISBN10('048665088X'))
# print(valid_ISBN10('1293000000'))
# print(valid_ISBN10('1234554321'))
# print(valid_ISBN10('1234512345'))
# print(valid_ISBN10('1293'))
# print(valid_ISBN10('X123456788'))
# print(valid_ISBN10('ABCDEFGHIJ'))
# print(valid_ISBN10('XXXXXXXXXX'))
# print(valid_ISBN10('123456789T'))




# import codewars_test as test

# @test.describe("Sample tests")
# def tests():
#     @test.it("Some examples")
#     def tests():
#         test.assert_equals(valid_ISBN10('1112223339'), True)
#         test.assert_equals(valid_ISBN10('048665088X'), True)
#         test.assert_equals(valid_ISBN10('1293000000'), True)
#         test.assert_equals(valid_ISBN10('1234554321'), True)
#         test.assert_equals(valid_ISBN10('1234512345'), False)
#         test.assert_equals(valid_ISBN10('1293'), False)
#         test.assert_equals(valid_ISBN10('X123456788'), False)
#         test.assert_equals(valid_ISBN10('ABCDEFGHIJ'), False)
#         test.assert_equals(valid_ISBN10('XXXXXXXXXX'), False)
#         test.assert_equals(valid_ISBN10('123456789T'), False)