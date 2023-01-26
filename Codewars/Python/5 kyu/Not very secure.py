import codewars_test as test
import re
def alphanumeric(password):
    re_exp = re.compile('''
    ^[a-zA-Z0-9]+$
    ''',re.VERBOSE)
    return re.search(re_exp,password) is not None


print(alphanumeric("helloworld"))
print(alphanumeric(" "))
print(alphanumeric("hello world_"))


# @test.describe("Sample Tests")
# def sample_tests():
#     tests = [
#         ("hello world_", False),
#         ("PassW0rd", True),
#         ("     ", False)
#     ]
#     for s, b in tests:
#         @test.it('alphanumeric("' + s + '")')
#         def sample_test():
#             test.assert_equals(alphanumeric(s), b)