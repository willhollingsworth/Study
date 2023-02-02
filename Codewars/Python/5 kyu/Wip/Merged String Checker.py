def is_merge(s, part1, part2):
    position = [0,0]
    for c in s:
        if c in part1:
            old_pos = position[0]
            new_pos = part1.find(c)
            if old_pos > new_pos:
                return False
            position[0] = new_pos
        elif c in part2:
            old_pos = position[1]
            new_pos = part2.find(c)
            if old_pos > new_pos:
                return False
            position[1] = new_pos
        else:
            return False    
    return True


    
# print(is_merge('codewars', 'code', 'wars'))
# print(is_merge('codewars', 'cdw', 'oears'))
# print(is_merge('codewars', 'cod', 'wars'))
print(is_merge("Can we merge it? Yes, we can!", "Cawe erg t? s, we can!", "n meiYe"), ' : should pass, doesn\'t')

# import codewars_test as test
# @test.describe('Merged string checker')
# def desc1():
#     @test.it('Sample tests')
#     def it1():
#         test.assert_equals(is_merge('codewars', 'code', 'wars'), True)
#         test.assert_equals(is_merge('codewars', 'cdw', 'oears'),True)
#         test.assert_equals(is_merge('codewars', 'cod', 'wars'),False)