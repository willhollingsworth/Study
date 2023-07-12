def land_perimeter(str) -> str:
    total = 0
    arr = [[x for x in y] for y in str ]
    for y,row in enumerate(arr):
        for x,val in enumerate(row):
            total += calc_perimeter(arr,x,y,val)
    return f'Total land perimeter: {total}'

def calc_perimeter(arr,x,y,val) -> int:
    neighbors = calc_neighbors(arr,x,y)
    if val == 'X':
        return 4 - neighbors
    else:
        return 0
 
def calc_neighbors(arr,x,y):
    neighbors = 0
    offsets = [[1,0],[-1,0],[0,1],[0,-1]]
    for off_x,off_y in offsets:
        new_x = x + off_x
        new_y = y + off_y
        if new_x < 0 or new_y < 0:
            continue
        if new_x > len(arr[0]) - 1 or new_y > len(arr) - 1:
            continue
        if arr[new_y][new_x] == 'X':
            neighbors += 1
    return neighbors



print(land_perimeter(["OXOOOX", "OXOXOO", "XXOOOX", "OXXXOO", "OOXOOX", "OXOOOO", "OOXOOX", "OOXOOO", "OXOOOO", "OXOOXX"]), "Total land perimeter: 60")
print(land_perimeter(["OXOOO", "OOXXX", "OXXOO", "XOOOO", "XOOOO", "XXXOO", "XOXOO", "OOOXO", "OXOOX", "XOOOO", "OOOXO"]), "Total land perimeter: 52")
print(land_perimeter(["XXXXXOOO", "OOXOOOOO", "OOOOOOXO", "XXXOOOXO", "OXOXXOOX"]), "Total land perimeter: 40")
print(land_perimeter(["XOOOXOO", "OXOOOOO", "XOXOXOO", "OXOXXOO", "OOOOOXX", "OOOXOXX", "XXXXOXO"]), "Total land perimeter: 54")
print(land_perimeter(["OOOOXO", "XOXOOX", "XXOXOX", "XOXOOO", "OOOOOO", "OOOXOO", "OOXXOO"]), "Total land perimeter: 40")