import day2_input
input = day2_input.input
# print(input)
#  A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors
# input = '''
# C Z
# '''
l = {}
l['win'] = {'A':'Y','B':'Z','C':'X'}
l['loss'] = {'A':'Z','B':'X','C':'Y'}
l['draw'] = {'A':'X','B':'Y','C':'Z'}
result_score = {'win':6 , 'draw':3 , 'loss':0}
shape_score = {'X':1, 'Y':2, 'Z':3}

score = 0
for match in input.split('\n'):
    result = ''
    if match == '' : continue
    o,m = match.split(' ')
    for outcome in l.keys():
        if m == l[outcome][o]:
            result = outcome
    score += result_score[result]
    score += shape_score[m]
print(score)