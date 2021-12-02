'''
https://www.codewars.com/kata/5270d0d18625160ada0000e4/train/python
Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, is to score a throw according to these rules. You will always be given an array with five six-sided dice values.

 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point
A single die can only be counted once in each roll. For example, a given "5" can only count as part of a triplet (contributing to the 500 points) or as a single 50 points, but not both in the same roll.

Example scoring

 Throw       Score
 ---------   ------------------
 5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
 1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
 2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)
In some languages, it is possible to mutate the input to the function. This is something that you should never do. If you mutate the input, you will not be able to pass all the tests.\

'''





def score(dice):
    score_3 = [1000,200,300,400,500,600]
    single_digit = [100,0,0,0,50,0] 
    out_score = 0
    
    dice_count = {}
    for x in range(1,7):
        dice_count[x] = 0

    for single_dice in dice:
        dice_count[single_dice] = dice_count[single_dice] + 1

    for roll,count in dice_count.items():
        # print(roll,count)
        if count < 3:
            out_score += single_digit[roll-1]*count 
        else:
            out_score += single_digit[roll-1]*(count-3) 
            out_score += score_3[roll-1]
    return out_score

print( score( [2, 3, 4, 6, 2] ), 0)
print( score(  [4, 4, 4, 3, 3] ), 400)
print( score(  [2, 4, 4, 5, 4] ), 450)
print( score(  [1, 1, 1, 1, 1] ), 1200)
print( score(  [6, 1, 1, 1, 1] ), 1100)
print( score(  [1, 1, 1, 1, 5] ), 1150)


'''
def score(dice):
    out_score = 0
    for single_dice in dice:
        for score in range(len(score_3)):
            if single_dice == score + 1:
                if dice.count(single_dice) > 2:
                    out_score += score_3[score]
                    for x in range(3):
                        dice.remove(single_dice)
    for single_dice in dice:
        if single_dice == 1:
            out_score += 100
        if single_dice == 5:
            out_score += 50
    return out_score
'''


# latch method
# def score(dice):
#     triple_free = True
#     quad_free = True
#     out_score = 0
#     for single_dice in dice:
#         current_count = dice.count(single_dice)
#         if current_count in [3]: 
#             if triple_free:
#                 triple_free = False
#                 out_score += score_3[single_dice-1]
#         elif current_count in [4]: 
#             if quad_free:
#                 quad_free = False
#                 out_score += score_3[single_dice-1]        
#                 out_score += single_digit[single_dice-1]        
#         elif current_count in [1,2]:
#             out_score += single_digit[single_dice-1]
#         else:
#             out_score += score_3[single_dice-1]
#             out_score += single_digit[single_dice-1]
#             out_score += single_digit[single_dice-1]
#             break