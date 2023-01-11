import day2_input
input = day2_input.input
# print(input)
#  A for Rock, B for Paper, and C for Scissors
#  X for Rock, Y for Paper, and Z for Scissors
#  X lose,  Y draw , Z win
# input = '''
# C Z
# '''


score = 0
win =  {'A':'Y','B':'Z','C':'X'}
loss = {'A':'Z','B':'X','C':'Y'}
draw = {'A':'X','B':'Y','C':'Z'}
shape_points = {'X':1, 'Y':2, 'Z':3}

for match in input.split('\n'):
    if match == '' : continue
    o = match.split(' ')[0] # opponent choice 
    r = match.split(' ')[1] # match result
    m = '' # my choice
    # calc result
    if r == 'X':
        m = loss[o]
    elif r == 'Y':
        m = draw[o]
        score += 3
    elif r == 'Z':
        m = win[o]
        score += 6
    # calc score    
    score += shape_points[m]
print(score)