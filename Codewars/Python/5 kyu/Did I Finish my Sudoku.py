from codewars_test import test_framework as test
from collections import Counter


#nfi why this doesnt work

def done_or_not(board): #board[i][j]
    # print(board)
    debug = ''
    for row in range(9):  #iter over each row
        for rowcount in Counter(board[row]).values():
            if rowcount != 1:
                return 'Try again!' 
            # debug += str(rowcount)
        col_temp = []
        for col in range(9): # iter over each col
            col_temp.append(board[col][row]) # build temp list of column
        for colcount in Counter(col_temp).values():
            # debug += str(colcount)
            if colcount != 1:
                return 'Try again!' 
        # if col_total != 45 :
        #     return 'Try again!' 
    # print(debug)
    return 'Finished!'

test.assert_equals(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]), 'Finished!');
                        
test.assert_equals(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 3, 5]]), 'Try again!');

test.assert_equals(done_or_not([[1, 2, 3, 4, 5, 6, 7, 8, 9]
                        , [2, 3, 4, 5, 6, 7, 8, 9, 1]
                        , [3, 4, 5, 6, 7, 8, 9, 1, 2]
                        , [4, 5, 6, 7, 8, 9, 1, 2, 3]
                        , [5, 6, 7, 8, 9, 1, 2, 3, 4]
                        , [6, 7, 8, 9, 1, 2, 3, 4, 5]
                        , [7, 8, 9, 1, 2, 3, 4, 5, 6]
                        , [8, 9, 1, 2, 3, 4, 5, 6, 7]
                        , [9, 1, 2, 3, 4, 5, 6, 7, 8]]), 'Try again!');