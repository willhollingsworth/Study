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
    board_checks = []
    for x in board: #horizontal checks
        board_checks.append(x)
    for x in range(3): # vert checks
        board_checks.append([board[0][x],board[1][x],board[2][x]])
    #diag checks
    board_checks.append([board[0][0],board[1][1],board[2][2]])
    board_checks.append([board[0][2],board[1][1],board[2][0]])
    # run all checks
    for check in board_checks:
        check_result = checker(check)
        if check_result:
            return check_result
    for x in board: # unfinished check
        if 0 in x:
            return -1
    return 0


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