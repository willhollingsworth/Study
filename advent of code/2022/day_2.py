import day2_input
input = day2_input.input
# print(input)
#  A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors
# input = '''
# C Z
# '''


score = 0
for match in input.split('\n'):
    win = {'A':'Y','B':'Z','C':'X'}
    loss = {'A':'Z','B':'X','C':'Y'}
    draw = {'A':'X','B':'Y','C':'Z'}
    shape = {'X':1, 'Y':2, 'Z':3}
    if match == '':
        continue
    o = match.split(' ')[0]
    m = match.split(' ')[1]
    if m == win[o]:
        score += 6
    elif m == draw[o]:
        score +=3
    score += shape[m]
print(score)