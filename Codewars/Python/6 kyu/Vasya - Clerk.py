'''
The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line. Each of them has a single 100, 50 or 25 dollar bill. An "Avengers" ticket costs 25 dollars.

Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

Can Vasya sell a ticket to every person and give change if he initially has no money and sells the tickets strictly in the order people queue?

Return YES, if Vasya can sell a ticket to every person and give change with the bills he has at hand at that moment. Otherwise return NO.

Examples:
tickets([25, 25, 50]) # => YES 
tickets([25, 100]) # => NO. Vasya will not have enough money to give change to 100 dollars
tickets([25, 25, 50, 50, 100]) # => NO. Vasya will not have the right bills to give 75 dollars of change (you can't make two bills of 25 from one of 50)
'''


'''inital attempt, more readable but longer
def tickets(people):
    til=[]
    for x in people:
        t2c = til.count(25)
        t5c = til.count(50)
        if x==25:
            til.append(25)
        elif x==50 and t2c>0:
            til.append(50)
            til.remove(25)
        elif x==100 and t5c>0 and t2c>0:
            til.remove(25)
            til.remove(50)
        elif x==100 and t2c>2:
            til.remove(25)
            til.remove(25)
            til.remove(25)
        else: return 'NO'
    return 'YES'



'''




# slightly shorter but harder to read
# def tickets(people):
#     til=[]
#     for x in people:
#         t2c = til.count(25)
#         t5c = til.count(50)
#         if x==25:
#             til.append(25)
#         elif t2c>0:
#             til.remove(25)
#             if x==50:
#                 til.append(50)
#             elif x==100 :
#                 if t5c>0:
#                     til.remove(50)
#                 elif t2c>2:
#                     til.remove(25)
#                     til.remove(25)

#                 else: return 'NO'
#             else: return 'NO'
#         else: return 'NO'
#     return 'YES'


#best solution online
def tickets(people):
    till = {100.0:0, 50.0:0, 25.0:0}

    for paid in people:
        till[paid] += 1
        change = paid-25.0
        
        for bill in (50,25):
            while (bill <= change and till[bill] > 0):
                till[bill] -= 1
                change -= bill

        if change != 0:
            return 'NO'      
    return 'YES'


print(tickets([25,25, 50]), "YES")
print(tickets([25,50,25, 100]), "YES")
print(tickets([25,50,100]), "NO")
print(tickets([25,50,25,100,25,25,25,25,50,100]), "YES")
print(tickets([25,100]), "NO")
