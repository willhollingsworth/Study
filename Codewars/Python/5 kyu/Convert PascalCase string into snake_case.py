

def to_underscore(string):
    input = str(string)
    out_string = ''
    for i,c in enumerate(input):
        first, last = i == 0, i == len(input)-1
        if c.isupper() and not any([first,last]) :
            out_string += '_' + c
        else:
            out_string += c
    return str(out_string).lower()


print(to_underscore("TestController"))
print(to_underscore("MoviesAndBookS"))
print(to_underscore("App7Test"))
print(to_underscore(1))



# import codewars_test as test
# @test.describe("Sample tests")
# def sample_tests():
#     @test.it("Tests")
#     def it_1():
#         test.assert_equals(to_underscore("TestController"), "test_controller")
#         test.assert_equals(to_underscore("MoviesAndBooks"), "movies_and_books")
#         test.assert_equals(to_underscore("App7Test"), "app7_test")
#         test.assert_equals(to_underscore(1), "1")