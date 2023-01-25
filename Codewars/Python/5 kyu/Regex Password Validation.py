from re import search,compile,VERBOSE
import codewars_test as test


regex1 = '^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=\w{6,})(?=^[a-zA-Z0-9]*$)'
# cleaner looking example using re's compile
regex2 = compile('''
^
(?=.*[a-z])
(?=.*[A-Z])
(?=.*[0-9])
(?=\w{6,})
(?=^[a-zA-Z0-9]*$)
''',VERBOSE)

# can also use a tuple to combine multi lines into a single long string

regex3 = (
'^'
'(?=.*[a-z])'
'(?=.*[A-Z])'
'(?=.*[0-9])'
'(?=\w{6,})'
'(?=^[a-zA-Z0-9]*$)'    
)

regex = regex3
print(search(regex, 'fjd3IR9'))
print(search(regex, 'aaa'))
# test.describe("Basic tests")
test.assert_equals(bool(search(regex, 'ghdfj32')), False)
test.assert_equals(bool(search(regex, 'DSJKHD23')), False)
test.assert_equals(bool(search(regex, 'fjd3IR9')), True)
test.assert_equals(bool(search(regex, 'dsF43')), False)
test.assert_equals(bool(search(regex, '4fdg5Fj3')), True)
test.assert_equals(bool(search(regex, 'DHSJdhjsU')), False)
test.assert_equals(bool(search(regex, 'fjd3IR9.;')), False)
test.assert_equals(bool(search(regex, 'fjd3  IR9')), False)
test.assert_equals(bool(search(regex, 'djI38D55')), True)
test.assert_equals(bool(search(regex, 'a2.d412')), False)
test.assert_equals(bool(search(regex, 'JHD5FJ53')), False)
test.assert_equals(bool(search(regex, '!fdjn345')), False)
test.assert_equals(bool(search(regex, 'jfkdfj3j')), False)
test.assert_equals(bool(search(regex, '123')), False)
test.assert_equals(bool(search(regex, 'abc')), False)
test.assert_equals(bool(search(regex, '123abcABC')), True)
test.assert_equals(bool(search(regex, 'ABC123abc')), True)
test.assert_equals(bool(search(regex, 'Password123')), True)