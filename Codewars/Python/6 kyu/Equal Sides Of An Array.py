'''
https://www.codewars.com/kata/5679aa472b8f57fb8c000047/train/python
You are going to be given an array of integers. Your job is to take that array and find an 
index N where the sum of the integers to the left of N is equal to the sum of the integers 
to the right of N. If there is no index that would make this happen, return -1.

For example:

Let's say you are given the array {1,2,3,4,3,2,1}: Your function will return the index 3, 
because at the 3rd position of the array, the sum of left side of the index ({1,2,3}) and 
the sum of the right side of the index ({3,2,1}) both equal 6.

Let's look at another one.
You are given the array {1,100,50,-51,1,1}: Your function will return the index 1, because 
at the 1st position of the array, the sum of left side of the index ({1}) and the sum of the 
right side of the index ({50,-51,1,1}) both equal 1.

'''


def find_even_index(arr):
    for x,y in enumerate(range(len(arr))):
        left_sum = sum(arr[:y])
        right_sum = sum(arr[y+1:])
        # print(left_sum,right_sum)
        if left_sum == right_sum:
            return(x)
    return(-1)

print(find_even_index([1,2,3,4,3,2,1]),3)
print(find_even_index([1,100,50,-51,1,1]),1)
print(find_even_index([1,2,3,4,5,6]),-1)
print(find_even_index([20,10,30,10,10,15,35]),3)
print(find_even_index([20,10,-80,10,10,15,35]),0)
print(find_even_index([10,-80,10,10,15,35,20]),6)
# print(find_even_index(list(range(1,100))),-1)
# print(find_even_index([0,0,0,0,0]),0,"Should pick the first index if more cases are valid")
# print(find_even_index([-1,-2,-3,-4,-3,-2,-1]),3)
# print(find_even_index(list(range(-100,-1))),-1)
