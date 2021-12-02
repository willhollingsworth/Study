'''
Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the row sums of this triangle from the row index (starting at index 1) e.g.:

row_sum_odd_numbers(1); # 1
row_sum_odd_numbers(2); # 3 + 5 = 8


comments - this is a very simple maths problem, not sure its a great
programming question

'''

odd_number_list = []
row_start = []
#find odd number ranges
for x in range(10000000):
    if x == 0:
        odd_number_list.append(1)
    else:
        odd_number_list.append(odd_number_list[x-1]+2)
# print(odd_number_list)

#find start point of each row
for x in range(10000000):
    if x == 0:
        row_start.append(0)
        old=0
    else:
        row_start.append(row_start[x-1]+x)
# print(row_start)

def row_sum_odd_numbers(num):
    # val = sum(odd_number_list[row_start[num-1]:[row_start[num-1]+num]])
    # print(row_start[num-1],row_start[num-1]+num) # select  the correct ranges in the list
    # print(odd_number_list[row_start[num-1]:row_start[num-1]+num]) # print the selected values
    return(sum(odd_number_list[row_start[num-1]:row_start[num-1]+num])) # sum them
print(row_sum_odd_numbers(1))
print(row_sum_odd_numbers(2))
print(row_sum_odd_numbers(3))
print(row_sum_odd_numbers(13))
print(row_sum_odd_numbers(19))
print(row_sum_odd_numbers(41))

# print(odd_number_list[row_start[1-1]:[row_start[1-1]+1-1]])
# num=2
# print([row_start[num-1],row_start[num-1]+num])