import codewars_test as Test



# https://www.codewars.com/kata/542f0c36d002f8cd8a0005e5




def build_empty_list(n):
    list =[]
    for x in range(n):
        list.append(0)
    return list
def seat_first_last(list):
    list[0] = 1
    if len(list) > 1:
        list[-1] = 2
    return list
def calc_closest_neigbour(position,list):
    left_neig = False
    current = position
    while True:
        if list[current-1] != 0:
            left_neig = current-1
            break
        else:
            current -= 1

    right_neig = False
    current = position
    while True:
        if list[current+1] != 0:
            right_neig = current+1
            break
        else:
            current += 1
    if left_neig < right_neig : 
        return left_neig
    else:
        return right_neig

def last_chair(n):
    chairs = build_empty_list(n)
    chairs = seat_first_last(chairs)
    distance = 0
    for x in range(n):
        if x == 0 or x == 1:
            continue
        for place,value in enumerate(chairs):
            if value == 0:
                distance = calc_closest_neigbour(place,chairs)
                print(place,distance)
            
    print(chairs)

# test1 = [1,0,0,3,0,0,0,0,2,0,0,0,0,0,0]
# test1 = [1,0,1,0,0,0,1,0,0,0,0,0,1]
# find_longest_space(test1)
# Test.assert_equals(last_chair(10), 9, 'Your solution failed the example test')


last_chair(4)
# last_chair(5)
# last_chair(6)

'''
last chair
3 = 1,3,2
4 = 1,3,4,2

if 


unused, method didnt work

def find_longest_space(list):
    best = {'length':0,'start':False,'end':False}
    current = {'length':0,'start':False,'end':False}
    for place,value in enumerate(list):
        if value == 0:
            current['length'] += 1
            if list[place-1] != 0:
                current['start'] = place
        if value != 0:
            if place == 0: continue
            if list[place-1] == 0:
                # current space has ended
                current['end'] = place-1
                if current['length'] > best['length']:
                    best = current
                # print('current',current)
                current = {'length':0,'start':False,'end':False}
    return best

if longest_space['length'] % 2 == 0: #length is even
    offset = longest_space['length']/2-1
    position = longest_space['start'] + int(offset)
    chairs[position] = x+1
else:
    offset = longest_space['length']/2
    position = longest_space['start'] + int(offset)
    chairs[position] = x+1


'''


