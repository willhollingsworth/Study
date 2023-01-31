from codewars_test import test_framework as Test


def increment_string(in_string):
    if not in_string : return str(1) # if blank return 1
    elif not in_string[-1].isdigit(): # if no number at the end
        return in_string + '1'      # chuck a 1 at the end
    else:
        count = 0
        for x in reversed(in_string):  # count up number of trailing digits
            if x.isdigit():
                count += 1
            else : break
        # print(in_string,'has',count,'digits')
        new_num = int(in_string[-count:])+1  # grab the trailing number and increment it
        missing_zeros = len(in_string[-count:]) - len(str(new_num)) #calc if there are missing zeros
        if missing_zeros > 0: # if there are
            new_num = '0'*missing_zeros + str(new_num) # then add them to the start of new num
        return in_string[:-count]+str(new_num) #return orginal string letter + new num



Test.assert_equals(increment_string('tig_N0458888Z)b55342v7160+GI698~&sxe0390679772Yes_*~r571442inbp*(198357087715000001'), 'tig_N0458888Z)b55342v7160+GI698~&sxe0390679772Yes_*~r571442inbp*(198357087715000002')
Test.assert_equals(increment_string("foo"), "foo1")
Test.assert_equals(increment_string("foobar001"), "foobar002")
Test.assert_equals(increment_string("foobar1"), "foobar2")
Test.assert_equals(increment_string("foobar00"), "foobar01")
Test.assert_equals(increment_string("foobar99"), "foobar100")
Test.assert_equals(increment_string("foobar099"), "foobar100")
Test.assert_equals(increment_string(""), "1")


# 'tig_N0458888\\Z)b55342v7160+GI698~&sxe0390679772Yes_*~r571442inbp*(198357087715000001' should equal 'tig_N0458888\\Z)b55342v7160+GI698~&sxe0390679772Yes_*~r571442inbp*(198357087715000010'