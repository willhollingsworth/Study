# https://www.codewars.com/kata/58b1ae711fcffa34090000ea/train/python
# wip

def controller(events):
    opening = True
    active = False
    out_string = ''
    for i,event in enumerate(events):
        if event == 'P':
            active = not active
        if event == 'O':
            opening = not opening
        if active:
            if i == 0:
                new_value = '1'
            else:
                if opening:
                    delta = 1
                elif not opening:
                    delta = -1
                new_value = str( int( out_string[-1]) + delta)
                nv_int = int(new_value)
                if nv_int > 5 or nv_int < 0:
                    active = False
                    opening = not opening
                    if nv_int > 5:
                        new_value = '5'
                    else:
                        new_value = '0'
        elif not active:
            if i == 0:
                new_value = '0'
            else:
                new_value = out_string[-1]
        out_string += new_value
    return out_string
            


print('Uninterrupted operation')
print(controller('..........'), '0000000000')
print(controller('P....'), '12345')

print('Operation paused')
print(controller('P.P..'), '12222')

# print('Obstacle detected')
print(controller('..P...O...'), '0012343210')
print(controller('..P................'))
print(controller('..P........P.........'))