import codewars_test as test

def checker(spots):
    if 0 in spots : 
        return
    elif sum(spots) == 6:
            return 2
    elif sum(spots) == 3:
            return 1

def is_solved(board):
    result = 0
    for x in board: #horizontal checks
        result = checker(x) if checker(x) else result
    for x in range(3): # vert checks
        column = [board[0][x],board[1][x],board[2][x]]
        result = checker(column) if checker(column) else result
    #diagonal checks    
    diagonal1 = [board[0][0],board[1][1],board[2][2]]
    result = checker(diagonal1) if checker(diagonal1) else result
    diagonal2 = [board[0][2],board[1][1],board[2][0]]
    result = checker(diagonal2) if checker(diagonal2) else result
    
    if result ==0: # unfinished checker
        for x in board:
            if 0 in x:
                return -1
    return result


# not yet finished
board = [[0, 0, 1],
         [0, 1, 2],
         [2, 1, 0]]
test.assert_equals(is_solved(board), -1)

# winning row
board = [[1, 1, 1],
         [0, 2, 2],
         [0, 0, 0]]
test.assert_equals(is_solved(board), 1)

# winning column
board = [[2, 1, 2],
         [2, 1, 1],
         [1, 1, 2]]
test.assert_equals(is_solved(board), 1)

# draw
board = [[2, 1, 2],
         [2, 1, 1],
         [1, 2, 1]]
test.assert_equals(is_solved(board), 0)