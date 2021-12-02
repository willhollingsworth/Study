import codewars_test as Test

def pig_it(in_string):
    wlis = in_string.split()
    for x in range(len(wlis)):
        if wlis[x] not in '?!':
            wlis[x] = \
            wlis[x][1:] + \
            wlis[x][:1] + \
            'ay'    
    return ' '.join(wlis)




Test.assert_equals(pig_it('Pig latin is cool'),'igPay atinlay siay oolcay')
Test.assert_equals(pig_it('This is my string'),'hisTay siay ymay tringsay')