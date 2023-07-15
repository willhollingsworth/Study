def move_zeros(lst):
    return [v for v in lst if v!=0] + [0]*lst.count(0)

print([0]*3)
print(move_zeros(
        [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]),
        [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
print(move_zeros(
        [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
        [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
print(move_zeros([0, 0]), [0, 0])
print(move_zeros([0]), [0])
print(move_zeros([]), [])