import codewars_test as test

#finished it 70% but gave up on the last section

def order_weight(in_string):
    working_list = []
    out_list = []

    # build 2d list of summed values
    for x in in_string.split():  
        temp_sum = 0
        for y in x:
            temp_sum += int(y)
        working_list += [[x,temp_sum]]
    # print(working_list)

    # sort list by second value
    working_list = sorted(working_list, key=
                        lambda  x: x[1])
    # print(working_list)
    for x in range(len(working_list)):
        out_list.append(working_list[x][0])
    output = ' '.join(out_list)
    print ('input is',in_string)
    print ('output is',output)
    return output




# order_weight("99 100 29 30")

test.assert_equals(order_weight("103 123 4444 99 2000"), "2000 103 123 4444 99")
test.assert_equals(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"), "11 11 2000 10003 22 123 1234000 44444444 9999")
# test.assert_equals(order_weight(""), "")
