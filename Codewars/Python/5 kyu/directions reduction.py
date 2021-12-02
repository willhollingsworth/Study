'''https://www.codewars.com/kata/550f22f4d758534c1100025a/train/python

'''

# directions = { "NORTH":"SOUTH" ,  "EAST":"WEST" }
# directions_flipped = {directions[x] : x for x in directions.keys()}
# directions = {**directions, **directions_flipped}
# print(directions)
directions_pair = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}


opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}

def dirReduc(plan):
    new_plan = []
    for d in plan:
        if new_plan and new_plan[-1] == opposite[d]:
            new_plan.pop()
        else:
            new_plan.append(d)
    return new_plan






# def dirReduc(arr):
#     processing = True
#     up_to = 0
#     processing_list = list(enumerate(arr))
#     while processing:
#         remaining = len(arr) - up_to

#         for x,y in processing_list[up_to:]:
#             previous = x - 1
#             if x <= up_to and remaining != 1: # if at the start and length isnt 0
#                 continue
#             elif processing_list[previous][1] == directions_pair[y]:  # if last entry matches current oposite
#                 del arr[ previous : previous + 2]
#                 up_to = x-1
#                 break
#             elif x == len(arr)-1:
#                 processing = False
#     return arr


a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
# cProfile.run('dirReduc(a)')
print(dirReduc(a), ['WEST'])
u=["NORTH", "WEST", "SOUTH", "EAST"]
print(dirReduc(u), ["NORTH", "WEST", "SOUTH", "EAST"])

# import cProfile
# import random
# directions = ['NORTH','SOUTH','EAST','WEST']
# c = [random.choice(directions) for x in range(1000)]
# cProfile.run('dirReduc(c)')