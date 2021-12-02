
def over_the_road(address, length):
    if (address % 2) == 0:
        return(length*2) - address + 1 
    else:
        return ((length*2)-address+1)
#iterate process, too slow
# def overroad(address,length):

    
#     street = []
#     for x in range(length):
#         s1 = x*2+1
#         s2 = (length*2)-x*2
#         if address == s1:
#             return str(s2)
#         elif address == s2: 
#             return str(s1)    




print(over_the_road(1,3))
print(over_the_road(3,3))
print(over_the_road(2,3))
print(over_the_road(3,5))
print(over_the_road(7,11))
