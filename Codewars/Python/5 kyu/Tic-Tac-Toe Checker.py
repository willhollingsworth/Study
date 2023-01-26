import codewars_test as test

def checker(spots):
    if spots[0] == spots[1] == spots [2]:
        return spots[0]

def build_check_list(board):
    output_list =[]
    # 3 horizontal, 3 vertical, 2 diagonals 
    board_checks = [
    [0,1,2],    
    [3,4,5],    
    [6,7,8],    
    [0,3,6],    
    [1,4,7],    
    [2,5,8],    
    [0,4,8],    
    [2,4,6],    
    ]
    board_list = board[0] + board[1] + board[2]
    for check in board_checks:
        output_list.append([
            board_list[check[0]],
            board_list[check[1]],
            board_list[check[2]],
        ])
    return output_list

def is_solved(board):
    result = 0
    draw = 0
    unfinished = -1

    #build check lists
    board_checks = build_check_list(board)
    # test all check lists
    for check in board_checks:
        check_result = checker(check)
        if check_result:
            return check_result
    for x in board: # unfinished check
        if 0 in x:
            return unfinished 
    return draw


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