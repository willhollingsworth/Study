# https://www.codewars.com/kata/54da539698b8a2ad76000228/train/python

def is_valid_walk(list):
    position = [0,0]
    for d in list:
        if d == 'n':
            position[1] += 1
        elif d == 's':     
            position[1] -= 1
        elif d == 'e':     
            position[0] += 1
        elif d == 'w':     
            position[0] -= 1
    if position == [0,0] and len(list) == 10:   
        return True
    return False



# print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))

assert is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']) == False
assert is_valid_walk(['w']) == False
assert is_valid_walk(['n','s','n','s','n','s','n','s','n','s']) == True
assert is_valid_walk(['n','n','n','s','n','s','n','s','n','s']) == False