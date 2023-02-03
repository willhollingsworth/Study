def next_gen(cells):
    output_cell = []
    for y in range(len(cells)):
        temp_col = []
        for x in range(len(cells[0])):
            new_value = calc_new_value(cells,[x,y])
            temp_col.append(new_value)
        output_cell.append(temp_col)
    return output_cell

def calc_new_value(cells,coords):
    alive_neighbors = find_alive_neighbors(cells,coords)
    cell_state = cells[coords[1]][coords[0]]
    if cell_state:
        if not alive_neighbors in [2,3]:
            cell_state = 0
    else :
        if alive_neighbors == 3:
            cell_state = 1
    return cell_state

def find_alive_neighbors(cells,coords):
    x1,y1 = coords
    alive_neighbors = 0
    lengths = [len(cells[0]),len(cells)]
    for x2 in range(-1,2):
        for y2 in range(-1,2):
            if x2 == 0 and y2 == 0:
                continue
            new_coords = [x1+x2, y1+y2]
            if calc_out_of_range(new_coords,lengths):
                continue
            neighbor = cells[new_coords[1]][new_coords[0]]
            if neighbor:
                alive_neighbors +=1
    return alive_neighbors

def calc_out_of_range(coords,lengths):
    for i,c in enumerate(coords):
         if c < 0 or c > lengths[i]-1:
            return True
    return False

def print_cells(cells):
    for lines in cells:
        for x in lines:
            if x:
                print(' X ',end='')
            else:
                print(' . ',end='')
        print()
    return

# cells = [[0,1,0],[0,1,0],[0,1,0]]
cells = [[1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 0, 1], [1, 0, 1, 0, 1, 1, 1], [0, 1, 1, 1, 1, 0, 1], [0, 1, 1, 1, 0, 0, 1], [0, 1, 0, 1, 1, 0, 1], [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 1], [1, 0, 1, 1, 0, 1, 1], [1, 0, 0, 1, 0, 0, 1], [0, 0, 1, 0, 0, 1, 0], [0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 1, 0, 1], [0, 1, 1, 0, 1, 1, 0], [1, 0, 0, 0, 1, 1, 1], [0, 1, 0, 0, 1, 0, 0], [0, 1, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0]]
print_cells(cells)
print()
print_cells(next_gen(cells))



# from preloaded import htmlize
# import codewars_test as test

# def do_test (input, expected):
#     str_input = input
#     str_expected = expected
#     actual = next_gen(input)
#     str_actual = actual
#     # test.assert_equals(actual, expected, f'for universe:\n{str_input}\nexpected:\n{str_expected}\nbut got:\n{str_actual}')
#     test.assert_equals(actual, expected)

# @test.describe("fixed tests")
# def sample_tests():

#     @test.it('blinker')
#     def blinker():
#         do_test([
#             [0,1,0],
#             [0,1,0],
#             [0,1,0]
#         ], [
#             [0,0,0],
#             [1,1,1],
#             [0,0,0]
#         ])

#     @test.it('glider')
#     def glider():
#         do_test([
#             [1,0,0,0,0,0,0],
#             [0,1,1,0,0,0,0],
#             [1,1,0,0,0,0,0],
#             [0,0,0,0,0,0,0],
#             [0,0,0,0,0,0,0]
#         ], [
#             [0,1,0,0,0,0,0],
#             [0,0,1,0,0,0,0],
#             [1,1,1,0,0,0,0],
#             [0,0,0,0,0,0,0],
#             [0,0,0,0,0,0,0]
#         ])

#     @test.it('block')
#     def block():
#         do_test([
#             [1,1],
#             [1,1]
#         ], [
#             [1,1],
#             [1,1]
#         ])

#     @test.it('pulsar')
#     def pulsar():
#         do_test([
#             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#             [0,0,0,1,1,1,0,0,0,1,1,1,0,0,0],
#             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#             [0,1,0,0,0,0,1,0,1,0,0,0,0,1,0],
#             [0,1,0,0,0,0,1,0,1,0,0,0,0,1,0],
#             [0,1,0,0,0,0,1,0,1,0,0,0,0,1,0],
#             [0,0,0,1,1,1,0,0,0,1,1,1,0,0,0],
#             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#             [0,0,0,1,1,1,0,0,0,1,1,1,0,0,0],
#             [0,1,0,0,0,0,1,0,1,0,0,0,0,1,0],
#             [0,1,0,0,0,0,1,0,1,0,0,0,0,1,0],
#             [0,1,0,0,0,0,1,0,1,0,0,0,0,1,0],
#             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#             [0,0,0,1,1,1,0,0,0,1,1,1,0,0,0],
#             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#         ], [
#             [0,0,0,0,1,0,0,0,0,0,1,0,0,0,0],
#             [0,0,0,0,1,0,0,0,0,0,1,0,0,0,0],
#             [0,0,0,0,1,1,0,0,0,1,1,0,0,0,0],
#             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#             [1,1,1,0,0,1,1,0,1,1,0,0,1,1,1],
#             [0,0,1,0,1,0,1,0,1,0,1,0,1,0,0],
#             [0,0,0,0,1,1,0,0,0,1,1,0,0,0,0],
#             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#             [0,0,0,0,1,1,0,0,0,1,1,0,0,0,0],
#             [0,0,1,0,1,0,1,0,1,0,1,0,1,0,0],
#             [1,1,1,0,0,1,1,0,1,1,0,0,1,1,1],
#             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#             [0,0,0,0,1,1,0,0,0,1,1,0,0,0,0],
#             [0,0,0,0,1,0,0,0,0,0,1,0,0,0,0],
#             [0,0,0,0,1,0,0,0,0,0,1,0,0,0,0]
#         ])