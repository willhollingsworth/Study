from math import floor

def grid_index(grid, indexes):
    row_count = len(grid[0])
    # print('row count is',row_count)
    out_string =''
    for x in indexes:
        row = floor((x-1)/row_count)
        column = x-1 - row * row_count
        # print('row is',row,'column is',column)
        out_string += grid[row][column]
        # out_string += grid[column][x-1-column]
    return (out_string)

# grid_index([['a','b','c'],['e','f','g']],[1,2,3,4,5,6])
print(grid_index([['m', 'y', 'e'], ['x', 'a', 'm'], ['p', 'l', 'e']], [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print('myexample')
print(grid_index([['m', 'y', 'e'], ['x', 'a', 'm'], ['p', 'l', 'e']], [1, 5, 6]))
print('mam')
print(grid_index([['m', 'y', 'e'], ['x', 'a', 'm'], ['p', 'l', 'e']], [1, 3, 7, 8]))
print('mepl')
print(grid_index([['h', 'e', 'l', 'l'], ['o', 'c', 'o', 'd'], ['e', 'w', 'a', 'r'], ['r', 'i', 'o', 'r']], [5, 7, 9, 3, 6, 6, 8, 8, 16, 13]))
print('ooelccddrr')